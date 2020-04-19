from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

path='/Users/lindafang/PycharmProjects/seleniumforpython2020/driver/chromedriver78'

# 静默执行
chrome_option =webdriver.ChromeOptions()
chrome_option.add_argument("--headless")
driver = webdriver.Chrome(executable_path=path,options=chrome_option)



driver.get("http://172.16.166.129:81/zentao/user-login.html")
driver.find_element_by_id("account").send_keys("admin")
driver.find_element(By.NAME, 'password').send_keys('123456.')
driver.find_element_by_id("submit").click()

wait = WebDriverWait(driver,10)
wait.until(EC.title_is("我的地盘 - 禅道"))
driver.maximize_window()

driver.find_element_by_link_text("组织").click()
driver.find_element_by_link_text("用户").click()
driver.find_element_by_link_text("添加用户").click()

driver.find_element_by_class_name("chosen-single").click()
driver.find_elements_by_class_name("active-result")[1].click()

driver.find_element_by_id("account").send_keys("linda3")
driver.find_element_by_id("password1").send_keys("123456.")
driver.find_element_by_id("password2").send_keys("123456.")
driver.find_element_by_id("realname").send_keys("lindafang3")
driver.find_element_by_id("role").click()
# select 分层定位
role = driver.find_element_by_id("role")
# Select(role).select_by_visible_text("测试")
Select(role).select_by_index(2)
# Select(role).select_by_value("qa")
print(driver.find_element_by_id("submit").is_displayed())
driver.execute_script("window.scrollBy(0,2000)")
# driver.save_screenshot()
print(driver.find_element_by_id("submit").is_enabled())
driver.find_element_by_id("genderf").click()
driver.find_element_by_id("verifyPassword").send_keys("123456.")

driver.find_element_by_id("submit").click()
time.sleep(2)
assert 'lindafang388' in driver.page_source
# assert

driver.quit()



