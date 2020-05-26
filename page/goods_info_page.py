import sys, os

sys.path.append(os.getcwd())
from appium.webdriver.common.mobileby import MobileBy
from base.base_action import BaseAction


class GoodsInfoPage(BaseAction):
    back_img = MobileBy.ID, 'com.tpshop.malls:id/back_ll'
    goods_tab = MobileBy.ANDROID_UIAUTOMATOR, 'text("商品")'
    details_tab = MobileBy.ANDROID_UIAUTOMATOR, 'text("详情")'
    comments_tab = MobileBy.ANDROID_UIAUTOMATOR, 'text("评价")'
    collect_img = MobileBy.ID, 'com.tpshop.malls:id/collect_img'
    specification_button = MobileBy.ID, 'com.tpshop.malls:id/current_spec_tv'
    version_3G_radio = MobileBy.ANDROID_UIAUTOMATOR, 'textContains("全网通3G")'
    version_4G_radio = MobileBy.ANDROID_UIAUTOMATOR, 'textContains("全网通4G")'
    minus_button = MobileBy.ID, 'com.tpshop.malls:id/cart_minus_btn'
    plus_button = MobileBy.ID, 'com.tpshop.malls:id/cart_plus_btn'
    # buy_now_button = MobileBy.ID, 'com.tpshop.malls:id/promptly_buy_tv' # 商品主页的立即购买按钮
    buy_now_button = MobileBy.ID, 'com.tpshop.malls:id/buy_tv' # 商品规格页的立即购买按钮
    address_button = MobileBy.ID, 'com.tpshop.malls:id/send_address_ll'
    customer_service_button = MobileBy.ID, 'com.tpshop.malls:id/service_ll1'
    shopping_cart_button = MobileBy.XPATH, '//*[@text="shopping cart"]/..'
    add_to_shopping_cart_button = MobileBy.ID, 'com.tpshop.malls:id/add_cart_tv'
    confirm_button = MobileBy.ID, 'com.tpshop.malls:id/confirm_tv'

    def __init__(self, driver):
        super().__init__(driver)

    # 返回
    def click_back_img(self):
        self.click(self.back_img)

    # 顶部切换到“商品”
    def click_goods_tab(self):
        self.click(self.goods_tab)

    # 顶部切换到“详情”
    def click_details_tab(self):
        self.click(self.details_tab)

    # 顶部切换到“评价”
    def click_comments_tab(self):
        self.click(self.comments_tab)

    # 左右滑动轮播图
    def swipe_slideshow(self, direction):
        if direction == 'left':
            self.driver.swipe(700, 300, 100, 300, 1000)
        elif direction == 'right':
            self.driver.swipe(100, 300, 700, 300, 1000)

    # 收藏
    def click_collect_img(self):
        self.click(self.collect_img)

    # 选择规格
    def click_specification_button(self):
        self.click(self.specification_button)

    # 选择全网通3G版
    def click_version_3G_radio(self):
        self.click(self.version_3G_radio)

    # 选择全网通4G版
    def click_version_4G_radio(self):
        self.click(self.version_4G_radio)

    # 数量减1
    def click_minus_button(self):
        self.click(self.minus_button)

    # 数量加1
    def click_plus_button(self):
        self.click(self.plus_button)

    # 选择收获地址
    def click_address_button(self):
        self.click(self.address_button)

    # 点击客户服务
    def click_customer_service_button(self):
        self.click(self.customer_service_button)

    # 查看购物车
    def click_shopping_cart_button(self):
        self.click(self.shopping_cart_button)

    # 加入购物车
    def click_add_to_shopping_cart_button(self):
        self.click(self.add_to_shopping_cart_button)

    # 点击规格页的确定
    def click_confirm_button(self):
        self.click(self.confirm_button)

    # 立即购买
    def click_buy_now_button(self):
        self.click(self.buy_now_button)