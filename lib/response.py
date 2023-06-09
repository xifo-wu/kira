from flask import request, jsonify


def bad_request(e):
    message = e.description
    meta = None
    if type(e.description) == dict:
        message = e.description.get("message")
        meta = e.description.get("meta")

    if request.path.startswith('/api/'):
        return error(message=message, meta=meta, status_code=400)
    else:
        return e, 400


def forbidden(e=None):
    if request.path.startswith('/api/'):
        return error(message="抱歉，暂无权限", status_code=403)
    else:
        return e, 403


def page_not_found(e):
    if request.path.startswith('/api/'):
        return error(message=e.description, status_code=404)
    else:
        return e, 404


def method_not_allowed(e):
    if request.path.startswith('/api/'):
        return error(message="服务器知道请求方法，但目标资源不支持该方法", status_code=405)
    else:
        return e, 405


def ratelimit_handler(e):
    return error(message="朋友，您操作太频繁了！", status_code=429)


def api_request_error(e):
    return jsonify(e.to_dict()), e.status_code


def format(data=None, message=None, meta=None, success=True, status_code=200):
    result = {
        "success": success,
    }

    if data is not None:
        result["data"] = data

    if message is not None:
        result["message"] = message

    if meta is not None:
        result["meta"] = meta

    return jsonify(result), status_code


def error(message=None, meta=None, success=False, status_code=400):
    result = {
        "success": success,
    }

    if message is not None:
        result["message"] = message

    if meta is not None:
        result["meta"] = meta

    return jsonify(result), status_code
