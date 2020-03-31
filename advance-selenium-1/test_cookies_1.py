from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/lindafang/PycharmProjects/"
                          "selenium3forpython2020/driver/chromedriver")

# driver.get("https://www.jianshu.com/sign_in")
#
# driver.find_element_by_id("session_email_or_mobile_number").send_keys("18310107883")
# driver.find_element_by_id("session_password").send_keys("js7883.")
# driver.find_element_by_id("sign-in-form-submit-btn").click()
# # driver.get("https://www.jianshu.com/writer#/notebooks/33704618/notes/45883774")
# time.sleep(18)
cookies = driver.get_cookies()
# print(cookies)
# time.sleep(2)
driver.get("https://www.jianshu.com/")
driver.delete_all_cookies()
cookies1 = [{'domain': '.jianshu.com', 'expiry': 7892345419, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross',
             'path': '/', 'secure': False,
             'value': '%7B%22distinct_id%22%3A%2216068989%22%2C%22%24device_id%22%3A%22171120765d26a7-0ee1c66be83508-396a7f06-1296000-171120765d38f3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22171120765d26a7-0ee1c66be83508-396a7f06-1296000-171120765d38f3%22%7D'},
            {'domain': '.jianshu.com', 'expiry': 1587823817, 'httpOnly': True, 'name': 'web_login_version',
             'path': '/', 'secure': False, 'value': 'MTU4NTE0NTQxNw%3D%3D--76eb2296a432dec3df223022a9352439cbba42fb'},
            {'domain': '.jianshu.com', 'expiry': 1585151999, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user',
             'path': '/', 'secure': False, 'value': '1'},
            {'domain': 'www.jianshu.com', 'expiry': 1616681419, 'httpOnly': False, 'name': '__yadk_uid', 'path': '/',
             'secure': False, 'value': 'Wdxz2YevkShdIoeyjWfAmRHkJBE3bS3H'},
            {'domain': '.jianshu.com', 'httpOnly': False, 'name': 'Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068',
             'path': '/', 'secure': False, 'value': '1585145419'},
            {'domain': '.jianshu.com', 'expiry': 1585167019, 'httpOnly': True, 'name': '_m7e_session_core',
             'path': '/', 'secure': True, 'value': 'f66794ecd1aad4452b948fd1ac4199e4'},
            {'domain': '.jianshu.com', 'expiry': 1587823817, 'httpOnly': True, 'name': 'remember_user_token',
             'path': '/', 'secure': True,
             'value': 'W1sxNjA2ODk4OV0sIiQyYSQxMSQxTklQbkNWMldtUERCRkZDSUtvNm5PIiwiMTU4NTE0NTQxNy41NDE0MDgiXQ%3D%3D--febd5f60754ed5954e575bb12061f17ed29cbc7e'},
            {'domain': '.jianshu.com', 'expiry': 1616681419, 'httpOnly': False,
             'name': 'Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068', 'path': '/', 'secure': False, 'value': '1585145407'},
            {'domain': 'www.jianshu.com', 'httpOnly': False, 'name': 'default_font', 'path': '/', 'secure': False,
             'value': 'font2'},
            {'domain': 'www.jianshu.com', 'httpOnly': False, 'name': 'locale', 'path': '/', 'secure': False,
             'value': 'zh-CN'},
            {'domain': 'www.jianshu.com', 'httpOnly': False, 'name': 'read_mode', 'path': '/', 'secure': False,
             'value': 'day'}]


for cookies in cookies1:
    driver.add_cookie(cookies)
driver.get("https://www.jianshu.com/writer#/notebooks/33704618/notes/45883774")


# driver.quit()
