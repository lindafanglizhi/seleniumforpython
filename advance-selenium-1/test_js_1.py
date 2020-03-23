from selenium import webdriver
import time
driver = webdriver.Chrome("/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver")

# 打开网页
driver.execute_script("window.location='http://www.baidu.com'")
# 返回标题
print(driver.execute_script("return document.title;"))
# 获得页面元素
search=driver.execute_script("return document.getElementById('kw');")
# 获得元素属性
print(search.get_attribute("class"))
driver.find_element_by_id("kw").send_keys("selenium")
cc=driver.find_element_by_id("su")
# 修改元素属性
driver.execute_script("arguments[0].value='搜索一下'",cc)
time.sleep(1)
cc.click()
time.sleep(3)
# 滚动
driver.execute_script("window.scrollBy(300,3000)")
sele= driver.find_element_by_link_text("selenium基础教程")
# driver.execute_script("arguments[0].scrollIntoView[true];",sele)
#
# 高亮某元素
driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",sele,"background:yellow;color:Red;border:4px")
time.sleep(2)
# 让某个元素消失
driver.execute_script("$(arguments[0]).fadeOut()",sele)
time.sleep(2)
driver.quit()