import datetime
import pytz


def format_shanghai_time(t: datetime.datetime):
    tz_cst = pytz.timezone('Asia/Shanghai')
    now_with_tz = t.astimezone(pytz.UTC).replace(tzinfo=pytz.utc).astimezone(tz_cst)
    # 转换成带时区信息的 ISO 8601 格式
    return now_with_tz.strftime('%Y-%m-%dT%H:%M:%S%z')
