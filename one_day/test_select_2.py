from selenium import webdriver
import time

# 打开浏览器
driver = webdriver.Chrome(executable_path="/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver78")

# 打开进入具体网址
driver.get("https://cn.bing.com/")
# 将窗口最大化
driver.maximize_window()

# 通过id定位搜索框，在里面输入"python"
# driver.find_element_by_id("sb_form_q").send_keys("python")
time.sleep(2)
# 通过name定位
# driver.find_element_by_name("q").send_keys("武汉")
# 通过classname定位
# driver.find_element_by_class_name("b_searchbox").send_keys("北京")
# 通过xpath定位
# driver.find_element_by_xpath("//*[@id='sb_form_q']").send_keys("黑龙江")
# 通过css定位
# driver.find_element_by_css_selector("#sb_form_q").send_keys("疫情")
# 通过tagname定位,get_attribute是获得属性值
# print(driver.find_element_by_tag_name("body").get_attribute("class"))

# 通过id定位提交搜索，操作是点击
# driver.find_element_by_id("sb_form_go").click()
time.sleep(2)
# 通过link链接文字定位
# driver.find_element_by_link_text("视频").click()
# 通过link链接文字定位
# driver.find_element_by_partial_link_text("视").click()
# time.sleep(3)
# 关闭浏览器
driver.quit()