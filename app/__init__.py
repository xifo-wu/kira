import os
from flask import Flask
from app.extensions import ma, db, migrate, jwt, redis_client, tmdb
from app.settings import config
from app.api import api
from lib import response
from lib.api_exception import APIRequestError

def create_app(config_name=None) -> Flask:
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
    redis_client.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    tmdb.init_app(app)

def register_blueprints(app: Flask):
    app.register_blueprint(api, url_prefix='/api')

    # 注册 API 请求错误
    app.register_error_handler(400, response.bad_request)
    app.register_error_handler(403, response.forbidden)
    app.register_error_handler(404, response.page_not_found)
    app.register_error_handler(405, response.method_not_allowed)
    app.register_error_handler(429, response.ratelimit_handler)
    app.register_error_handler(APIRequestError, response.api_request_error)
