from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome("/Users/lindafang/PycharmProjects/seleniumforpython2020/driver/chromedriver")

driver.get("https://www.jd.com")
# qiye=driver.find_element_by_link_text("企业采购")
# lipii=driver.find_element_by_link_text("礼品卡")
# # 悬停
# ActionChains(driver).move_to_element(qiye).move_to_element(lipii).perform()
# lipii.click()
# driver.maximize_window()
# driver.implicitly_wait(10)
# 拖拽
jydq_drag =driver.find_element_by_link_text("家用电器")
ss_drop =driver.find_element_by_id("key")
# ActionChains(driver).drag_and_drop(jydq_drag,ss_drop).perform()
ActionChains(driver).click_and_hold(jydq_drag)\
    .move_to_element(ss_drop)\
    .release(ss_drop)\
    .perform()

time.sleep(2)
# driver.find_element_by_class_name("button").click()



