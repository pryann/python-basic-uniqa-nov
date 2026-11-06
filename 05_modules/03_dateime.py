from datetime import date, time, datetime

d = date(2020, 10, 10)
print(d)
t = time(11, 11, 11, 123456)
print(t)

print(datetime.combine(d, t))

now = datetime.now()
print(now)
print(now.strftime("%Y. %B %d %H:%M:%S"))
print(now.isoformat())
print(date(2021, 10, 10) - date(2020, 1, 1))
