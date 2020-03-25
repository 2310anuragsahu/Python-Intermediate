import time

epoch_sec = time.time()
print(epoch_sec)

current_date_time = time.ctime(epoch_sec)
print(current_date_time)

local_time = time.localtime(epoch_sec)
print(local_time)

gm_time = time.gmtime(epoch_sec)
print(gm_time)

mk_time = time.mktime(local_time)
print(mk_time)

asc_time = time.asctime(local_time)
print(asc_time)

help(time.strftime)
date = time.strftime("%m/%Y/%d %a %A %c")
print(date)

help(time.strptime)