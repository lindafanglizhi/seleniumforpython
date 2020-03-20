# 与定位的类名匹配
# 公共的方法提取出来
from .locators import MainPageLocators,SearchResultPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    def save_pic(self, filepath):
        self.driver.get_screenshot_as_file(filepath)


class MainPage(BasePage):
    def enter_search_text(self, text):
        # lambda是匿名函数 *是传参的格式是元组类型需要解包
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*MainPageLocators.search_text)
        )
        element = self.driver.find_element(*MainPageLocators.search_text)
        element.clear()
        element.send_keys(text)

    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocators.click_search)
        element.click()

    def title_matches(self):

        return self.driver.title


class SearchResultPage(BasePage):
    def results_found(self):
        # 等待元素加载出来后返回元素文本信息
        WebDriverWait(self.driver, 10).\
            until(EC.presence_of_element_located(SearchResultPageLocators.search_result))
        # print(self.driver.find_element(*SearchResultPageLocators.search_result).text)
        return self.driver.find_element(*SearchResultPageLocators.search_result).text
