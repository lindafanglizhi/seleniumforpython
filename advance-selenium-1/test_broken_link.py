from selenium import webdriver
import ssl
import requests
driver = webdriver.Chrome("/Users/lindafang/PycharmProjects/seleniumforpython2020/driver/chromedriver")
driver.get("http://www.jianshu.com/")
list_A=driver.find_elements_by_xpath("//a")
print(list_A)
for i in list_A:

    href=i.get_attribute("href")
    try:
        if href is not None or 'javascript:void(null)' not in href :
            ssl._create_default_https_context = ssl._create_unverified_context
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}

            req = requests.get(url=href,headers=headers)
            responsecode=req.status_code
            sec=req.elapsed.total_seconds()
            print("responsecode:", responsecode)
    except Exception as e:
        print(href)
        print(e)




