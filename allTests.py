import os,sys,time,unittest
sys.path.append('./common')
sys.path.append('./basepage')
sys.path.append('./page')
from HTMLTestRunner import HTMLTestRunner
from basepage.homeBase import *
from page.loginpage import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def getAllCases():
    '''获取testCases下所有的测试模块'''
    Testsuite = unittest.defaultTestLoader.discover(start_dir=os.path.join(os.path.dirname(__file__),'testCases'),pattern='test*.py')
    return Testsuite

def RunMain():
    '''生成测试报告写入指定Reports目录'''
    fp = open(os.path.join(os.path.dirname(__file__),'report',time.strftime("%Y_%m_%d_%H_%M_%S")+'report.html'),'wb')
    HTMLTestRunner(stream=fp,title='Python+Selenium自动化测试实战',description='基于python语言PO自动化测试').run(getAllCases())

def send_mail(file_new):
    fp = open(file_new,'rb')
    mail_body = fp.read()
    fp.close()
    # 基本信息
    smtpserver = 'smtp.qq.com'
    pwd = 'drrpxuonrtcbbcgb'
    # 定义邮件主题
    msg = MIMEMultipart()
    msg['subject'] = Header(u'Page Object自动化测试报告','utf-8')
    msg['from'] = '928217478@qq.com'
    msg['to'] = '928217478@163.com'
    # html邮件正文
    body = MIMEText(mail_body,"html",'utf-8')
    msg.attach(body)
    att = MIMEText(mail_body,'base64','utf-8')
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename="test_report.html"'
    msg.attach(att)
    # 连接邮箱服务器发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(msg['from'],pwd)
    smtp.sendmail(msg['from'],[msg['to']],msg.as_string())
    print("邮件发送成功")

def new_file(test_dir):
    result_dir = test_dir
    lists = os.listdir(result_dir)   # 列出测试报告列表
    lists.sort()
    file = [x for x in lists if x.endswith('.html')]
    file_path = os.path.join(result_dir,file[-1])
    return file_path

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.realpath(__file__))   # 获取文件所在路径
    test_dir = os.path.join(base_dir,'testCases')           # 获取用例所在目录
    test_report = os.path.join(base_dir,'report')            # 测试报告所在目录
    testlist = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
    now = time.strftime("%Y_%m_%d  %H_%M_%S")
    filename = test_report + '//' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='PageObject自动化测试报告',description='系统环境：macos12.4 浏览器：Chrome 用例执行情况：')
    runner.run(testlist)
    fp.close()
    new_report = new_file(test_report)          # 获取最新报告文件
    send_mail(new_report)                       # 发送最新测试报告