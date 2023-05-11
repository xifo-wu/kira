import uuid
from flask import abort, request
from marshmallow import Schema, ValidationError
from lib.api_exception import APIParamsValidationError, APIBadRequestError


def load_schema(schema: Schema, **kwargs):
    try:
        payload = request.get_json()
    except BaseException as e:
        print(e, "API Request Error")
        raise APIBadRequestError()

    try:
        data = schema.load(payload, **kwargs)
    except ValidationError as err:
        print(err, "err")
        raise APIParamsValidationError(errors=err)

    return data


def parse_hex_uuid(uuidHexStr):
    try:
        return str(uuid.UUID(uuidHexStr))
    except Exception as e:
        abort(code=400, description={
            "message": "UUID 不正确",
            "meta": {
                "detail": str(e)
            }
        })
