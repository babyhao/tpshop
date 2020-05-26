import os, sys

sys.path.append(os.getcwd())
from base.base_action import BaseAction
from appium.webdriver.common.mobileby import MobileBy


class SearchPage(BaseAction):
    back_button = MobileBy.ID, 'com.tpshop.malls:id/back_img'
    search_box = MobileBy.ID, 'com.tpshop.malls:id/search_et'
    search_for_button = MobileBy.ID, 'com.tpshop.malls:id/search_btn'
    hot_search_first_button = MobileBy.ANDROID_UIAUTOMATOR, 'resourceId("com.tpshop.malls:id/search_key_layout").childSelector(index(0))'
    search_history_second_button = MobileBy.ANDROID_UIAUTOMATOR, 'resourceId("com.tpshop.malls:id/search_key_list").childSelector(index(1))'
    delete_search_history_third_button = MobileBy.ANDROID_UIAUTOMATOR, 'resourceId("com.tpshop.malls:id/search_key_list").childSelector(index(2)).childSelector(index(1))'

    def __init__(self, driver):
        super().__init__(driver)

    # 返回
    def click_back_button(self):
        self.click(self.back_button)

    # 输入搜索内容
    def input_search_text(self, text):
        self.input_text(self.search_box, text)

    # 开始搜索
    def click_search_for_button(self):
        self.click(self.search_for_button)

    # 点击热搜榜的第一名
    def click_hot_search_button(self):
        self.click(self.hot_search_first_button)

    # 点击搜索历史的第二个
    def click_search_history_button(self):
        self.click(self.search_history_second_button)

    # 删除搜索历史的第三个
    def click_delete_button(self):
        self.click(self.delete_search_history_third_button)