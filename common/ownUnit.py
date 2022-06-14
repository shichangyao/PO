import sys
sys.path.append('../basepage')
sys.path.append('../page')
from basepage.homeBase import *
from page.loginpage import *
from selenium import webdriver
import unittest
import time

class MyunitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'https://qhfles.gjfax.com/toLogin'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 实例化一个loginpage对象
        self.loginpage = LoginPage(self.url,self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

'''将用例层中测试固件SetUp()和tearDown()的公共部分单独定义成一个测试类MyunitTests()，方便其他用例层调用，这样设计也比较合理'''