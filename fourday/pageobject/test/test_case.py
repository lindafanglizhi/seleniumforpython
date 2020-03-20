from selenium import webdriver
import time
import unittest
import datetime,os
from ..pages import pages


class TestBingSo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("这是初始化开始测试")
        parent_abspath = os.path.abspath(os.path.dirname(os.getcwd()))
        driver_path =os.path.join(parent_abspath,"driver/chromedriver78")
        cls.driver = webdriver.Chrome(executable_path=driver_path)
        cls.driver.get("https://cn.bing.com/?ensearch=1&FORM=BEHPTB")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait()


    @classmethod
    def tearDownClass(cls):
        print("执行完成环境销毁")
        cls.driver.quit()

    def test_soso(self):
        main_page =pages.MainPage(self.driver)
        assert 'Bing' in main_page.title_matches()
        main_page.enter_search_text("python")
        main_page.click_search_button()
        search_result_page = pages.SearchResultPage(self.driver)
        assert 'Python' in search_result_page.results_found()
        search_result_page.save_pic(str(datetime.datetime.now())+"_soso.png")


if __name__ == '__main__':
    unittest.main()
