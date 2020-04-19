from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# 打开浏览器
driver = webdriver.Chrome(executable_path="/Users/lindafang/PycharmProjects/seleniumforpython2020/driver/chromedriver78")
# 打开进入具体网址
driver.get("https://www.baidu.com/")
driver.maximize_window()
print(driver.find_element_by_tag_name("body").get_attribute("link"))

driver.find_element_by_id("kw").send_keys("python")

driver.find_element_by_id("su").click()

driver.quit()