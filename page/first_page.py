import os, sys

sys.path.append(os.getcwd())
from base.base_action import BaseAction
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class FirstPage(BaseAction):
    first_page_tab = MobileBy.ID, 'com.tpshop.malls:id/home_ll'
    search_box_xy = 400, 100
    message_center_img_xy = 725, 95
    slideshow = MobileBy.ID, 'com.tpshop.malls:id/sdv_item_head_img'
    slideshow_dot_xy = (372, 369), (393, 369)
    all_cates_button = MobileBy.ID, 'com.tpshop.malls:id/home_menu_category_layout'
    points_mall_button = MobileBy.ID, 'com.tpshop.malls:id/home_menu_integral_layout'
    brand_street_button = MobileBy.ID, 'com.tpshop.malls:id/home_menu_brand_layout'
    product_promotion_button = MobileBy.ID, 'com.tpshop.malls:id/home_menu_promote_layout'
    group_buy_button = MobileBy.ID, 'com.tpshop.malls:id/home_menu_group_layout'
    coupon_center_button = MobileBy.ID, 'com.tpshop.malls:id/home_menu_coupon_layout'
    i_want_to_fight_button = MobileBy.ID, 'com.tpshop.malls:id/home_menu_fightGroup_layout'
    user_center_button = MobileBy.ID, 'com.tpshop.malls:id/home_menu_user_layout'
    flash_sale_button = MobileBy.ID, 'com.tpshop.malls:id/flash_more_ll'
    hot_sale_goods = MobileBy.XPATH, '//*[contains(@text,"客邻尚品")]/..'


    def __init__(self, driver):
        super().__init__(driver)

    # 进入“首页”
    def switch_to_first_page(self):
        self.click(self.first_page_tab)

    # 点击搜索框
    def click_search_box(self):
        x = self.search_box_xy[0]
        y = self.search_box_xy[1]
        TouchAction(self.driver).tap(x=x, y=y).perform()

    # 点击“消息中心”
    def click_message_center_button(self):
        x = self.message_center_img_xy[0]
        y = self.message_center_img_xy[1]
        TouchAction(self.driver).tap(x=x, y=y).perform()

    # 左右滑动轮播图
    def swipe_slideshow(self, direction):
        if direction == 'left':
            self.driver.swipe(700, 200, 100, 200, 1000)
        elif direction == 'right':
            self.driver.swipe(100, 200, 700, 200, 1000)

    # 点击轮播图导航，num从1开始
    def click_slideshow_dot(self, num):
        x = self.slideshow_dot_xy[num-1][0]
        y = self.slideshow_dot_xy[num-1][1]
        TouchAction(self.driver).tap(x=x, y=y).perform()

    # 点击轮播图图片
    def click_slideshow(self):
        self.click(self.slideshow)

    # 点击“全部分类”
    def click_all_cates_button(self):
        self.click(self.all_cates_button)

    # 点击“Points Mall”图标
    def click_points_mall_button(self):
        self.click(self.points_mall_button)

    # 点击“Brand street”
    def click_brand_street_button(self):
        self.click(self.brand_street_button)

    # 点击“Product promotion”
    def click_product_promotion_button(self):
        self.click(self.product_promotion_button)

    # 点击“Group buy”
    def click_group_buy_button(self):
        self.click(self.group_buy_button)

    # 点击“Coupon center”
    def click_coupon_center_button(self):
        self.click(self.coupon_center_button)

    # 点击“I want to fight”
    def click_i_want_to_fight_button(self):
        self.click(self.i_want_to_fight_button)

    # 点击“User center”
    def click_user_center_button(self):
        self.click(self.user_center_button)

    # 点击“限时抢购”
    def click_flash_sale_button(self):
        self.click(self.flash_sale_button)

    # 选择某热卖商品
    def click_hot_sale_goods(self):
        self.click(self.hot_sale_goods)