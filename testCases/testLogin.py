# sys.path.append('../basepage')
# from basepage.homeBase import *   # 导入基础类
# from page.loginpage import *        # 导入页面类
# from selenium import webdriver
# import time
# import unittest
import sys
sys.path.append('../page')
sys.path.append('../common')
sys.path.append('../data')
from common.ownUnit import MyunitTests  # 导入测试关键所在类
from common.helper import Helper        # 新增Helper类
from common.getImage import getImage          # 导入截图功能
import time
import logging

class TestLogin(MyunitTests,Helper):
    def testlogin(self):
        '''正确的用户名和密码'''
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1),self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(),self.exceptText(1))
        self.makelog('PO-gjs:登陆成功获取信息进行断言')
        getImage(self.driver,'login_success.png')
        self.makelog('PO-gjs:登录成功后获取截图信息')
        self.makelog('PO-gjs:第四条用例执行结束.....')

    def test_user_null(self):
        '''测试密码为空'''
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(2),self.readpassword(2))
        self.makelog('PO-gjs:输入正确的用户名和密码为空')
        self.assertEqual(self.loginpage.get_passwordNullText(),self.exceptText(2))
        self.makelog('PO-gjs:登陆失败获取信息进行断言')
        getImage(self.driver, 'login_passwordNull.png')
        self.makelog('PO-gjs:登录成功后获取截图信息')
        self.makelog('PO-gjs:第一条用例执行结束.....')

    def test_password_null(self):
        '''测试用户名为空'''
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(3),self.readpassword(3))
        self.makelog('PO-gjs:输入正确的密码，用户名为空')
        self.assertEqual(self.loginpage.get_userNullText(),self.exceptText(3))
        self.makelog('PO-gjs:登陆失败获取信息进行断言')
        getImage(self.driver, 'login_userNull.png')
        self.makelog('PO-gjs:登录成功后获取截图信息')
        self.makelog('PO-gjs:第二条用例执行结束.....')

    def test_user_passwd_null(self):
        '''测试用户名/密码为空'''
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(4),self.readpassword(4))
        self.makelog('PO-gjs:不输入用户名和密码')
        self.assertEqual(self.loginpage.get_userNullText(),self.exceptText(4))
        self.makelog('PO-gjs:登陆失败获取信息进行断言')
        getImage(self.driver, 'login_user_password.png')
        self.makelog('PO-gjs:登录成功后获取截图信息')
        self.makelog('PO-gjs:第三条用例执行结束.....')

if __name__ == "__main__":
    MyunitTests.main(verbosity=2)