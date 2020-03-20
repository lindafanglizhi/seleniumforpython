from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

path='/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver78'


driver = webdriver.Chrome(executable_path=path)

driver.get("http://172.16.166.129:81/zentao/user-login.html")
driver.find_element_by_id("account").send_keys("admin")
driver.find_element(By.NAME, 'password').send_keys('123456.')
driver.find_element_by_id("submit").click()

wait = WebDriverWait(driver,10)
wait.until(EC.title_is("我的地盘 - 禅道"))
driver.maximize_window()
driver.find_element_by_link_text("组织").click()
driver.find_element_by_link_text("用户").click()

print(driver.find_elements_by_class_name("icon-trash")[6].is_enabled())
# origial_window=driver.current_window_handle
# print(driver.window_handles)
# for window_handle in driver.window_handles:
#     if(window_handle != origial_window):
#         driver.switch_to.window(window_handle)
#         break

# alert = Alert(driver)
# alert.send_keys("123456.")
# alert.accept()
# alert =driver.switch_to.alert
# alert.send_keys("123456.")
# alert.accept()

driver.get("http://172.16.166.129:81/zentao/user-delete-8.html")
driver.find_element_by_id("verifyPassword").send_keys("123456.")
driver.find_element_by_id("submit").click()
