import multiprocessing as np
import os
import uiautomator2 as u2
import subprocess
import time


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

def test_xxx(i):  #执行用例
    d = u2.connect(getphonelist()[int(i)])  # d = u2.connect('192.168.1.117')#  uiautomator2 连接手机
    MultiDevice(d)

def MultiDevice(d):  # 功能执行
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
        d.press('home')


def main():#多进程

    for i in range(len(getphonelist())):  #有几个设备起几个进程
        p = np.Process(target=test_xxx, args=(str(i)))
        p.start()

if __name__ == '__main__':
    main()

