from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# 打开浏览器
driver = webdriver.Chrome(executable_path="/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver78")
# 打开进入具体网址
driver.get("https://cn.bing.com/?ensearch=1&FORM=BEHPTB")
driver.maximize_window()
# 通过id定位搜索框，在里面输入"selenium"
driver.find_element_by_id("sb_form_q").send_keys("python"+Keys.RETURN)
# 通过id定位提交搜索，操作是点击
time.sleep(2)
driver.find_element_by_id("sb_form_go").click()
time.sleep(5)

# assert 'pytest' in driver.title
driver.find_element_by_link_text("VIDEOS").click()
time.sleep(2)
print(driver.title)

# 断言搜索内容在title中

# 关闭浏览器
driver.quit()