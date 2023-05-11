import urllib
import hashlib
from flask_marshmallow import Schema
from marshmallow import EXCLUDE, fields, validate
from app.schemas import BaseSchema

class UserSchema(BaseSchema):
    class Meta:
        unknown = EXCLUDE

    email = fields.Str()
    nickname = fields.Str()
    username = fields.Str()
    avatar_url = fields.Str(allow_none=True)
    gravatar_url = fields.Method('generate_gravatar', dump_only=True)

    def generate_gravatar(self, user):
        if user is None:
            return ""

        if not user.email:
            return ''
        url = "https://www.gravatar.com/avatar/" + \
            hashlib.md5(user.email.lower().encode('utf-8')).hexdigest() + "?"
        url += urllib.parse.urlencode({'s': '128'})

        return url


class ChangePasswordSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    current_password = fields.Str(
        required=True,
        error_messages={
            "required": "当前密码不能为空"
        }
    )

    password = fields.Str(
        required=True,
        validate=validate.Length(min=8, error="密码必须大于 {min} 位"),
        error_messages={
            "required": "密码不能为空"
        }
    )
