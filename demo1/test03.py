import time

import uiautomator2 as u2

d = u2.connect()

#  停止所有应用程序
# d.app_stop_all()
# time.sleep(5)

# 指定package name启动
d.app_start("com.ss.android.ugc.aweme",use_monkey=True)#"com.ss.android.ugc.aweme.splash.SplashActivity"
# d.implicitly_wait(5)

time.sleep(5)

sum=0
while sum<2:
    #指定滑动方向和速度
    # d.swipe(0.5, 0.8, 0.5, 0.4, 0.5)
    d.swipe_ext('up',scale=0.9)
    time.sleep(10)
    sum += 1

# 执行强制停止
d.app_stop("com.ss.android.ugc.aweme")

d.press('home')




