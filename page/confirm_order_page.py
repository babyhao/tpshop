import sys, os

sys.path.append(os.getcwd())
from appium.webdriver.common.mobileby import MobileBy
from base.base_action import BaseAction


class ConfirmOrderPage(BaseAction):
    back_img = MobileBy.ID, 'com.tpshop.malls:id/title_back_rl'
    address_button = MobileBy.ID, 'com.tpshop.malls:id/consignee_layout'
    submit_orders_button = MobileBy.ID, 'com.tpshop.malls:id/submit_tv'

    def __init__(self, driver):
        super().__init__(driver)

    # 返回
    def click_back_img(self):
        self.click(self.back_img)

    # 选择收获地址
    def click_address_button(self):
        self.click(self.address_button)

    # 提交订单
    def click_submit_orders_button(self):
        self.click(self.submit_orders_button)