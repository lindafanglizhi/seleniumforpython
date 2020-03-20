from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path='/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver78'
driver = webdriver.Chrome(executable_path=path)

# 隐式等待，全局10秒
driver.implicitly_wait(10)
driver.get("https://cn.bing.com/")

elem=driver.find_element_by_id("sb_form_q")
elem.send_keys("seleniumhq"+Keys.RETURN)
assert 'selenium' in driver.page_source

# 显示等待10秒
wait = WebDriverWait(driver,10)
original_window=driver.current_window_handle
assert len(driver.window_handles)==1
driver.find_element_by_partial_link_text("selenium中文网").click()
# 等待走到切换到第二个窗口
wait.until(EC.number_of_windows_to_be(2),'超时返回的信息，没有第2个窗口呀')

# 切换到不是原来的那个窗口
for window_handle in driver.window_handles:
    print(window_handle)
    if window_handle!=original_window:
        driver.switch_to.window(window_handle)
        break

# 等待新窗口的title包含""
wait.until(EC.title_contains("selenium中文网"))
print(driver.title)
driver.close()
driver.quit()






