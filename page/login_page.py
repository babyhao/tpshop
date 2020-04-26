import os, sys
sys.path.append(os.getcwd())
from base.base_action import BaseAction
from appium.webdriver.common.mobileby import MobileBy


class LoginPage(BaseAction):
    mine_button = MobileBy.ID, 'com.tpshop.malls:id/mine_ll'
    login_or_signup_button = MobileBy.ID, 'com.tpshop.malls:id/head_img'
    username_input_box = MobileBy.ID, 'com.tpshop.malls:id/mobile_et'
    password_input_box = MobileBy.ID, 'com.tpshop.malls:id/pwd_et'
    login_button = MobileBy.ID, 'com.tpshop.malls:id/login_tv'

    def __init__(self, driver):
        super().__init__(driver)
        # 点击“我的”
        self.click(self.mine_button)
        # 点击“登录/注册”
        self.click(self.login_or_signup_button)

    # 输入用户名
    def input_username(self, username):
        self.input_text(self.username_input_box, username)

    # 输入密码
    def input_password(self, password):
        self.input_text(self.password_input_box, password)

    # 点击“登录”
    def click_login(self):
        self.click(self.login_button)