from Base.base import Base
import Page


class PageSetting(Base):
    def page_click_search(self):
        self.base_click(Page.search_btn)
    def page_input(self,text):
        self.base_input(Page.input_search,text)
    def page_back(self):
        self.base_click(Page.back_btn)