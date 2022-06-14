import os
import time

def getImage(driver,errorImage):
    '''用例失败截图功能'''
    Rawpath = os.path.join(os.path.dirname(os.path.dirname(__file__)),'Image')
    print(Rawpath)
    NewPicture = Rawpath + '//' + time.strftime('%Y_%y_%d_%H_%M_%S') + '_' + errorImage
    driver.get_screenshot_as_file(NewPicture)
