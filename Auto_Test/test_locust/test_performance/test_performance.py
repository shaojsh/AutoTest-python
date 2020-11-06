import os
from locust import HttpUser, task, between, SequentialTaskSet


# 定义一个任务类，这个类名称自己随便定义，
# 类继承SequentialTaskSet 或 TaskSet类，所以要从locust中，引入SequentialTaskSet或TaskSet
# 当类里面的任务请求有先后顺序时，
# 继承SequentialTaskSet类， 没有先后顺序，可以使用继承TaskSet类

class MyTaskCase(SequentialTaskSet):
    # 初始化方法，相当于 setup
    def on_start(self):
        pass

    @task(1)  # 装饰器，说明下面是一个任务
    def login_(self):
        url = '/v1/account/login'  # 接口请求的URL地址
        headers = {
            "Host": "10.10.128.152:10000",
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */*",
            "Origin": "http://10.10.128.152:10052",
            "appId": "chengtay-zcd",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
            "Referer": "http://10.10.128.152:10052/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9"

        }
        json = {
            "userName": "17082200006",
            "password": "MTIzNDU2"
        }
        with self.client.post(url,
                              catch_response=True, json=json, headers=headers) as rsp:
            # 提取响应json 中的信息，定义为 类变量
            # self.token = rsp.json()['token']
            if rsp.status_code == 200:
                rsp.success()
            else:
                rsp.failure('login_ 接口失败！')

    # 结束方法， 相当于teardown
    def on_stop(self):
        pass


# 定义一个运行类 继承HttpUser类， 所以要从locust中引入 HttpUser类
class UserRun(HttpUser):
    host = 'http://10.10.128.152:10000'
    tasks = [MyTaskCase]
    # 设置运行过程中间隔时间 需要从locust中 引入 between
    wait_time = between(0.1, 3)


if __name__ == "__main__":
    path = os.getcwd() + '\\test_performance.py'
    os.system("locust -f " + path)
