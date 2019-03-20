import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image

size = (164, 164)

class PythonOrgSearch(unittest.TestCase, awbNo):

    awbNo = input('请输入运单号：')


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://mydhlplus.dhl.com/cn/zh/tracking.html#/results?id={}".format(awbNo))
        driver.maximize_window()
        # self.assertIn("EShip", driver.title)
        # driver.find_element_by_class_name("btn").click()
        # elem = driver.find_element_by_id('email')
        # elem.send_keys('13802728727')
        # elem = driver.find_element_by_id('pw')
        # elem.send_keys('Lyt722726')
        # driver.save_screenshot('1.png')
        # time.sleep(1)
        # elem.submit()
        # time.sleep(2)
        # im = Image.open('1.png')
        # im_grey = im.convert('L')
        # im_grey.save(r'C:\Users\Administrator\Desktop\2.png')
        # print(im.format, im.size, im.mode)
        # print(driver.get_cookies())

    def tearDown(self):
        time.sleep(1000)
        self.driver.close()

if __name__ == '__main__':
    while True:
        try:
            if PythonOrgSearch.awbNo.isdigit():
                unittest.main()
            else:
                pass
        except:
            pass




