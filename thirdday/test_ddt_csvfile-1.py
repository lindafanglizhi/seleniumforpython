import csv
import unittest
from ddt import ddt,data


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


    @data(*get_csv_data("test_data.csv"))
    def test_get_data(self,value):
        username = value[0]
        password = value[1]
        print('登陆的用户名：%s'% username, '密码是%s' % password)



if __name__ == '__main__':
    unittest.main()

