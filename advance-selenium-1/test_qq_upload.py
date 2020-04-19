from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/lindafang/PycharmProjects/"
                          "seleniumforpython2020/driver/chromedriver")

# QQ 邮箱的基础版
driver.get('https://mail.qq.com/cgi-bin/loginpage')
# time.sleep(2)
#因为全部都在ifrom的标签底下所以我们需要 先找到的是ifrom这个标签
l_frame = driver.find_element_by_id('login_frame')
#然后我们用切换语句切换到这个窗口底下在去找 如果直接去找的话是找不到的
driver.switch_to.frame(l_frame)
time.sleep(2)
driver.find_element_by_id("u").send_keys("1317854164")
driver.find_element_by_id("p").send_keys("******",Keys.RETURN)

driver.find_element_by_id("login_button").click()

# cookies = driver.get_cookies()
#
# login_cookies = {dic['name']:dic['value']for dic in cookies}
#
# print(login_cookies)
time.sleep(2)
# 切回默认
driver.switch_to.default_content()
# 断言
assert '1317854164@qq.com' == driver.find_element_by_id("useraddr").text
time.sleep(2)
# 点击写信
driver.find_element_by_id("composebtn").click()
time.sleep(2)
# 切到主框架
driver.switch_to.frame("mainFrame")
# 点击输入邮箱地址（可以封装成类，进行数据驱动，发给不同的人）
driver.find_element_by_xpath("//*[@id='toAreaCtrl']/div[2]/input").send_keys('fanglizhi@hljxlh.net')

time.sleep(2)

#输入主题

driver.find_element_by_id('subject').send_keys('测试主题')

time.sleep(2)

#退出iframe

driver.switch_to.default_content()

#再进入正文的iframe,先切入到大的frame，再切入到嵌套的frame中，分两步走

driver.switch_to.frame('mainFrame')

frame_boby=driver.find_element_by_xpath('//iframe[@scrolling="auto"]')

driver.switch_to.frame(frame_boby)

time.sleep(2)
# 输入正文（下文内容可以更换可以做成从文件 读）
driver.find_element_by_xpath('/html/body').send_keys('https://www.jianshu.com/u/030c07091ea4')
#退回到大的frame框架中再点击发送邮件
time.sleep(2)
# 切回父框架
driver.switch_to.parent_frame()
# 上传文件（后面的地址是你本地的地址，可以多个）
driver.find_element_by_name("UploadFile").send_keys("/Users/lindafang/PycharmProjects/seleniumforpython2020/advance-selenium-1/DevOps-Tutorial.pdf")

time.sleep(2)
# 发送
driver.find_element_by_name('sendbtn').click()

