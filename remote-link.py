import os
import re
import subprocess

def remote_link():
    try:
        result = os.popen('adb shell ifconfig wlan0')

        context = result.read()
        ip = context.splitlines()[1]
        result.close()
        ip = 'adb connect ' + re.findall(r'Bcast:(.*)  Mask', str(ip))[0]
        subprocess.Popen('adb tcpip 5555', shell=True, stdout=subprocess.PIPE)
        os.system(ip)
        print(os.system('adb devices'))
    except:
        print('移动端远程连接未成功')


if __name__ == "__main__":
    remote_link()
