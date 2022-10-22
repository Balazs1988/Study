import datetime


if __name__ == '__main__':
    d = datetime.date(2020, 5, 10)
    print(d.strftime('%d, %b of %Y'))
    print(d.strftime('%Y_%m_%d'))
    print(d.strftime('%m%d%Y'))
    print(f'{d.year}. {d.month}. {d.day}')
    d_1 = datetime.datetime.strptime('10, May of 2020', '%d, %b of %Y')
    d_2 = datetime.datetime.strptime('2020_05_10', '%Y_%m_%d')
    d_3 = datetime.datetime.strptime('05102020', '%m%d%Y')
    text = '2020. 5. 10.'
    splits = text.split(' ')
    year = int(splits[0][:-1])
    month = int(splits[1][:-1])
    day = int(splits[2][:-1])
    d_4 = datetime.date(year, month, day)
