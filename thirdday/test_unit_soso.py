from selenium import webdriver
import time
import unittest
import datetime,os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestBingSo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("这是初始化开始测试")
        parent_abspath = os.path.abspath(os.path.dirname(os.getcwd()))
        driver_path =os.path.join(parent_abspath,"driver/chromedriver78")
        cls.driver = webdriver.Chrome(executable_path=driver_path)
        cls.driver.get("https://cn.bing.com/?ensearch=1&FORM=BEHPTB")
        cls.driver.maximize_window()
        assert 'Bing' in cls.driver.title

    @classmethod
    def tearDownClass(cls):
        print("执行完成环境销毁")
        cls.driver.quit()

    def test_soso(self):

        self.driver.find_element_by_id("sb_form_q").send_keys("python")
        self.driver.find_element_by_id("sb_form_go").click()
        self.driver.get_screenshot_as_file(str(datetime.datetime.now())+"_soso.png")
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.title_contains("python"),'页面没加载上')
        assert 'python' in self.driver.page_source


if __name__ == '__main__':
    unittest.main()
