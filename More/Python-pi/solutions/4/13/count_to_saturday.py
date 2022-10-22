import datetime


def count_days_to_saturday() -> int:
    """
    Count the remaining whole days to the next saturday.
    :return: count of the days
    """
    today = datetime.date.today()
    delta = datetime.timedelta(days=1)
    d = today + delta
    n = 0
    while d.weekday() != 5:
        d += delta
        n += 1
    return n


if __name__ == '__main__':
    n = count_days_to_saturday()
    print(f'Remaining days to Saturday: {n}')
