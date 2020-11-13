# cmd = schtasks /create /tn start /tr C:\Users\shaojunshuai\PycharmProjects\AutoTest-python\Auto_Test\start.py /sc daily /st 18:00
# 每天执行定时任务py   开机  控制面板  维护
# 1.wins+R
# 2. 执行命令 cmd
# 3. schtasks 删除任务：schtasks /Delete /TN start /F
import os


# 调用后会自动关机
def shout_dowm():
    os.system('shutdown -s -f -t 10')


# 调用后自动开机
def start_up():
    pass


if __name__ == "__main__":
    shout_dowm()