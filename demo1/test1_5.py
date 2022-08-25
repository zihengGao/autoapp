import os
import time

import uiautomator2 as u2

# d = u2.connect()
# lis =d.serial
# for a in d.serial():
#     print(a)


def get_deviceid():
    device = os.popen("adb devices").readlines()
    device_id = device[1]

    sz = device_id.split()[0]

    number = [15239078904, 10086, 10010, 12580]
    for a in sz:
        d = u2.connect(a)

        # 直接一个for循环，循环号码
        for num in number:
            # 使用adb打电话
            call = os.popen('adb shell am start -a android.intent.action.CALL -d tel:%s' % num)
            # 这里的sleep时间基本就是你想让通话保持的时间了
            time.sleep(10)
            # 挂断电话
            end = os.popen('adb shell input keyevent 6')  # code6是挂断
            time.sleep(4)


get_deviceid()