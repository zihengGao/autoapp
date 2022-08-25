import subprocess
import uiautomator2 as u2


def getphoneidlist():
    """获取所有手机设备序列号的列表"""


    cmd = r'adb devices'
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    pr.wait()  # 不会马上返回输出的命令，需要等待
    out = pr.stdout.readlines()  # out = pr.stdout.read().decode("UTF-8")
    devices = []
    for i in (out)[1:-1]:
        device = str(i).split("\\")[0].split("'")[-1]
        devices.append(device)
    return devices
    #遍历拿到的序列id，并打印
    # for aa in devices:
    #     return aa
        # print(aa)


def test_id(i):
    d = u2.connect(i)  # d = u2.connect('192.168.1.117')#  uiautomator2 连接手机
    test_cases(d)


def test_cases(d):  #用例编写
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



# getphoneidlist()
# test_id()
if __name__ == '__main__':
    test_cases()
    test_id()