import sqlalchemy as sa


def find_or_create_by(db, model, **kwargs):
    # 查询条件
    filters = {key: value for key,
               value in kwargs.items() if hasattr(model, key)}

    # 查询数据库是否已经存在符合条件的记录
    try:
        record = db.session.execute(
            db.select(model).
            filter_by(**filters)
        ).scalar_one()
    except (sa.exc.NoResultFound, sa.exc.MultipleResultsFound):
        record = None

    if record is None:
        # 如果没有找到符合条件的记录，则创建一个新的记录
        record = model(**kwargs)
        # 保存记录到数据库中
        db.session.add(record)

    # 返回查询到的记录
    return record
