from ddt import ddt,data,unpack
import unittest

'''
实现DDT的步骤：
1、在测试类上使用@ddt装饰符
2、在测试方法上使用@data装饰符
3、@data  把参数当作 测试数据，参数可以是单个值，列表，元组，字典
4、将传入的列表解析（折包）使用@unpack

'''
@ddt
class TestDdt(unittest.TestCase):
    @unittest.skip
    @data('你好', '1', 'hello')
    def test_var(self, value):
        print(value)
        assert '你好' == value

    @unittest.skip
    @data([2],[1])
    @unpack
    def test_list(self, value):
        print(value)
        assert 3 == value +1

    @unittest.skip
    @data((1, 2), (2, 3))
    @unpack
    def test_tuple(self, value1, value2):
        print(value1, value2)
        assert value2 == value1 + 1

    @unittest.skip
    @data({'first': 1, 'second': 3, 'third': 5},
          {'first': 4, 'second': 7, 'third': 8})
    @unpack
    def test_dicts(self, first, second, third):
        self.assertTrue(first < second < third)


    @data({'name':'linda','age':'18'})
    @unpack
    def test_dict1(self,name,age):
        print(name,age)



if __name__ == '__main__':
    unittest.main()

