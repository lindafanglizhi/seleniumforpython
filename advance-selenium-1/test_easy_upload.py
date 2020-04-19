# __picker-input

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# 自动下载浏览器的驱动程序
driver = webdriver.Chrome(executable_path="/Users/lindafang/PycharmProjects/seleniumforpython2020/driver/chromedriver")
driver.get("https://smallpdf.com/cn/pdf-to-word")
driver.maximize_window()
time.sleep(3)
# change_visibility = '$("#__picker-input").css("visibility","visible");'
# change_display = '$("#__picker-input").css("display","block");'
# change_width='$("#__picker-input").css("width","200px");'
# change_height='$("#__picker-input").css("height","200px");'
# change_position='$("#__picker-input").css("position","fixed");'
# change_overflow='$("#__picker-input").css("overflow","visible");'
# change_zIndex='$("#__picker-input").css("zIndex","999999");'
# change_top='$("#__picker-input").css("top","500px");'
# change_bottom='$("#__picker-input").css("bottom","500px");'
# change_left='$("#__picker-input").css("left","500px");'
# change_right='$("#__picker-input").css("right","500px");'
# change_marginBottom='$("#__picker-input").css("marginBottom","100px");'
#
# driver.execute_script(change_visibility)
# driver.execute_script(change_display)
# driver.execute_script(change_zIndex)
# driver.execute_script(change_width)
# driver.execute_script(change_height)
# driver.execute_script(change_overflow)
# driver.execute_script(change_position)
# driver.execute_script(change_top)
# driver.execute_script(change_bottom)
# driver.execute_script(change_left)
# driver.execute_script(change_right)
# driver.execute_script(change_marginBottom)
change_visibility='document.querySelector("#__picker-input").style.visibility="visible";'
change_display='document.querySelector("#f__picker-input").style.display="block";'

driver.execute_script(change_visibility)
# driver.execute_script(change_display)
time.sleep(2)
driver.find_element_by_id("__picker-input").send_keys("/Users/lindafang/PycharmProjects/seleniumforpython2020/advance-selenium-1/DevOps-Tutorial.pdf")
time.sleep(5)
# driver.quit()