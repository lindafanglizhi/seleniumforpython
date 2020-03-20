import pytest
# 先导入pip install pytest
from selenium import webdriver
import datetime, os
from util.get_path import get_par_path
import allure
from fourday.pageobject.pages import pages
from util.read_yaml import get_yaml_data

# driver是全局吗？


@allure.feature('打开浏览器')
@pytest.fixture(scope="module")
def driver(request):
    driver_path = os.path.join(get_par_path(), "driver/chromedriver78")
    driver = webdriver.Chrome(executable_path=driver_path)

    def close_browser():
        driver.quit()

    # 无论执行正确和错误最终都执行关闭浏览器的方法
    request.addfinalizer(close_browser)
    return driver


class TestBingSo():
    @allure.feature("打开bing首页")
    @pytest.fixture(scope="module",autouse=True)
    def open_bingpage(self, driver):
        with allure.step("step 1:打开浏览器，输入必应的地址"):
            driver.get("https://cn.bing.com/?ensearch=1&FORM=BEHPTB")
            driver.maximize_window()
            driver.implicitly_wait(10)


    test_data =get_yaml_data("test_data_soso.yml")


    @allure.step("初始化数据")
    @pytest.fixture()
    def sosovalue(self,request):
        value=request.param
        return value

    @pytest.mark.parametrize("sosovalue",test_data)
    @allure.feature("必应的搜索功能")
    @allure.story("验证不同的搜索信息，返回的结果是否正确")
    def test_soso(self,driver,sosovalue):
        with allure.step("step 2:加载主页页面，加载成功"):
            main_page = pages.MainPage(driver)
            assert 'Bing' in main_page.title_matches()
        with allure.step("step 3:输入搜索信息，点击搜索"):
            main_page.enter_search_text(sosovalue)
            main_page.click_search_button()
        with allure.step("step 4:加载搜索结果页"):
            search_result_page = pages.SearchResultPage(driver)
        with allure.step("step 5:验证结果成功"):
            assert sosovalue in search_result_page.results_found()
        with allure.step("step 6:截图"):
            filename=str(datetime.datetime.now()) + "_soso.png"
            search_result_page.save_pic(filename)
            allure.attach.file(filename,attachment_type=allure.attachment_type.PNG)


if __name__ == '__main__':
    pytest.main()


