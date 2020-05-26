import sys, os

sys.path.append(os.getcwd())
from appium.webdriver.common.mobileby import MobileBy
from base.base_action import BaseAction


class AddressPage(BaseAction):
    back_img = MobileBy.ID, 'com.tpshop.malls:id/title_back_rl'
    new_address_button = MobileBy.ID, 'com.tpshop.malls:id/add_address_tv'
    address_of_nero_button = MobileBy.XPATH, '//*[@text="nero"]/..'

    def __init__(self, driver):
        super().__init__(driver)

    # 返回
    def click_back_img(self):
        self.click(self.back_img)

    # 添加收获地址
    def click_new_address_button(self):
        self.click(self.new_address_button)

    # 选择nero的地址
    def click_address_of_nero_button(self):
        self.click(self.address_of_nero_button)