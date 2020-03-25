import datetime

print(datetime.datetime(2019, 12, 23, 4, 50, 58, 854))

print(datetime.datetime.today())
print(datetime.datetime.now())

date = datetime.datetime.today()
print(date.year)
print(date.time())

print(datetime.date(2019, 12, 23))

b1 = datetime.timedelta(days=50)
b2 = datetime.timedelta(days=100)

print(b1-b2)