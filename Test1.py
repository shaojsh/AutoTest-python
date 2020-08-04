import win32com.client as win32
import datetime, os

project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
# addressee = 'test01@qq.com' + ';' + 'test02@jd.com'  # 收件人邮箱列表
#  cc = 'test02@163.com' + ';' + 'test03@alibaba.com'  # 抄送人邮件列表
addressee = 'shaojunshuai@chengtay.com'  # 收件人邮箱列表
cc = '2319898127@qq.com'
mail_path = project_path+'Auto_Test\\report\\reporthtml\\index.html'


class send_email():
    def outlook(self):
        olook = win32.Dispatch("outlook.Application")  # 固定写法
        mail = olook.CreateItem(win32.constants.olMailItem)  # 固定写法
        mail.To = addressee  # 收件人
        # mail.CC = cc  # 抄送人
        # mail.Recipients.Add(addressee)
        mail.Subject = str(datetime.datetime.now())[0:19] + 'XXX反馈报告'  # 邮件主题
        mail.Attachments.Add(mail_path, 1, 1, "myFile")
        read = open(mail_path, encoding='utf-8')  # 打开需要发送的测试报告附件文件
        content = read.read()  # 读取测试报告文件中的内容
        read.close()
        mail.Body = content  # 将从报告中读取的内容，作为邮件正文中的内容
        mail.Send()  # 发送


if __name__ == '__main__':
    send_email().outlook()
    print("send email ok!!!!!!!!!!")
