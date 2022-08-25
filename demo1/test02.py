
import time, os


# def test_call_number():
#     """number是个列表，在这里加入你想要呼的号码"""
#
#     number = [15239078904,10086, 10010, 12580]
#     # 直接一个for循环，循环号码
#     for num in number:
#         # 使用adb打电话
#         call = os.popen('adb shell am start -a android.intent.action.CALL -d tel:%s' % num)
#         # 这里的sleep时间基本就是你想让通话保持的时间了
#         time.sleep(10)
#         # 挂断电话
#         end = os.popen('adb shell input keyevent 6')  # code6是挂断
#         time.sleep(4)


# def test_call_number():
#     """number是个列表，在这里加入你想要呼的号码"""
#
#     number = [15239078904,10086, 10010, 12580]
#     # 直接一个for循环，循环号码
#     for num in number:
#         # 使用adb打电话
#         call = os.popen('adb shell am start -a android.intent.action.SENDTO -d sms:%s' % num --es sms_body  hello)
#         # 这里的sleep时间基本就是你想让通话保持的时间了
#         time.sleep(10)
#         # 挂断电话
#         end = os.popen('adb shell input keyevent 6')  # code6是挂断
#         time.sleep(4)



# def test_call_number():
#
#     #
#     call = os.popen('adb shell service call phone 2 s16 "10086"')
#     # 这里的sleep时间基本就是你想让通话保持的时间了
#     time.sleep(10)
#     # 挂断电话
#     end = os.popen('adb shell input keyevent 6')  # code6是挂断
#     time.sleep(4)

#
# def test_cm(mobiles,msg):
#     mobiles = [15239078904]
#     msg = "短信内容"



def test_call_msg():
    # mobiles = [15239078904]
    # msgs = "短信内容"
    #遍历表格，读取手机号
    # for num in mobiles,msgs:
    #     os.popen("adb shell am start -a android.intent.action.SENDTO -d sms:{} --es sms_body {hello}" % num)

    os.popen("adb shell am start -a android.intent.action.SENDTO -d sms:15239078904 --es sms_body  hello")



if __name__ == '__main__':
    # test_call_number()
    test_call_msg()