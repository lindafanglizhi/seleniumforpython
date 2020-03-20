from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
default_path = {"download.default_directory": "/Users/lindafang/PycharmProjects/selenium3forpython2020"}
options.add_experimental_option("prefs", default_path)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("http://www.sahitest.com/demo/php/fileUpload.htm")

# 第一个
# 如果是纯的js
change_visibility='document.querySelector("#file").style.visibility="visible";'
change_display='document.querySelector("#file").style.display="block";'

driver.execute_script(change_visibility)
driver.execute_script(change_display)
driver.find_element_by_id("file").send_keys("/Users/lindafang/PycharmProjects/selenium3forpython2020/advance-selenium-1/selenium-upload.pages")
# 第二个
change_visibility='document.querySelector("#file5").style.visibility="visible";'
change_display='document.querySelector("#file5").style.display="block";'
driver.execute_script(change_visibility)
driver.execute_script(change_display)
driver.find_element_by_id("file5").send_keys("/Users/lindafang/PycharmProjects/selenium3forpython2020/advance-selenium-1/selenium-upload.pages")
# 第三个
change_visibility='document.querySelector("#file2").style.visibility="visible";'
change_display='document.querySelector("#file2").style.display="block";'
driver.execute_script(change_visibility)
driver.execute_script(change_display)
driver.find_element_by_id("file2").send_keys("/Users/lindafang/PycharmProjects/selenium3forpython2020/advance-selenium-1/selenium-upload.pages")
change_visibility='document.querySelector("#file3").style.visibility="visible";'
change_display='document.querySelector("#file3").style.display="block";'
driver.execute_script(change_visibility)
driver.execute_script(change_display)
driver.find_element_by_id("file3").send_keys("/Users/lindafang/PycharmProjects/selenium3forpython2020/advance-selenium-1/selenium-upload.pages")
# 第四个
change_visibility='document.querySelector("#file4").style.visibility="visible";'
change_display='document.querySelector("#file4").style.display="block";'
driver.execute_script(change_visibility)
driver.execute_script(change_display)
driver.find_element_by_id("file4").send_keys("/Users/lindafang/PycharmProjects/selenium3forpython2020/advance-selenium-1/selenium-upload.pages")
# 第五个
change_visibility='document.querySelector("#files").style.visibility="visible";'
change_display='document.querySelector("#files").style.display="block";'
driver.execute_script(change_visibility)
driver.execute_script(change_display)
driver.find_element_by_id("files").send_keys("/Users/lindafang/PycharmProjects/selenium3forpython2020/advance-selenium-1/selenium-upload.pages")

# 第五个fileWdValidation
change_visibility='document.querySelector("#fileWdValidation").style.visibility="visible";'
change_display='document.querySelector("#fileWdValidation").style.display="block";'
driver.execute_script(change_visibility)
driver.execute_script(change_display)
driver.find_element_by_id("fileWdValidation").send_keys("/Users/lindafang/PycharmProjects/selenium3forpython2020/advance-selenium-1/selenium-upload.pages")

# 如果是jquery用下面这个
# change_visibility = '$("#file").css("visibility","visible");'
# change_display = '$("#file").css("display","block");'
# 如果是其他隐藏方式
'''
document.querySelector("#fileField").style.visibility="visible";
document.querySelector("#fileField").style.display="block";
document.querySelector("#fileField").style.width="200px";
document.querySelector("#fileField").style.height="200px";
document.querySelector("#fileField").style.position="fixed";
document.querySelector("#fileField").style.overflow="visible";
document.querySelector("#fileField").style.zIndex="999999";
document.querySelector("#fileField").style.top="500px";
document.querySelector("#fileField").style.bottom="500px";
document.querySelector("#fileField").style.left="500px";
document.querySelector("#fileField").style.right="500px";
document.querySelector("#fileField").style.marginBottom ="100px";

'''
