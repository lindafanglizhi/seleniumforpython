# 导入selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

# 下载 驱动并且打开浏览器
driver= webdriver.Chrome(executable_path="/Users/lindafang/PycharmProjects/"
                                         "selenium3forpython2020/driver/chromedriver")
# 打开浏览器输入地址
driver.get("http://www.51job.com")
# 在搜索框输入"测试开发" 定位
driver.find_element_by_id("kwdselectid").send_keys("测试开发")
time.sleep(3)
driver.find_element_by_id("work_position_input").click()
driver.find_element_by_id("work_position_click_multiple_selected").click()
driver.find_element_by_id("work_position_click_center_right_list_category_000000_010000").click()
driver.find_element_by_id("work_position_click_bottom_save").click()



# driver.quit()
