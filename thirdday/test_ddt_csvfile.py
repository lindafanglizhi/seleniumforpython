import csv
import unittest
from ddt import ddt,data
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_csv_data(file_name):
    rows=[]
    with open(file_name,'r') as f:
        reader = csv.reader(f)
        next(reader,None)
        for row in reader:
            rows.append(row)
        return rows



@ddt
class TestDdtCsv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = '/Users/lindafang/PycharmProjects/seleniumforpython2020/driver/chromedriver78'
        cls.driver = webdriver.Chrome(executable_path=path)

        cls.driver.maximize_window()

        cls.driver.get("http://172.16.166.129:81/zentao/user-login.html")

    @data(*get_csv_data("test_data.csv"))
    def test_get_data(self,value):
        username = value[0]
        password = value[1]
        print('登陆的用户名：%s'% username, '密码是%s' % password)
        self.driver.find_element_by_id("account").send_keys(username)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element_by_id("submit").click()

        time.sleep(2)
        self.driver.find_element_by_class_name("dropdown-toggle").click()
        self.driver.find_element_by_link_text("退出").click()


    @classmethod
    def tearDownClass(cls):
        # pass
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

