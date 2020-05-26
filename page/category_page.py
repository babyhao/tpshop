import sys, os

sys.path.append(os.getcwd())
from base.base_action import BaseAction
from appium.webdriver.common.mobileby import MobileBy


class CategoryPage(BaseAction):
    category_tab = MobileBy.ID, 'com.tpshop.malls:id/category_ll'
    search_box = MobileBy.ID, 'com.tpshop.malls:id/search_key_et'
    message_center_img = MobileBy.ID, 'com.tpshop.malls:id/msg_img'
    cellphone_tab = MobileBy.ANDROID_UIAUTOMATOR, 'text("手机").resourceId("com.tpshop.malls:id/category_left_name_tv")'
    clothes_tab = MobileBy.ANDROID_UIAUTOMATOR, 'resourceId("com.tpshop.malls:id/category_left_name_tv").text("服饰")'
    computer_tab = MobileBy.ANDROID_UIAUTOMATOR, 'resourceId("com.tpshop.malls:id/category_left_name_tv").text("电脑")'
    household_tab = MobileBy.ANDROID_UIAUTOMATOR, 'resourceId("com.tpshop.malls:id/category_left_name_tv").text("家居")'
    shoes_tab = MobileBy.ANDROID_UIAUTOMATOR, 'resourceId("com.tpshop.malls:id/category_left_name_tv").text("鞋类")'
    cellphone_goods = MobileBy.XPATH, '//*[@text="手机数码"][@resource-id="com.tpshop.malls:id/category_item_tv"]/..'

    def __init__(self, driver):
        super().__init__(driver)

    # 进入分类页
    def switch_to_category_page(self):
        self.click(self.category_tab)

    # 点击搜索框
    def click_search_box(self):
        self.click(self.search_box)

    # 打开消息中心
    def click_message_center_img(self):
        self.click(self.message_center_img)

    # 选择手机标签
    def click_cellphone_tab(self):
        self.click(self.cellphone_tab)

    # 选择服饰标签
    def click_clothes_tab(self):
        self.click(self.clothes_tab)

    # 选择电脑标签
    def click_computer_tab(self):
        self.click(self.computer_tab)

    # 选择家居标签
    def click_household_tab(self):
        self.click(self.household_tab)

    # 选择鞋类标签
    def click_shoes_tab(self):
        self.click(self.shoes_tab)

    # 进入手机数码类目
    def click_cellphone_goods(self):
        self.click(self.cellphone_goods)