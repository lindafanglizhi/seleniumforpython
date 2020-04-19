from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/Users/lindafang/PycharmProjects/"
                          "seleniumforpython2020/driver/chromedriver")
driver.execute_script("window.location='http://www.baidu.com'")
print(driver.execute_script("return document.title;"))
search = driver.execute_script("return document.getElementById('kw');")
print(search.get_attribute("class"))
driver.execute_script('document.getElementById("su").value = "你猜一下";')
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(2)
driver.execute_script("window.scrollBy(300,3000)")
ele = driver.find_element_by_link_text("selenium基础教程")
driver.execute_script("arguments[0].scrollIntoView(true);", ele)
print(ele.text)
driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background:yellow;color:Red;border:4px")
time.sleep(2)

driver.execute_script('$(arguments[0]).fadeOut()',ele)
# driver.execute_script("history.go(0)")


# driver.quit()
