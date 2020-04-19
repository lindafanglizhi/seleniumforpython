import unittest
from selenium import webdriver
# from ..pages import pages
import os
import sys
from seconddy.pageobject5.pages import pages
import HtmlTestRunner
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.path.join("/Users/lindafang/PycharmProjects/seleniumforpython2020/driver/chromedriver78"))
        self.driver.get("https://cn.bing.com/")
        self.driver.get_screenshot_as_file("1.png")

    def test_search_in_bing(self):
        main_page = pages.MainPage(self.driver)
        assert 'Bing' in main_page.title_matches()
        main_page.enter_search_text('yaml')
        main_page.click_search_button()
        search_results_page = pages.SearchResultsPage(self.driver)
        assert 'yaml' in search_results_page.results_found()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/lindafang/PycharmProjects/seleniumforpython2020/seconddy/report"))
