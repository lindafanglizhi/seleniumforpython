from selenium import webdriver
import time

# 本节课熟悉浏览器相关操作
# 常用几种元素定位，包含返回结果是数组的写法
browser = webdriver.Chrome(executable_path="/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver78")
browser.get("http://172.16.166.129/zentao/")
# browser.maximize_window()
# print(browser.current_url)
# print(browser.page_source)
# print(browser.name)
# print(browser.current_window_handle)
# # 所有句柄
# print(browser.window_handles)

browser.find_element_by_id("account").send_keys("admin")
# browser.find_element_by_name("account").send_keys("admin")
# browser.find_element_by_css_selector("#account").send_keys("admin")
# browser.find_elements_by_class_name("form-control")[0].send_keys("admin")
# browser.find_element_by_xpath("//*[@id='account']").send_keys("admin")
browser.find_element_by_name("password").send_keys("123456.")
browser.find_element_by_id("submit").click()
time.sleep(3)
browser.save_screenshot("1.jpg")
# print(browser.title)
assert '禅道' in browser.title
# print(browser.find_element_by_css_selector("#userNav .user-name").text)
username = browser.find_element_by_css_selector("#userNav .user-name").text
assert 'admin' == username
# browser.back()
# browser.forward()
# browser.refresh()
# browser.close()
browser.quit()
