import sys
sys.path.append('../basepage')
from basepage.homeBase import HomePage
from selenium.webdriver.common.by import By
import time

# 定义LoginPage页面类并继承HomePage基础类，分别定义登录页面上需要用到的元素。
class LoginPage(HomePage):
    # 定位器
    # 用户名
    username_loc = (By.ID,'mobilePhone')
    # 密码
    password_loc = (By.ID,'password')
    # "登录"按钮
    loginBtn_loc = (By.ID,'loginBtn')
    # 退出连接
    logoutBtn_loc = (By.CSS_SELECTOR,'#loginBtn')
    # 用户名为空
    userNull_loc = (By.CSS_SELECTOR,'#error > span')
    # 密码为空
    passWordNull_loc = (By.CSS_SELECTOR,'#error > span')

    # 打开登录页面
    def openLoginPage(self):
        self.driver.get(self.url)
        self.driver.refresh()
        self.driver.maximize_window()
        time.sleep(3)

    # 输入用户名
    def input_userName(self,userName):
        self.find_element(*self.username_loc).send_keys(userName)

    # 输入密码
    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    # 点击登录按钮
    def click_loginBtn(self):
        self.find_element(*self.loginBtn_loc).click()

    # 获取登录成功后的提示信息
    def get_assertText(self):
        return self.find_element(*self.logoutBtn_loc).text

    # 用户名为空的提示
    def get_userNullText(self):
        return self.find_element(*self.userNull_loc).text

    # 密码为空的提示
    def get_passwordNullText(self):
        return self.find_element(*self.passWordNull_loc).text

    # 组装成登录流程
    def login_gjs_pro(self,username,password):
        self.input_userName(username)
        self.input_password(password)
        self.click_loginBtn()