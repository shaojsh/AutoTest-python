# !/usr/bin/python
# coding:utf-8

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    # 每隔5秒执行一次
    scheduler.add_job(tick, 'interval', seconds=5)
    # 该部分调度是一个独立的线程
    scheduler.start()

    try:
        # 模拟主进程持续运行
        while True:
            time.sleep(2)
            print('sleep')
    except(KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')
