import time
import datetime

t0 = datetime.datetime.utcnow()
time.sleep(1)
t1 = datetime.datetime.utcnow()

time_format = '%Y-%m-%dT%H:%M:%S.%fZ'
print(t0.strftime(time_format), end='')

print(t1.strftime(time_format), end='')

