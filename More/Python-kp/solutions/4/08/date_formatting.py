import datetime as dt

today = dt.datetime.now()
print(f'{today:%d, %B of %Y}')
print(f'{today:%Y_%m_%d}')
print(f'{today:%m%d%Y}')
print(f'{today:%Y. %m. %d.}')
