# from pywinauto import application
from selenium import webdriver
import time
driver = webdriver.Chrome("/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver")
driver.get("http://www.sahitest.com/demo/php/fileUpload.htm")
driver.find_element_by_id('file').click()   # 点击上传/浏览按钮
time.sleep(2)                      # 需要稍作等待，因为点击上传按钮到文件选择窗口打开会有延迟
# app = application.Application()   # 实例化Application
# # 这里用的class而没有加窗口title，主要为了保证兼容性
# app.connect(class_name='#32770')    #根据class_name找到弹出窗口
# app["Dialog"]["Edit1"].TypeKeys("/Users/lindafang/PycharmProjects/selenium3forpython2020/advance-selenium-1/remote.png")     # 在输入框中输入值
# app["Dialog"]["Button1"].click()                 # 点击打开/保存按钮