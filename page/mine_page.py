import os, sys

sys.path.append(os.getcwd())
from base.base_action import BaseAction
from appium.webdriver.common.mobileby import MobileBy


class MinePage(BaseAction):
    mine_tab = MobileBy.ID, 'com.tpshop.malls:id/mine_ll'
    setting_img = MobileBy.ID, 'com.tpshop.malls:id/setting_btn'
    head_img = MobileBy.ID, 'com.tpshop.malls:id/head_img'
    balance_button = MobileBy.ID, 'com.tpshop.malls:id/balance_l'
    points_button = MobileBy.ID, 'com.tpshop.malls:id/point_ll'
    my_order_button = MobileBy.XPATH, '//*[@text="My Order"]/..'
    coupon_button = MobileBy.XPATH, '//*[@text="优惠券"]/..'
    poster_button = MobileBy.XPATH, '//*[@text="海报"]/..'
    group_order_button = MobileBy.XPATH, '//*[@text="拼团订单"]/..'
    my_evaluation_button = MobileBy.XPATH, '//*[@text="我的评价"]/..'
    points_exchange_button = MobileBy.XPATH, '//*[@text="积分兑换"]/..'
    my_signin_button = MobileBy.XPATH, '//*[@text="我的签到"]/..'
    coupon_center_button = MobileBy.XPATH, '//*[@text="领券中心"]/..'
    my_collection_button = MobileBy.XPATH, '//*[@text="我的收藏"]/..'
    my_track_button = MobileBy.XPATH, '//*[@text="我的足迹"]/..'
    my_message_button = MobileBy.XPATH, '//*[@text="我的消息"]/..'
    address_management_button = MobileBy.XPATH, '//*[@text="地址管理"]/..'
    username_input_box = MobileBy.ID, 'com.tpshop.malls:id/mobile_et'
    password_input_box = MobileBy.ID, 'com.tpshop.malls:id/pwd_et'
    login_button = MobileBy.ID, 'com.tpshop.malls:id/login_tv'

    def __init__(self, driver):
        super().__init__(driver)

    # 进入“我的”
    def switch_to_mine_page(self):
        self.click(self.mine_tab)

    # 点击设置图标
    def click_setting_button(self):
        self.click(self.setting_img)

    # 点击头像
    def click_head_img(self):
        self.click(self.head_img)

    # 点击余额按钮
    def click_balance_button(self):
        self.click(self.balance_button)

    # 点击积分按钮
    def click_points_button(self):
        self.click(self.points_button)

    # 点击进入“我的订单”页
    def click_my_order_button(self):
        self.click(self.my_order_button)

    # 点击优惠券按钮
    def click_coupon_button(self):
        self.click(self.coupon_button)

    # 点击海报按钮
    def click_poster_button(self):
        self.click(self.poster_button)

    # 点击拼团订单按钮
    def click_group_order_button(self):
        self.click(self.group_order_button)

    # 点击我的评价按钮
    def click_my_evaluation_button(self):
        self.click(self.my_evaluation_button)

    # 点击积分兑换按钮
    def click_points_exchange_button(self):
        self.click(self.points_exchange_button)

    # 点击我的签到按钮
    def click_my_signin_button(self):
        self.click(self.my_signin_button)

    # 点击领券中心按钮
    def click_coupon_center_button(self):
        self.click(self.coupon_center_button)

    # 点击我的收藏按钮
    def click_my_collection_button(self):
        self.click(self.my_collection_button)

    # 点击我的足迹按钮
    def click_my_track_button(self):
        self.click(self.my_track_button)

    # 点击我的消息按钮
    def click_my_message_button(self):
        self.click(self.my_message_button)

    # 点击地址管理按钮
    def click_address_management_button(self):
        self.click(self.address_management_button)