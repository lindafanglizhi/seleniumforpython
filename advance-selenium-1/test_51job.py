# 导入selenium
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time
# 下载 驱动并且打开浏览器
driver = webdriver.Chrome("/Users/lindafang/PycharmProjects/"
                          "selenium3forpython2020/driver/chromedriver")

driver.get("http://www.51job.com")
driver.find_element_by_id("kwdselectid").send_keys("软件测试工程师")
# 点击哈尔滨，改成北京
driver.find_element_by_id("work_position_input").click()
driver.find_element_by_id("work_position_click_multiple_selected").click()
driver.find_element_by_id("work_position_click_center_right_list_category_000000_010000").click()
driver.find_element_by_id("work_position_click_bottom_save").click()
# 打开具体页，可以没有
driver.get("https://search.51job.com/list/010000,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=")
zhiwei_list = []
try:
    for i in range(5,53):
        # 测试工程师链接定位
        href_e=driver.find_element_by_xpath("//*[@id='resultList']/div[%s]/p/span/a" % i)
        # 获得每一个链接href
        href=href_e.get_attribute("href")
        # //*[@id="resultList"]/div[53]/p/span/a
        # //*[@id="resultList"]/div[6]/p/span/a
        print(href)
        driver.get(href)
        # 职位信息定位
        ele =driver.find_element_by_css_selector(".bmsg")
        if ele is not None:
            print(ele.text)

            zhiwei_list.append(ele.text)
            print("-----------------")
        driver.back()
except Exception as e:
    print(e)
str =" ".join(zhiwei_list)
with open("zhiwei.txt", 'w+')as f:
    f.write(str)
time.sleep(3)
# driver.quit()
