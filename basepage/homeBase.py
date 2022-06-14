from selenium.webdriver.support.ui import WebDriverWait         # 显示等待
from selenium.webdriver.support import expected_conditions as EC    # 判断元素是否被定位到

class HomePage(object):             # 页面的基础类
    def __init__(self,url,driver):      # 定义驱动和地址
        self.url = url
        self.driver = driver

    def find_element(self,*loc):    # 封装元素定位方式
        try:
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print( "元素定位在页面中无法找到！")