from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome("/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver")
driver.get("http://jqueryui.com/resources/demos/sortable/connect-lists.html")
left2=driver.find_element_by_xpath("//*[@id='sortable1']/li[3]")
right2=driver.find_element_by_xpath("//*[@id='sortable2']/li[2]")

# ActionChains(driver).drag_and_drop(left2,right2).perform()
ActionChains(driver).click_and_hold(left2)\
    .move_to_element(right2)\
    .release(right2)\
    .perform()
