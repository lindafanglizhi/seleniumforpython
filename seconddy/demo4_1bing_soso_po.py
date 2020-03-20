from selenium import webdriver
import unittest
import time
import datetime


class bing_soso_po(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome(executable_path="/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver78")
        cls.browser.get('https://cn.bing.com/')
        cls.browser.maximize_window()
        cls.browser.implicitly_wait(10)
        assert '微软 Bing 搜索 ' in cls.browser.title

    @classmethod
    def tearDownClass(cls):
        if(cls.browser!=None):
            print("环境销毁")
            print("运行时间总计:"+str(datetime.datetime.now()))
            cls.browser.quit()

    def test_soso(self):
        elem = self.browser.find_element_by_id('sb_form_q')
        elem.click()
        elem.clear()
        elem.send_keys('seleniumhq')
        elec = self.browser.find_element_by_id('sb_form_go')
        elec.click()
        self.browser.get_screenshot_as_file(str(datetime.datetime.now())+"_sousuo.png")
        time.sleep(3)
        assert 'selenium' in self.browser.page_source


if __name__ == '__main__':
    unittest.main()


