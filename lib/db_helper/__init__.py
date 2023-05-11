from .find_or_create_by import find_or_create_by


def find_by(db, model, **kwargs):
    # 查询条件
    filters = {key: value for key,
               value in kwargs.items() if hasattr(model, key)}

    try:
        record = db.session.execute(
            db.select(model).filter_by(**filters)
        ).scalar_one()
    except Exception:
        record = None

    return record
