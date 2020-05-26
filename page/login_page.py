import os, sys

sys.path.append(os.getcwd())
from base.base_action import BaseAction
from appium.webdriver.common.mobileby import MobileBy


class LoginPage(BaseAction):
    back_img = MobileBy.ID, 'com.tpshop.malls:id/title_back_rl'
    account_number_box = MobileBy.ID, 'com.tpshop.malls:id/mobile_et'
    password_box = MobileBy.ID, 'com.tpshop.malls:id/pwd_et'
    login_button = MobileBy.ID, 'com.tpshop.malls:id/login_tv'
    register_button = MobileBy.ID, 'com.tpshop.malls:id/register_tv'
    retrieve_password_button = MobileBy.ID, 'com.tpshop.malls:id/forget_pwd_tv'

    def __init__(self, driver):
        super().__init__(driver)

    # 返回
    def click_back_img(self):
        self.click(self.back_img)

    # 输入账号
    def input_account_number(self, account_number):
        self.input_text(self.account_number_box, account_number)

    # 输入密码
    def input_password(self, password):
        self.input_text(self.password_box, password)

    # 登录
    def click_login_button(self):
        self.click(self.login_button)

    # 选择用手机号注册
    def click_register_button(self):
        self.click(self.register_button)

    # 选择忘记密码
    def click_retrieve_password_button(self):
        self.click(self.retrieve_password_button)