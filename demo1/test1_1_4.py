import uiautomator2 as u2


"""监控app打开时的弹窗，实现跳过对应的弹窗"""

d = u2.connect()

# 启动设置
d.app_start("com.android.browser")

# 设置监控元素
d.watcher.when('关闭').click()
d.watcher.when('一键登录').click()
d.watcher.when('获取验证码').click()
d.watcher.when('始终允许').click()
d.watcher.when('同意').click()
d.watcher.when('仅在使用中允许').click()

# 注册名为ANR的监控，当出现ANR和Force Close时，点击Force Close
d.watcher("ANR").when(xpath="ANR").when("Force Close").click()

# 其他回调例子
# d.watcher.when("抢红包").press("back")
# d.watcher.when("//*[@text = 'Out of memory']").call(lambda d: d.shell('am force-stop com.im.qq'))

# 回调说明,两种调用方法
# def click_callback(d: u2.Device):
#     d.xpath("同意").click() # 在回调中调用不会再次触发watcher
# click_callback(d)

d.xpath("同意").click() # 使用d.xpath检查元素的时候，会触发watcher（目前最多触发5次


# # 移除ANR的监控
# d.watcher.remove("ANR")
#
# # 移除所有的监控
# d.watcher.remove()
#
# # 开始后台监控
# d.watcher.start()
# d.watcher.start(2.0) # 默认监控间隔2.0s
#
#
# # 强制运行所有监控
# d.watcher.run()
#
# # 停止监控
# d.watcher.stop()

# 停止并移除所有的监控，常用于初始化
d.watcher.res