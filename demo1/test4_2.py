
import sys
import uiautomator2  as u2
from time import sleep
import os
import subprocess
import threading
import time

def MultiDevice(d):  # 功能执行

    d.set_fastinput_ime(True)  # 输入法设置

    d.press('home')

    """自动打电话"""
    # 启动设置
    d.app_start("com.android.settings")
    # 点击输入框
    d(resourceId="android:id/input").click()
    # 输入”自动接听“
    d.send_keys("自动接听")
    # 点击搜索结果
    d(resourceId="com.android.settings:id/settings_search_item_name").click()
    # 开启自动接听
    d(resourceId="android:id/widget_frame").click()

    d.press('home')

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
    MultiDevice(d)


def start():
        threads = []
        for i in range(len(getphonelist())):
            threads.append(threading.Thread(target=test_xxx(getphonelist()[i]),args=()))
        for t in threads:
            time.sleep(0.3)
            t.start()
        for t in threads:
            t.join()

if __name__ == '__main__':
    start()
