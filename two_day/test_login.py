from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path='/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver78'
driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()


driver.get("http://172.16.166.129:81/zentao/user-login.html")

print(driver.title)
# 获得当前地址，一般可用于断言是否达到正确的页面
print(driver.current_url)
print(driver.name)

# 获得当前的窗口句柄，可以进一步进行窗口的切换
print(driver.current_window_handle)
# print(driver.window_handles)
# 切换窗口（窗口名）
driver.switch_to.window(driver.current_window_handle)
# print(driver.current_window_handle)
# 切换回默认窗口
driver.switch_to.default_content()
# print(driver.current_window_handle)

driver.find_element_by_id("account").send_keys("admin")
driver.find_element(By.NAME, 'password').send_keys('123456.')
driver.find_element_by_id("submit").click()
time.sleep(2)
# 截图
driver.save_screenshot("1.png")
# 返回页面源码，用于获得页面看不见的，或一闪就没的。
print(driver.page_source)
# 设置窗口的位置
driver.set_window_position(100,200,'current')
time.sleep(2)
print(driver.title)
# driver.back()
# driver.forward()
# driver.refresh()

#
#
driver.close()
driver.quit()

