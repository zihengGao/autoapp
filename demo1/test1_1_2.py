
import random
import time, os

def test_call_number():
    """number是个列表，在这里加入你想要呼的号码"""

    number = [15239078904,10086, 10010, 12580]
    aa = random.sample(number, 1)

    # 直接一个for循环，循环号码
    for num in aa:
        # 使用adb打电话
        call = os.popen('adb shell am start -a android.intent.action.CALL -d tel:%s' % aa)
        # 这里的sleep时间基本就是你想让通话保持的时间了
        time.sleep(10)
        # 挂断电话
        end = os.popen('adb shell input keyevent 6')  # code6是挂断
        time.sleep(4)


if __name__ == '__main__':
    test_call_number()
