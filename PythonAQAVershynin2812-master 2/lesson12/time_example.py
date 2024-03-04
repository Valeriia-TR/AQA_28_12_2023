'''import time


def get_range():
    time.sleep(3)
    return [item for item in range(1000000)]


start = time.time()

get_range()

finish = time.time()

print(f'execution time:{finish-start}')
print(time.time_ns())
t = (2024,2,8,8,3,20,1,35,0)
t = time.mktime(t)
print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))
'''
import datetime
import datetime as dt
'''
print(dt.date(year=2024,month=2,day=8))
print(dt.datetime.now())
print(dt.datetime.utcnow())
today = dt.datetime.now()
print(today.day)
print(today.second)

t1 = dt.date(2024,2,7)
t2 = dt.date(2025,2,14)
t3 = t2-t1
print(t3)
t4 = t2 + t3
print(t4)
t5 = dt.datetime(2024,5,23,14,5,30)
t6 = dt.datetime(2024,5,21,12,50,35)
t7 = t5-t6
print(t7)
t8 = datetime.timedelta(weeks=1, days=3)
t9 = datetime.timedelta(10)
print(t8+t9)
'''
t10 = dt.datetime.now().timestamp()
print(t10)
t11 = dt.datetime(2021,5,17).timestamp()
print(t11)
t12 = t10 + 86800
t13 = dt.datetime.fromtimestamp(t12)
print(t13)

timeformat_string = "%Y-%m-%d %I:%M:%S %p"
t14 = dt.datetime.now().strftime(timeformat_string)
print(t14)
t15 = dt.datetime.strptime(t14, timeformat_string)
print(t15)
a = t15.astimezone()
t15.replace()
t15.replace(tzinfo=datetime.tzinfo(7200, 'a') )



