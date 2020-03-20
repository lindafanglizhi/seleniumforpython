# 页面中有二类：一类是元素，元素的定位，一类是元素的方法
from selenium.webdriver.common.by import By

# 一个大的功能模块写在一个文件中
class MainPageLocators(object):
    search_text = (By.ID, "sb_form_q")
    click_search = (By.ID, "sb_form_go")


class SearchResultPageLocators(object):
    search_result = (By.ID, "b_results")

