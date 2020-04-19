from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/lindafang/PycharmProjects/"
                          "seleniumforpython2020/driver/chromedriver")

# driver.get("http://www.jianshu.com")
# cookies=driver.get_cookies()
# print(cookies)
driver.get("https://www.jianshu.com/sign_in")

time.sleep(2)
# wh =driver.window_handles
# print(wh)

driver.find_element_by_id("session_email_or_mobile_number").click()
driver.find_element_by_id("session_email_or_mobile_number").send_keys("18310107883")
driver.find_element_by_id("session_password").send_keys("js7883.")
time.sleep(3)
driver.find_element_by_id("sign-in-form-submit-btn").click()
time.sleep(18)
driver.get("https://www.jianshu.com/writer#/notebooks/33704618/notes/45883774")
# cookies1=driver.get_cookies()
# print(cookies1)
# cookies_login=[{'domain': '.jianshu.com', 'expiry': 7892323340, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%2216068989%22%2C%22%24device_id%22%3A%2217110b679bd550-0e3b128f301e5e-396a7f06-1296000-17110b679bea76%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2217110b679bd550-0e3b128f301e5e-396a7f06-1296000-17110b679bea76%22%7D'},
#                {'domain': '.jianshu.com', 'expiry': 1587801739, 'httpOnly': True, 'name': 'web_login_version', 'path': '/', 'secure': False, 'value': 'MTU4NTEyMzMzOQ%3D%3D--c50672fee20c2a2ab937dd6479ac14c17fa05b3c'},
#                {'domain': '.jianshu.com', 'expiry': 1585151999, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'secure': False, 'value': '1'},
#                {'domain': '.jianshu.com', 'httpOnly': False, 'name': 'Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068', 'path': '/', 'secure': False, 'value': '1585123341'},
#                {'domain': '.jianshu.com', 'expiry': 1585144941, 'httpOnly': True, 'name': '_m7e_session_core', 'path': '/', 'secure': True, 'value': '4149ee152bec20c0f9fd8f0b14670218'},
#                {'domain': '.jianshu.com', 'expiry': 1587801739, 'httpOnly': True, 'name': 'remember_user_token', 'path': '/', 'secure': True, 'value': 'W1sxNjA2ODk4OV0sIiQyYSQxMSQxTklQbkNWMldtUERCRkZDSUtvNm5PIiwiMTU4NTEyMzMzOS4wNzU1NTYiXQ%3D%3D--f2289e24dcebc550bd7cfacde2f33aa5e64aa12f'},
#                {'domain': '.jianshu.com', 'expiry': 1616659340, 'httpOnly': False, 'name': 'Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068', 'path': '/', 'secure': False, 'value': '1585123327'},
#                {'domain': 'www.jianshu.com', 'expiry': 1616659326, 'httpOnly': False, 'name': '__yadk_uid', 'path': '/', 'secure': False, 'value': 'lgUsQef9uraDEiKEU1m3AMivrSwKMdCT'},
#                {'domain': 'www.jianshu.com', 'httpOnly': False, 'name': 'default_font', 'path': '/', 'secure': False, 'value': 'font2'},
#                {'domain': 'www.jianshu.com', 'httpOnly': False, 'name': 'locale', 'path': '/', 'secure': False, 'value': 'zh-CN'},
#                {'domain': 'www.jianshu.com', 'httpOnly': False, 'name': 'read_mode', 'path': '/', 'secure': False, 'value': 'day'}]
# driver.delete_all_cookies()
# time.sleep(3)
# for cookie in cookies_login:
#     print(cookie)
#     driver.add_cookie(cookie)
# time.sleep(5)
# driver.get("https://www.jianshu.com/writer#/notebooks/33704618/notes/45883774")

#
# time.sleep(18)
time.sleep(8)
print(driver.window_handles)
driver.switch_to.window("CDwindow-52E08BC4BCD84E8A71A3AF016131963D")

driver.find_element_by_css_selector("._3P4JX _2VLy-").click()
time.sleep(2)
driver.find_element_by_class_name("fa fa-plus").click()
driver.find_element_by_class_name("_24i7u").send_keys("这是要测试的内容标题")
driver.find_element_by_id("arthur-editor").send_keys("这是文章内容")
time.sleep(2)
driver.find_element_by_class_name("tGbI7 cztJE").click()


# driver.quit()