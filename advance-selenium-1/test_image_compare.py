from urllib.request import urlretrieve
from selenium import webdriver
import ssl
from PIL import Image
from PIL import ImageChops
import time

ssl._create_default_https_context = ssl._create_unverified_context
dir1="/Users/lindafang/PycharmProjects/seleniumforpython2020/advance-selenium-1"
remote_img="{}/{}".format(dir1,"remote.png")
local_img="{}/{}".format(dir1,"local1.png")

driver =webdriver.Chrome("/Users/lindafang/PycharmProjects/seleniumforpython2020/driver/chromedriver")
driver.get("http://www.jianshu.com/")

logo=driver.find_element_by_xpath("//img[@alt='Nav logo']").get_attribute('src')
print(logo)
urlretrieve(logo,remote_img)
time.sleep(2)
driver.quit()


def compare(pic1,pic2,diff_save_location):
    '''
    :param pic1: 图片1路径
    :param pic2: 图片2路径
    :return: 返回对比的结果
    '''
    image1 = Image.open(pic1)
    image2 = Image.open(pic2)
    try:
        diff =ImageChops.difference(image1,image2)
        if diff.getbbox() is None:
        # 图片间没有任何不同则直接退出
            print("我们是相同的")
        else:
            diff.save(diff_save_location)
    except ValueError as e:
        text = ("表示图片大小和box对应的宽度不一致")
        print("【{0}】{1}".format(e,text))




compare(remote_img,local_img,"我们不一样.png")
