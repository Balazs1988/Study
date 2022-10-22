import datetime


def count_weekends(year=None) -> int:
    """
    Count the weekends in the given year.
    :param year: the considered year (default the current one)
    :return: count of weekend days
    """
    if year is None:
        now = datetime.datetime.now()
        year = now.year
    if year < 1990 or year > 2100:
        raise ValueError('The year is out of the range!')
    d = datetime.date(year, 1, 1)
    end_date = datetime.date(year + 1, 1, 1)
    delta = datetime.timedelta(days=1)
    n_weekends = 0
    while d < end_date:
        if d.weekday() in [5, 6]:
            n_weekends += 1
        d += delta
    return n_weekends


if __name__ == '__main__':
    year = 2022
    n_weekends = count_weekends(year)
    print(f'Number of weekends in {year}: {n_weekends}')
