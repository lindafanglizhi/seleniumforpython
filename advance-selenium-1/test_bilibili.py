from selenium import webdriver
import time
import pyautogui
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

option1 = webdriver.ChromeOptions()
option1.add_argument('disable-infobars')
driver = webdriver.Chrome(executable_path="/Users/lindafang/PycharmProjects/"
                                          "selenium3forpython2020/driver/chromedriver",options=option1)
# driver.get("https://passport.bilibili.com/login")
# time.sleep(2)
# driver.find_element_by_id("login-username").send_keys("18145198883")
# driver.find_element_by_id("login-passwd").send_keys("blmyid88.")
# driver.find_element_by_css_selector(".btn-login").click()
# time.sleep(10)
# coo=driver.get_cookies()
# print(coo)
driver.get("https://www.bilibili.com/")
driver.maximize_window()
driver.implicitly_wait(10)
cookie = [{'domain': '.bilibili.com', 'httpOnly': False, 'name': 'INTVER', 'path': '/', 'secure': False, 'value': '1'},
          {'domain': '.bilibili.com', 'expiry': 1600925991, 'httpOnly': False, 'name': 'bili_jct', 'path': '/',
           'secure': False, 'value': 'facf39adc998d977b665c33082cad439'},
          {'domain': '.bilibili.com', 'expiry': 1600925991, 'httpOnly': True, 'name': 'SESSDATA', 'path': '/',
           'secure': False, 'value': '91942a54%2C1600926959%2Ccacec*31'},
          {'domain': '.bilibili.com', 'expiry': 1600925991, 'httpOnly': False, 'name': 'DedeUserID', 'path': '/',
           'secure': False, 'value': '501526271'},
          {'domain': '.bilibili.com', 'expiry': 2177452831, 'httpOnly': False, 'name': 'LIVE_BUVID', 'path': '/',
           'secure': False, 'value': 'AUTO8615853749547869'},
          {'domain': '.bilibili.com', 'expiry': 253402300799, 'httpOnly': False, 'name': 'PVID', 'path': '/',
           'secure': False, 'value': '1'},
          {'domain': '.bilibili.com', 'expiry': 1616910982, 'httpOnly': False, 'name': 'sid', 'path': '/',
           'secure': False, 'value': '8qwg24f3'},
          {'domain': '.bilibili.com', 'expiry': 1679982949, 'httpOnly': False, 'name': 'buvid3', 'path': '/',
           'secure': False, 'value': '753EF907-3453-4072-95A9-E7B6F2444E7D155803infoc'},
          {'domain': '.bilibili.com', 'expiry': 1600925991, 'httpOnly': False, 'name': 'DedeUserID__ckMd5',
           'path': '/', 'secure': False, 'value': '3c19133e5ac741ee'},
          {'domain': '.bilibili.com', 'expiry': 1616910949, 'httpOnly': False, 'name': '_uuid', 'path': '/',
           'secure': False, 'value': '80DCA440-0B74-ED9F-3DD9-6E99FDD5E48C49542infoc'}]
driver.delete_all_cookies()

for cook in cookie:
    driver.add_cookie(cook)
time.sleep(3)
driver.get("https://space.bilibili.com/501526271")
list_A=driver.find_elements_by_xpath("//a")
print(list_A)
for i in list_A:
    try:
        link_text=i.get_attribute("title")
        # print(link_text)
        if link_text!=None and "linda" in link_text:

            print(link_text)
            driver.find_element_by_partial_link_text(link_text).click()
            time.sleep(5)
            driver.execute_script("window.scrollBy(300,3000)")
            # pyautogui.click(171,785)
            pyautogui.mouseDown(171, 785, 2, button='left')
            pyautogui.mouseUp(171, 785, 2, button='left')
            # driver.find_element_by_id("player_placeholder").click()
            # driver.find_element_by_id("bilibiliPlayer").click()
            # list_input =driver.find_elements_by_tag_name("input")
            # for input in list_input:
            #     class_name=input.get_attribute("class")
            #     print(input.get_attribute("class"))
                # driver.find_element_by_class_name(class_name).send_keys("")
            # time.sleep(3)
            # break
    except Exception as e:
        print(e)

