from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

driver = webdriver.Chrome("/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver")
driver.get("http://fex.baidu.com/webuploader/getting-started.html#%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0")

driver.find_element_by_name("file")\
    .send_keys("/Users/lindafang/PycharmProjects/selenium3forpython2020/advance-selenium-1/DevOps-Tutorial.pdf")
change_visibility='document.querySelector(".webuploader-element-invisible").style.visibility="visible";'
change_display='document.querySelector(".webuploader-element-invisible").style.display="block";'
driver.execute_script(change_visibility)
driver.execute_script(change_display)
driver.find_elements_by_name("file")[1].send_keys("/Users/lindafang/PycharmProjects/selenium3forpython2020/advance-selenium-1/1.png")