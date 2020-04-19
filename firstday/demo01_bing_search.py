from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# 增加--headless参数，可以静默执行
browser = webdriver.Chrome(executable_path="/Users/lindafang/PycharmProjects/seleniumforpython2020/driver/chromedriver78",chrome_options=chrome_options)

browser.get('http://www.bing.com')

assert '微软 Bing 搜索 ' in browser.title
print(browser.title)

elem = browser.find_element_by_id('sb_form_q')
elem.send_keys('seleniumhq' + Keys.RETURN)

assert 'selenium' in browser.page_source
print(browser.page_source)
browser.implicitly_wait(3)
browser.quit()

