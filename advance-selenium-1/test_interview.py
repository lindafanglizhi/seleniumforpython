from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="chromedriver")
# driver_firefox = webdriver.Firefox(executable_path='geckodirver')
# driver_ie =webdriver.Ie("")

driver.find_element_by_id("定位元素的id").send_keys("输入的文本")
driver.find_element(By.ID,'wd').send_keys("输入的文本")
driver.find_element_by_id("定位").is_enabled()
driver.find_element_by_id("定位").is_selected()
driver.find_element_by_id("定位").is_displayed()
txt =driver.find_element_by_id("定位").text
driver.find_element_by_link_text("用户").click()
driver.find_element_by_partial_link_text("用").click()
assert '百度搜索title'==driver.title
driver.find_element_by_id("定位").value_of_css_property("font-size")
driver.find_element_by_id("定位元素id").get_attribute("class")
driver.find_element_by_id("").get_property("text_length")
text=driver.find_element_by_id("").text
