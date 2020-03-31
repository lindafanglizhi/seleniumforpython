from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver")

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://space.bilibili.com/501526271")
list_A=driver.find_elements_by_xpath("//a")
print(list_A)
for i in list_A:
    try:
        href=i.get_attribute("href")
        # print(href)
        if href!=None and "https://www.bilibili.com/video" in href :
            print(href)
            driver.get(href)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".van-icon-videodetails_like")))
            driver.find_element_by_css_selector(".van-icon-videodetails_like").click()
            driver.find_element_by_css_selector(".bilibili-player-video-danmaku-input").send_keys("这个老师很幽默！")
            driver.find_element_by_css_selector(".bilibili-player-video-btn-send").click()
            time.sleep(2)
    except Exception as e:
        print(e)

