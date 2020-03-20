from .locators import MainPageLocators,SearchResultPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def save_pic(self,filepath):
        self.driver.save_screenshot(filepath)


class MainPage(BasePage):

    def title_matches(self):
        return self.driver.title

    def enter_search_text(self, text):
        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*MainPageLocators.search_text))
        element = self.driver.find_element(*MainPageLocators.search_text)
        element.clear()
        element.send_keys(text)

    def click_search_button(self):
        ele = self.driver.find_element(*MainPageLocators.click_search)
        ele.click()


class SearchResultsPage(BasePage):
    def results_found(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(SearchResultPageLocators.search_result))
        return self.driver.find_element(*SearchResultPageLocators.search_result).text
