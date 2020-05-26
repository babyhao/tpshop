import sys, os

sys.path.append(os.getcwd())
from appium.webdriver.common.mobileby import MobileBy
from base.base_action import BaseAction


class GoodsListPage(BaseAction):
    back_img = MobileBy.ID, 'com.tpshop.malls:id/title_back_img'
    show_style_img = MobileBy.ID, 'com.tpshop.malls:id/show_style_iv'
    rank_button = MobileBy.ID, 'com.tpshop.malls:id/sort_composite_tv'
    comprehensive_rank_option = MobileBy.ANDROID_UIAUTOMATOR, 'text("综合排序")'
    new_product_first_option = MobileBy.ANDROID_UIAUTOMATOR, 'text("新品优先")'
    comments_order_option = MobileBy.ANDROID_UIAUTOMATOR, 'textContains("评论数")'
    sales_volume_button = MobileBy.ID, 'ccom.tpshop.malls:id/sort_sale_num_tv'
    price_button = MobileBy.ID, 'com.tpshop.malls:id/sort_price_tv'
    filter_button = MobileBy.ID, 'com.tpshop.malls:id/sort_filter_tv'
    threeG_option = MobileBy.ANDROID_UIAUTOMATOR, 'textContains("全网通3G")'
    fourG_option = MobileBy.ANDROID_UIAUTOMATOR, 'textContains("全网通4G")'
    official_standard_option = MobileBy.ANDROID_UIAUTOMATOR, 'text("官方标配")'
    combo_one_option = MobileBy.ANDROID_UIAUTOMATOR, 'text("套餐一")'
    combo_two_option = MobileBy.ANDROID_UIAUTOMATOR, 'text("套餐二")'
    color_one_option = MobileBy.ANDROID_UIAUTOMATOR, 'text("铂光色")'
    color_two_option = MobileBy.ANDROID_UIAUTOMATOR, 'text("极光色")'
    color_three_option = MobileBy.ANDROID_UIAUTOMATOR, 'text("幻夜色")'
    price_one_option = MobileBy.ANDROID_UIAUTOMATOR, 'text("1198元以下")'
    price_two_option = MobileBy.ANDROID_UIAUTOMATOR, 'text("1198-2396元")'
    price_three_option = MobileBy.ANDROID_UIAUTOMATOR, 'text("2396-3594元")'
    price_four_option = MobileBy.ANDROID_UIAUTOMATOR, 'text("4792-5990元")'
    changwan6 = MobileBy.ANDROID_UIAUTOMATOR, 'textContains("畅玩6").fromParent(className("android.widget.ImageView"))'

    def __init__(self, driver):
        super().__init__(driver)

    # 返回
    def click_back_img(self):
        self.click(self.back_img)

    # 切换显示模式
    def click_show_style_img(self):
        self.click(self.show_style_img)

    # 选择排序方式
    def click_rank_button(self):
        self.click(self.rank_button)

    # 选择综合排序
    def click_comprehensive_rank_option(self):
        self.click(self.comprehensive_rank_option)

    # 选择新品优先
    def click_new_product_first_option(self):
        self.click(self.new_product_first_option)

    # 选择按评论数从多到少排序
    def click_comments_order_option(self):
        self.click(self.comments_order_option)

    # 选择按销量排序
    def click_sales_volume_button(self):
        self.click(self.sales_volume_button)

    # 切换按售价排序
    def click_price_button(self):
        self.click(self.price_button)

    # 点击过滤器按钮
    def click_filter_button(self):
        self.click(self.filter_button)

    # 选择全网通3G
    def click_threeG_option(self):
        self.click(self.threeG_option)

    # 选择全网通4G
    def click_fourG_option(self):
        self.click(self.fourG_option)

    # 选择官方标配
    def click_official_standard_option(self):
        self.click(self.official_standard_option)

    # 选择套餐一
    def click_combo_one_option(self):
        self.click(self.combo_one_option)

    # 选择套餐二
    def click_combo_two_option(self):
        self.click(self.combo_two_option)

    # 选择铂光色
    def click_color_one_option(self):
        self.click(self.color_one_option)

    # 选择极光色
    def click_color_two_option(self):
        self.click(self.color_two_option)

    # 选择幻夜色
    def click_color_three_option(self):
        self.click(self.color_three_option)

    # 选择1198元以下
    def click_price_one_option(self):
        self.click(self.price_one_option)

    # 选择1198-2396元
    def click_price_two_option(self):
        self.click(self.price_two_option)

    # 选择2396-3594元
    def click_price_three_option(self):
        self.click(self.price_three_option)

    # 选择4792-5990元
    def click_price_four_option(self):
        self.click(self.price_four_option)

    # 选择荣耀畅玩6
    def choose_goods(self):
        self.click(self.changwan6)