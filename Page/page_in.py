from Page.page_setting import PageSetting
class PageIn():
    def __init__(self,driver):
        self.driver =driver
    def page_get_page_setting(self):
        return PageSetting(self.driver)