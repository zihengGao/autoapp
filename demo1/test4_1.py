
import uiautomator2 as u2

aa = ("f20129e5","de07ac7e")
for bb in aa:
    d = u2.connect(bb)

    d.press('home')

    """自动打电话"""
    # 启动设置
    d.app_start("com.android.settings")
    # 点击输入框
    d(resourceId="android:id/input").click()
    # 输入”自动接听“
    d.send_keys("自动接听")
    #点击搜索结果
    d(resourceId="com.android.settings:id/settings_search_item_name").click()
    #开启自动接听
    d(resourceId="android:id/widget_frame").click()

    d.press('home')

