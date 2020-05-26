import allure, pytest, os, sys

sys.path.append(os.getcwd())
from base.base_driver import get_driver
from base.base_yaml import data_with_key
from page.first_page import FirstPage
from page.search_page import SearchPage
from page.goods_info_page import GoodsInfoPage


# 获取搜索关键字
def get_search_data():
    dict_values = data_with_key('test_search')
    for data in dict_values:
        return data


class TestFirstPage:
    def setup(self):
        self.driver = get_driver()
        self.first_page = FirstPage(self.driver)
        self.first_page.switch_to_first_page()

    def teardown(self):
        self.driver.quit()

    @allure.step(title='测试：首页的搜索功能')
    @pytest.mark.parametrize('arg', get_search_data())
    def test_search(self, arg):
        allure.attach('', '点击搜索框')
        self.first_page.click_search_box()
        allure.attach('', '输入搜索内容')
        self.search_page = SearchPage(self.driver)
        self.search_page.input_search_text(arg)
        allure.attach('', '点击“search for”')
        self.search_page.click_search_for_button()
        allure.attach('', '检查是否跳转到搜索结果页，有截图')
        res = self.first_page.is_toast_exist('Comprehensive', True, '搜索结果页')
        assert res

    @allure.step(title='测试：点击首页的“消息中心”图标时，页面是否正确跳转')
    def test_message_center_button(self):
        allure.attach('', '点击"小心中心"图标')
        self.first_page.click_message_center_button()
        allure.attach('', '检查是否跳转到消息中心页，有截图')
        res = self.first_page.is_toast_exist('通知', True, '消息中心页')
        assert res

    @allure.step(title='测试：轮播图功能')
    def test_slideshow(self):
        # allure.attach('', '向左滑')
        # self.first_page.swipe_slideshow('left')
        # allure.attach('', '向右滑')
        # self.first_page.swipe_slideshow('right')
        # allure.attach('', '点击轮播图导航图标')
        # self.first_page.click_slideshow_dot(2)
        allure.attach('', '点击图片')
        self.first_page.click_slideshow()
        allure.attach('', '检查是否跳转到对应的商品购买页，有截图')
        res = self.first_page.is_toast_exist('Buy now', True, '轮播图商品购买页')
        assert res

    @allure.step(title='测试：点击“全部分类”时，是否正确切换到“分类”模块')
    def test_all_cates_button(self):
        allure.attach('', '点击“全部分类”图标')
        self.first_page.click_all_cates_button()
        allure.attach('', '检查是否切换到“分类”模块，有截图')
        res = self.first_page.is_toast_exist('服饰', True, '分类页')
        assert res

    @allure.step(title='测试：点击“Points Mall”图标时，页面是否正确跳转')
    def test_points_mall_button(self):
        allure.attach('', '点击"Points Mall"图标')
        self.first_page.click_points_mall_button()
        allure.attach('', '检查是否跳转到积分兑换页，有截图')
        res = self.first_page.is_toast_exist('积分值', True, '积分兑换页')
        assert res

    @allure.step(title='测试：点击“Brand street”图标时，页面是否正确跳转')
    def test_brand_street_button(self):
        allure.attach('', '点击"Brand street"图标')
        self.first_page.click_brand_street_button()
        allure.attach('', '检查是否跳转到品牌页，有截图')
        res = self.first_page.is_toast_exist('推荐大牌', True, '品牌页')
        assert res

    @allure.step(title='测试：点击“Product promotion”图标时，页面是否正确跳转')
    def test_product_promotion_button(self):
        allure.attach('', '点击"Product promotion"图标')
        self.first_page.click_product_promotion_button()
        allure.attach('', '检查是否跳转到优惠活动页，有截图')
        res = self.first_page.is_toast_exist('优惠活动', True, '优惠活动页')
        assert res

    @allure.step(title='测试：点击“Group buy”图标时，页面是否正确跳转')
    def test_group_buy_button(self):
        allure.attach('', '点击"Group buy"图标')
        self.first_page.click_group_buy_button()
        allure.attach('', '检查是否跳转到团购页，有截图')
        res = self.first_page.is_toast_exist('Buy today', True, '团购页')
        assert res

    @allure.step(title='测试：点击“Coupon center”图标时，页面是否正确跳转')
    def test_coupon_center_button(self):
        allure.attach('', '点击"Coupon center"图标')
        self.first_page.click_coupon_center_button()
        allure.attach('', '检查是否跳转到优惠券页，有截图')
        res = self.first_page.is_toast_exist('精选', True, '优惠券页')
        assert res

    @allure.step(title='测试：点击“i want to fight”图标时，页面是否正确跳转')
    def test_i_want_to_fight_button(self):
        allure.attach('', '点击"i want to fight"图标')
        self.first_page.click_i_want_to_fight_button()
        allure.attach('', '检查是否跳转到拼团活动页，有截图')
        res = self.first_page.is_toast_exist('拼团活动', True, '拼团活动页')
        assert res

    @allure.step(title='测试：点击“User center”图标时，是否正确切换到“我的”模块')
    def test_user_center_button(self):
        allure.attach('', '点击"User center"图标')
        self.first_page.click_user_center_button()
        allure.attach('', '检查是否切换到“我的”模块，有截图')
        res = self.first_page.is_toast_exist('余额', True, '用户中心页')
        assert res

    @allure.step(title='测试：点击“限时抢购”图标时，页面是否正确跳转')
    def test_flash_sale_button(self):
        allure.attach('', '点击"限时抢购"图标')
        self.first_page.click_flash_sale_button()
        allure.attach('', '检查是否切换到限时抢购页面，有截图')
        res = self.first_page.is_toast_exist('即将开场', True, '限时抢购页')
        assert res

    @allure.step(title='测试：从热卖产品板块选择一样商品加入购物车')
    def test_add_to_cart(self):
        allure.attach('', '选择客邻尚品')
        self.first_page.click_hot_sale_goods()
        allure.attach('', '查看详情页')
        self.goods_info_page = GoodsInfoPage(self.driver)
        self.goods_info_page.click_details_tab()
        allure.attach('', '查看商品评价')
        self.goods_info_page.click_comments_tab()
        allure.attach('', '回到商品购买页')
        self.goods_info_page.click_goods_tab()
        allure.attach('', '点击收藏')
        self.goods_info_page.click_collect_img()
        allure.attach('', '加入购物车')
        self.goods_info_page.click_add_to_shopping_cart_button()
        allure.attach('', '选择规格页面的确定')
        self.goods_info_page.click_confirm_button()
        allure.attach('', '检查是否成功加入购物车')
        res = self.first_page.is_toast_exist('加入购物车成功', True, '加入购物车')
        assert res