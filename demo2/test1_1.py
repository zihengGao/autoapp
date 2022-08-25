from adbutils import adb

for d in adb.device_list():
    print(d.serial) # print device serial

d = adb.device(serial="33ff22xx")

# or
d = adb.device(transport_id=24) # transport_id can be found in: adb devices -l

# You do not need to offer serial if only one device connected
# RuntimeError will be raised if multi device connected
d = adb.device()