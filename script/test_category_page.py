import allure, pytest, os, sys

sys.path.append(os.getcwd())
from base.base_driver import get_driver
from base.base_yaml import data_with_key
from page.category_page import CategoryPage
from page.search_page import SearchPage
from page.goods_list_page import GoodsListPage
from page.goods_info_page import GoodsInfoPage
from page.confirm_order_page import ConfirmOrderPage
from page.address_page import AddressPage


def get_search_data():
    dict_values = data_with_key('test_search')
    for data in dict_values:
        return data


class TestCategoryPage:
    def setup(self):
        self.driver = get_driver()
        self.category_page = CategoryPage(self.driver)
        self.category_page.switch_to_category_page()

    def teardown(self):
        self.driver.quit()

    @allure.step(title='测试：分类页的搜索功能')
    @pytest.mark.parametrize('arg', get_search_data())
    def test_search(self, arg):
        allure.attach('', '点击搜索框')
        self.category_page.click_search_box()
        allure.attach('', '输入搜索内容')
        self.search_page = SearchPage(self.driver)
        self.search_page.input_search_text(arg)
        allure.attach('', '开始搜索')
        self.search_page.click_search_for_button()
        allure.attach('', '检查是否跳转到搜索结果页，有截图')
        res = self.category_page.is_toast_exist('Comprehensive', True, '搜索结果页')
        assert res

    @allure.step(title='测试：点击分类页的“消息中心”图标时，页面是否正确跳转')
    def test_message_center_button(self):
        allure.attach('', '点击消息中心')
        self.category_page.click_message_center_img()
        allure.attach('', '检查是否跳转到消息中心页，有截图')
        res = self.category_page.is_toast_exist('通知', True, '消息中心页')
        assert res

    @allure.step(title='测试：左侧商品类目标签能否正常切换')
    def test_toggle_category(self):
        allure.attach('', '点击服饰标签')
        self.category_page.click_clothes_tab()
        allure.attach('', '检查是否展示服饰类商品')
        assert self.category_page.is_toast_exist('牛仔裤')
        allure.attach('', '点击电脑标签')
        self.category_page.click_computer_tab()
        allure.attach('', '检查是否展示电脑类商品')
        assert self.category_page.is_toast_exist('一体机')
        allure.attach('', '点击家居标签')
        self.category_page.click_household_tab()
        allure.attach('', '检查是否展示家居类商品')
        assert self.category_page.is_toast_exist('保温杯')
        allure.attach('', '点击鞋类标签')
        self.category_page.click_shoes_tab()
        allure.attach('', '检查是否展示鞋类商品')
        assert self.category_page.is_toast_exist('休闲鞋')
        allure.attach('', '点击手机标签')
        self.category_page.click_cellphone_tab()
        allure.attach('', '检查是否展示手机类商品')
        assert self.category_page.is_toast_exist('游戏手机')

    @allure.step(title='测试：从分类页选购商品的业务流程')
    def test_buy_something(self):
        allure.attach('', '点击手机标签中的手机数码类目')
        self.category_page.click_cellphone_goods()
        allure.attach('', '选择荣耀畅玩6')
        self.goods_list_page = GoodsListPage(self.driver)
        self.goods_list_page.swipe_screen('up')
        self.goods_list_page.choose_goods()
        allure.attach('', '查看商品详情')
        self.goods_info_page = GoodsInfoPage(self.driver)
        self.goods_info_page.click_details_tab()
        allure.attach('', '查看评价')
        self.goods_info_page.click_comments_tab()
        allure.attach('', '返回商品购买页')
        self.goods_info_page.click_goods_tab()
        allure.attach('', '收藏商品')
        self.goods_info_page.click_collect_img()
        allure.attach('', '选择规格')
        self.goods_info_page.click_specification_button()
        allure.attach('', '选择全网通4G版')
        self.goods_info_page.click_version_4G_radio()
        allure.attach('', '数量加1')
        self.goods_info_page.click_plus_button()
        allure.attach('', '立即购买')
        self.goods_info_page.click_buy_now_button()
        allure.attach('', '选择收获地址')
        self.confirm_order_page = ConfirmOrderPage(self.driver)
        self.confirm_order_page.click_address_button()
        allure.attach('', '选择nero的地址')
        self.address_page = AddressPage(self.driver)
        self.address_page.click_address_of_nero_button()
        allure.attach('', '提交订单')
        self.confirm_order_page.click_submit_orders_button()
        res = self.category_page.is_toast_exist('支付方式', True, '立即支付页')
        assert res