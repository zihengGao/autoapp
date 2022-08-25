import time

from adbutils import adb

d = adb.device()


"""屏幕录像"""
d.start_recording("video/v1.mp4")
time.sleep(5)
d.stop_recording()