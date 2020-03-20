from ddt import ddt,file_data
import unittest

'''
实现DDT的步骤：
1、在测试类上使用@ddt装饰符
2、在测试方法上使用@file_data装饰符
3、@file_data
4、将传入的列表解析（折包）使用@unpack

'''

@ddt
class TestDdtFile(unittest.TestCase):
    @unittest.skip
    @file_data('test_data.yml')
    def test_yaml(self, value):
        print(value)

    # json----dict  --**
    @unittest.skip
    @file_data('test_data_interface.yaml')
    def test_yaml_interface(self, **value):
        print(value)
        print(type(value))


    @file_data('test_data.json')
    def test_json(self, value):
        print(value)

    @unittest.skip
    @file_data('test_data1.json')
    def test_json_com(self, **value):
        print(value)

if __name__ == '__main__':
    unittest.main()
