from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

path='/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver78'
driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()

driver.get("http://172.16.166.129:81/zentao/user-login.html")
driver.find_element_by_id("account").clear()
driver.find_element_by_id("account").send_keys("admin")
driver.find_element(By.NAME, 'password').send_keys('123456.')
driver.find_element_by_id("submit").click()

wait = WebDriverWait(driver,10)
wait.until(EC.title_is("我的地盘 - 禅道"))
driver.maximize_window()

driver.find_element_by_link_text("组织").click()
driver.find_element_by_link_text("用户").click()
print(driver.find_elements_by_class_name("icon-trash")[4].is_enabled())
# is_selected /is_displayed
# 使用窗口切换，是不是多窗口
# print(driver.window_handles)
# 是不是弹出框alert,不是弹出框
# alert =Alert(driver)
# alert.send_keys("123456.")
# alert.accept()
# alert.dismiss()
# alert = driver.switch_to.alert
# alert.send_keys("123456.")
# alert.accept()
# driver.get("http://172.16.166.129:81/zentao/user-delete-6.html")
# driver.find_element_by_id("verifyPassword").send_keys("123456.")
# driver.find_element_by_id("submit").click()

# driver.quit()
