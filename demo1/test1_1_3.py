

import time
from telnetlib import EC
from selenium.webdriver.support.ui import WebDriverWait
import uiautomator2 as u2


d = u2.connect()

# d.press('home')
"""实现默认上网卡和拨号卡的切换"""
# 启动设置
d.app_start("com.android.browser")
# # 点击输入框
# d(resourceId="android:id/input").click()
# # 输入”自动接听“
# d.send_keys("上网卡")
# #点击搜索结果
# d(resourceId="com.android.settings:id/settings_search_item_name").click()
# #设置上网卡
# d(resourceId="com.android.phone:id/sim1",description="上网卡1").click()
#
# time.sleep(1)
# #设置拨号卡
# d(resourceId="com.android.phone:id/sim1",description="拨号卡1").click()
#
# time.sleep(2)
#
# #停止所有任务
# d.app_stop_all()
# time.sleep(5)
#
# sum=0
# while sum<3:
#     #指定滑动方向和速度
#     # d.swipe(0.5, 0.8, 0.5, 0.4, 0.5)
#     d.swipe_ext('up',scale=0.9)
#     time.sleep(10)
#     sum += 1




# 判断是否有权限弹窗("xpath"="com.android.browser:id/tg")("xpath", "//*[@text='始终允许']")
for i in range(5):
    loc = ("xpath","//*[@resource-id='com.android.browser:id/tg']")
    try:
        e = WebDriverWait(d, 1, 0.5).until(EC.presence_of_element_located(loc))
        e.click()
    except:
        pass


d.press('home')

