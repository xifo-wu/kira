from app.extensions import db
from app.models.base_model_mixin import BaseModelMixin


class SystemSetting(db.Model, BaseModelMixin):
    telegram_bot_token = db.Column(db.String(255))
    telegram_default_chat = db.Column(db.String(255))
    tmdb_app_key = db.Column(db.String(255))
