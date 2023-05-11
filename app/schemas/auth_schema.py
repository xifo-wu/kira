from marshmallow import EXCLUDE, INCLUDE, Schema, validates_schema, ValidationError, fields, validates, validate
from app.extensions import db
from app.models import User


class PasswordLoginSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    username = fields.Str(
        required=True,
        error_messages={
            "required": "用户名不能为空"
        }
    )

    password = fields.Str(
        required=True,
        error_messages={
            "required": "密码不能为空"
        }
    )

    @validates_schema
    def validate_username_and_password(self, data, **kwargs):
        u = db.session.scalar(
            db.select(User).filter_by(username=data['username']))

        if u is None:
            raise ValidationError(message="用户不存在", field_name="username")

        if not u.validate_password(data['password']):
            raise ValidationError(message="密码不正确", field_name="pasword")


class RegisterSchema(Schema):
    class Meta:
        unknown = INCLUDE

    username = fields.Str(
        required=True,
        error_messages={
            "required": "用户名不能为空"
        }
    )

    password = fields.Str(
        required=True,
        load_only=True,
        validate=validate.Length(min=8, error="密码必须大于 {min} 位"),
        error_messages={
            "required": "密码不能为空",
        }
    )
