from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
default_path ={"download.default_directory":"/Users/lindafang/PycharmProjects/selenium3forpython2020"}
options.add_experimental_option("prefs",default_path)
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
driver.get("https://github.com/lindafanglizhi/restAssuredTest")
driver.find_element_by_css_selector("#js-repo-pjax-container > div.container-lg.clearfix.new-discussion-timeline.px-3 > div > div.file-navigation.in-mid-page.d-flex.flex-items-start > span > details > summary").click()
driver.find_element_by_css_selector("#js-repo-pjax-container > div.container-lg.clearfix.new-discussion-timeline.px-3 > div > div.file-navigation.in-mid-page.d-flex.flex-items-start > span > details > div > div > div.get-repo-modal-options > div.mt-2.d-flex > a.flex-1.btn.btn-outline.get-repo-btn.js-anon-download-zip-link").click()
driver.quit()
