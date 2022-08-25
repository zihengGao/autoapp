import os
import subprocess
import time
import uiautomator2 as u2


# def get_deviceid():
#     device = os.popen("adb devices").readlines()
#     device_id = device[1]
#     return device_id
    # print (device_id.split()[0])


def test_call_number(d):
    """number是个列表，在这里加入你想要呼的号码"""

    number = [15239078904,10086, 10010, 12580]
    # 直接一个for循环，循环号码
    for num in number:
        # 使用adb打电话
        call = os.popen('adb shell am start -a android.intent.action.CALL -d tel:%s' % num)
        # 这里的sleep时间基本就是你想让通话保持的时间了
        time.sleep(10)
        # 挂断电话
        end = os.popen('adb shell input keyevent 6')  # code6是挂断
        time.sleep(4)



def getphonelist():  # 获取手机设备
    cmd = r'adb devices'  # % apk_file
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    pr.wait()  # 不会马上返回输出的命令，需要等待
    out = pr.stdout.readlines()  # out = pr.stdout.read().decode("UTF-8")
    devices = []
    for i in (out)[1:-1]:
        device = str(i).split("\\")[0].split("'")[-1]
        devices.append(device)
    return devices  # 手机设备列表


def test_xxx(i):
    d = u2.connect(i)  # d = u2.connect('192.168.1.117')#  uiautomator2 连接手机
    test_call_number(d)