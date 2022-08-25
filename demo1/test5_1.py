import time

import uiautomator2 as u2


d = u2.connect()

# d.press('home')
"""实现默认上网卡和拨号卡的切换"""
# 启动设置
d.app_start("com.android.settings")
# 点击输入框
d(resourceId="android:id/input").click()
# 输入”自动接听“
d.send_keys("上网卡")
#点击搜索结果
d(resourceId="com.android.settings:id/settings_search_item_name").click()
#设置上网卡
d(resourceId="com.android.phone:id/sim1",description="上网卡1").click()

time.sleep(1)
#设置拨号卡
d(resourceId="com.android.phone:id/sim1",description="拨号卡1").click()

time.sleep(2)

#停止所有任务
d.app_stop_all()
time.sleep(3)


d.press('home')

