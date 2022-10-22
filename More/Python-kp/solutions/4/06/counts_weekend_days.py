from datetime import date, timedelta


def counts_weekend_days(year=date.today().year):
    if year not in range(1990, 2101):
        print('Please type a year between 1990 and 2100!')
    else:
        date_from = date(year, 1, 1)
        date_to = date(year, 12, 31)
        all_days = (date_from + timedelta(x + 1) for x in range((date_to - date_from).days))
        weekdays = sum(1 for day in all_days if day.weekday() > 4)
        print('Number of weekend days is:', weekdays)
