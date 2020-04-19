from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
# 浏览器选项
options=webdriver.ChromeOptions()
# 设置下载内容的默认路径
prefs={"download.default_directory":"/Users/lindafang/PycharmProjects/seleniumforpython2020"}
# 将这个路径加入到浏览器选项中
options.add_experimental_option("prefs",prefs)
# 自动下载浏览器的驱动程序
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
driver.get("https://github.com/lindafanglizhi/restAssuredTest")
driver.maximize_window()
driver.find_element_by_css_selector("#js-repo-pjax-container > div.container-lg.clearfix.new-discussion-timeline.px-3 > div > div.file-navigation.in-mid-page.d-flex.flex-items-start > span > details > summary").click()
time.sleep(1)
driver.find_element_by_css_selector("#js-repo-pjax-container > div.container-lg.clearfix.new-discussion-timeline.px-3 > div > div.file-navigation.in-mid-page.d-flex.flex-items-start > span > details > div > div > div.get-repo-modal-options > div.mt-2.d-flex > a.flex-1.btn.btn-outline.get-repo-btn.js-anon-download-zip-link").click()
time.sleep(5)
driver.quit()