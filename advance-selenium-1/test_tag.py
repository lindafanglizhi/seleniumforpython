# Author: lindafang
# Date: 2020-04-16 20:05
# File: test_tag.py


from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/lindafang/PycharmProjects/"
                          "seleniumforpython2020/driver/chromedriver")
driver.get("http://cn.bing.com")
list1 =driver.find_elements_by_tag_name("a")
for li in list1:
    print(li.get_attribute('href'))
