# 建立csv文件--excel表建立完成导出成csv格式 ，utf-8  ,记事本另存为csv
# 读取csv每一个数据
# 在通过ddt方式 实现数据驱动


import csv
import unittest
from ddt import ddt,data
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_csvdata(file_name):
    rows=[]
    with open(file_name,'r') as f:
        reader1 = csv.reader(f)
        # 跳过第一行
        next(reader1, None)
        for row in reader1:
            rows.append(row)
        print(rows)
        return rows



@ddt
class TestDdtCsv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = '/Users/lindafang/PycharmProjects/seleniumforpython2020/driver/chromedriver78'
        cls.driver = webdriver.Chrome(executable_path=path)

        cls.driver.maximize_window()
        cls.driver.get("http://172.16.166.129:81/zentao/user-login.html")

    @classmethod
    def tearDownClass(cls):
        # pass
        cls.driver.close()
        cls.driver.quit()

    @data(*get_csvdata("test_data.csv"))
    def test_csv_getdata(self,value):
        username=value[0]
        password=value[1]
        print("用户名是%s" % username,"密码是%s" % password)
        self.driver.find_element_by_id("account").send_keys(username)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element_by_id("submit").click()
        time.sleep(3)
        self.driver.find_element_by_class_name("dropdown-toggle").click()
        self.driver.find_element_by_link_text("退出").click()


if __name__ == '__main__':
    unittest.main()



