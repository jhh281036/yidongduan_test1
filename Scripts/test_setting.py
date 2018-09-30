import os,sys
sys.path.append(os.getcwd())
import pytest
from appium import webdriver



from Base.get_driver import get_driver
from Base.read_yaml import ReadYaml02
from Page.page_in import PageIn


# 测试封装的读取工具类方法
def get_data():
    return ReadYaml02().read_yaml()




class TestSetting():
    def setup_class(self):
        # 获取driver
        self.driver = get_driver()
        # 实例化driver
        self.page = PageIn(self.driver)
        # 获取pageSetting实例化对象，为什么要拿到setting对象
        self.setting =self.page.page_get_page_setting()
    def teardown_class(self):
        # 关闭驱动对象
        self.driver.quit()
    # 测试方法
    @pytest.mark.parametrize("text", get_data())
    def test_seach(self,text):
        # 按照操作步骤完成
        # 点击搜索按钮
        self.setting.page_click_search()
        # 输入信息

        self.setting.base_input(text)
        # 点击返回按钮
        self.setting.page_back()

if __name__ == '__main__':
    pytest.main()
