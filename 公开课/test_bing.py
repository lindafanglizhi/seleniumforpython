# pip install selenium
# 导入到文件
from selenium import webdriver
import time
# 启动浏览，驱动

driver=webdriver.Chrome("/Users/lindafang/PycharmProjects/seleniumforpython2020/driver/chromedriver")
# 输入网址
driver.get("http://cn.bing.com")
# 在输入框（如何定位）中输入数据
driver.find_element_by_id("sb_form_q").send_keys("python")
# 定位搜索
driver.find_element_by_id("sb_form_go").click()
time.sleep(3)
# 断言python是否在返回的页面中
assert 'python' in driver.page_source
time.sleep(1)
driver.quit()


