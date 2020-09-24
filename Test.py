import threading

import time


def fun_timer():
    time.sleep(1)
    print('hello')
    global timer
    timer = threading.Timer(1, fun_timer)
    timer.start()


timer = threading.Timer(1, fun_timer)
timer.start()

time.sleep(2)  # 15秒后停止定时器
timer.cancel()
