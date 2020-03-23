from urllib.request import urlretrieve
from selenium import webdriver
import time
import ssl
from PIL import Image
from PIL import ImageChops

ssl._create_default_https_context = ssl._create_unverified_context
dir1 = "/Users/lindafang/PycharmProjects/selenium3forpython2020/advance-selenium-1"
remote_img = "{}/{}".format(dir1, "remote1.png")
local_img = "{}/{}".format(dir1, "local.png")

driver = webdriver.Chrome("/Users/lindafang/PycharmProjects/selenium3forpython2020/driver/chromedriver")

driver.get("http://www.jianshu.com")
logo_url = driver.find_element_by_xpath("//img[@alt='Nav logo']").get_attribute("src")
print(logo_url)
# 下载网上文件
urlretrieve(logo_url, remote_img)
time.sleep(2)


# 使用pillow库，导入PIL
def compare(pic1, pic2, diff_save_location):
    image1 = Image.open(pic1)
    image2 = Image.open(pic2)
    try:
        diff = ImageChops.difference(image1, image2)
        if diff.getbbox() is None:
            print("是相同的")
        else:
            diff.save(diff_save_location)
    except ValueError as e:
        text = ("表示图片大小 和box对应的宽度不一致")
        print("[{0}]:{1}".format(e, text))


compare(remote_img,local_img,"diff.png")

driver.quit()
