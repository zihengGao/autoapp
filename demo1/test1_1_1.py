import random
# list1 = ['佛山', '南宁', '北海', '杭州', '南昌', '厦门', '温州']
# # 随机返回只有一个值的list
# a = random.sample(list1, 1)
#
# # 随机返回只有一个值的list
# # b = random.sample(list1, 3)
# print(a)
# # print(b)
# # 返回list


import time, os
from random import random


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
