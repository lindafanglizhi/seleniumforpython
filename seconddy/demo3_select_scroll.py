from selenium import webdriver
import time

# select类是选择类，主要场景是下拉菜单，获得菜单内容选择项，并进行操作。
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome(executable_path="/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver78")
browser.get("http://172.16.166.129/zentao/")
browser.find_element_by_id("account").send_keys("admin")
browser.find_element_by_name("password").send_keys("123456.")
browser.find_element_by_id("submit").click()
time.sleep(3)
browser.find_element_by_link_text("组织").click()
browser.find_element_by_link_text("添加用户").click()
browser.maximize_window()
isEdit = browser.find_element_by_id("account").is_enabled()
print(isEdit)
browser.find_element_by_id("account").click()
browser.find_element_by_id("account").clear()
browser.find_element_by_id("account").send_keys("linda333")

browser.find_element_by_id("password1").click()
browser.find_element_by_id("password1").clear()
browser.find_element_by_id("password1").send_keys("f138!@#$%^.")
time.sleep(1)
browser.find_element_by_id("password2").click()
browser.find_element_by_id("password2").clear()
browser.find_element_by_id("password2").send_keys("f138!@#$%^.")
time.sleep(1)
browser.find_element_by_id("realname").click()
browser.find_element_by_id("realname").clear()
browser.find_element_by_id("realname").send_keys("房荔枝777")
browser.find_element_by_id("role").click()
# <select name="role" id="role" class="form-control" onchange="changeGroup(this.value)">
# <option value="" selected="selected" title="" data-keys=" "></option>
# <option value="dev" title="研发" data-keys="yanfa yf">研发</option>
# <option value="qa" title="测试" data-keys="ceshi cs">测试</option>
# <option value="pm" title="项目经理" data-keys="xiangmujingli xmjl">项目经理</option>
# <option value="po" title="产品经理" data-keys="chanpinjingli cpjl">产品经理</option>
# <option value="td" title="研发主管" data-keys="yanfazhuguan yfzg">研发主管</option>
# <option value="pd" title="产品主管" data-keys="chanpinzhuguan cpzg">产品主管</option>
# <option value="qd" title="测试主管" data-keys="ceshizhuguan cszg">测试主管</option>
# <option value="top" title="高层管理" data-keys="gaocengguanli gcgl">高层管理</option>
# <option value="others" title="其他" data-keys="qita qt">其他</option>
# </select>
role = browser.find_element_by_id("role")
# Select(role).select_by_value("qa")
Select(role).select_by_index(2)
# Select(browser.find_element_by_id("role")).select_by_visible_text("测试")
browser.execute_script("window.scrollBy(0,2000)")
browser.find_element_by_id("genderf").click()
browser.find_element_by_id("verifyPassword").click()
browser.find_element_by_id("verifyPassword").clear()
browser.find_element_by_id("verifyPassword").send_keys("123456.")
browser.find_element_by_id("submit").click()
time.sleep(2)
# assert ("lindafang" in browser.page_source)
browser.quit()


