from datetime import timedelta, datetime


def counts_days():
    d = datetime.now()
    t = timedelta((12 - d.weekday()) % 7)
    return t.days
