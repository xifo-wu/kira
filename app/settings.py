import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    # -- TMDB 配置开始 -- #
    TMDB_APP_KEY = os.getenv("TMDB_APP_KEY")
    TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/"
    TMDB_IMAGE_BASE_URL_ORIGINAL = "https://image.tmdb.org/t/p/original"

    TMDB_IMAGE_BACKDROP_SIZES = ["w300", "w780", "w1280", "original"]
    TMDB_IMAGE_PROFILE_SIZES = ["w45", "w185", "h632", "original"]
    TMDB_IMAGE_STILL_SIZES = ["w92", "w185", "w300", "original"]
    TMDB_IMAGE_LOGO_SIZES = ["w45", "w92", "w154",
                             "w185", "w300", "w500", "original"]
    TMDB_IMAGE_POSTER_SIZES = ["w92", "w154",
                               "w185", "w342", "w500", "w780", "original"]
    # -- TMDB 配置结束 -- #

    PAGE_SIZE = 20
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'root')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', '')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'app')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'secret_Key')
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}?charset=utf8mb4"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=365)
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

    CELERY = dict(
        broker_url=REDIS_URL,
        result_backend=REDIS_URL,
        task_ignore_result=True,
    )

class DevelopmentConfig(BaseConfig):
    # Flask Sqlalchemy
    SQLALCHEMY_ECHO = True


class ProductionConfig(BaseConfig):
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)


class TestingConfig(BaseConfig):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
