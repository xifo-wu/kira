from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from app.extensions.redis import RedisClient
from app.extensions.tmdb import TMDB

tmdb = TMDB()

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
redis_client = RedisClient()
ma = Marshmallow()
