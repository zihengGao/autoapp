import os


def get_deviceid():
    device = os.popen("adb devices").readlines()
    device_id=device[1]
    print (device_id.split()[0])


get_deviceid()