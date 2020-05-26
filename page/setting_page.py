import os, sys

sys.path.append(os.getcwd())
from base.base_action import BaseAction
from appium.webdriver.common.mobileby import MobileBy


class MinePage(BaseAction):
    back_button = MobileBy.ID, 'com.tpshop.malls:id/title_back_rl'
    customer_service_button = MobileBy.XPATH, '//*[contains(@text,"客服电话")]/..'
    about_us_button = MobileBy.XPATH, '//*[@text="关于我们"]/..'
    clear_cache_button = MobileBy.XPATH, '//*[contains(@text,"清除缓存")]/..'
    check_version_button = MobileBy.XPATH, '//*[contains(@text,"检测版本")]/..'
    retreat_safely_button = MobileBy.ID, 'com.tpshop.malls:id/exit_tv'

    def __init__(self, driver):
        super().__init__(driver)

    # 返回
    def click_back_button(self):
        self.click(self.back_button)

    # 跳转到拨打客服电话的拨号页
    def click_customer_service_button(self):
        self.click(self.customer_service_button)

    # 查看“关于我们”
    def click_about_us_button(self):
        self.click(self.about_us_button)

    # 清除缓存
    def click_clear_cache_button(self):
        self.click(self.clear_cache_button)

    # 查看版本
    def click_check_version_button(self):
        self.click(self.check_version_button)

    # 退出登录
    def click_retreat_safely_button(self):
        self.click(self.retreat_safely_button)