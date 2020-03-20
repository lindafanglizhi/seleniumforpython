from selenium import webdriver
import unittest
import datetime,os,sys
from ..pages import pages
from util.get_path import get_par_path
# 1、加导入
from ddt import ddt,file_data

# 2、在类上加@ddt
@ddt
class TestBingSo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("这是初始化开始测试")
        # parent_abspath = os.path.abspath(os.path.dirname(os.getcwd()))
        parent_abspath=get_par_path()
        driver_path =os.path.join(parent_abspath,"driver/chromedriver78")
        sys.path.append(driver_path)
        cls.driver = webdriver.Chrome(executable_path=driver_path)
        cls.driver.get("https://cn.bing.com/?ensearch=1&FORM=BEHPTB")
        cls.driver.maximize_window()


    @classmethod
    def tearDownClass(cls):
        print("执行完成环境销毁")
        cls.driver.quit()

    # 3、在测试方法上加@file_data,通过yaml类型的文件导入数据
    @file_data("test_data_soso.yml")
    def test_soso(self,sosovalue):

        main_page =pages.MainPage(self.driver)
        assert 'Bing' in main_page.title_matches()
        # 4、变量值sosovalue在输入搜索值的地方替换
        main_page.enter_search_text(sosovalue)
        main_page.click_search_button()
        search_result_page = pages.SearchResultPage(self.driver)
        # 5、如果断言相同 ，修改断言为变量
        assert sosovalue in search_result_page.results_found()
        search_result_page.save_pic(str(datetime.datetime.now())+"_soso.png")


if __name__ == '__main__':
    unittest.main()
