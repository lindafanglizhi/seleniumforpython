from selenium import webdriver
import time

# 打开浏览器
driver = webdriver.Chrome(executable_path="/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver78")

# 打开进入具体网址
driver.get("https://cn.bing.com/?FORM=BEHPTB")

# 浏览器某页的标题title
print(driver.title)
# 中断休息3秒
time.sleep(3)

driver.get("https://cn.bing.com/?FORM=BEHPTB&ensearch=1")
print(driver.title)
# 最大化窗口
driver.maximize_window()
# 返回刚才操作的页
driver.back()
print(driver.title)
# 向前进行操作的页
driver.forward()
print(driver.title)
time.sleep(3)
driver.save_screenshot("1.png")
# 刷新页面
driver.refresh()

# 关闭当前浏览器
driver.close()
# 关闭所有的浏览器
driver.quit()