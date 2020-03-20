from selenium.webdriver.common.by import By


class MainPageLocators(object):
    search_text = (By.ID, "sb_form_q")
    click_search = (By.ID, "sb_form_go")


class SearchResultPageLocators(object):
    search_result = (By.ID, 'b_results')
