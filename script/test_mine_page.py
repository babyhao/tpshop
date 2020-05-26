import allure, pytest, os, sys

sys.path.append(os.getcwd())
from base.base_driver import get_driver
from base.base_yaml import data_with_key
from page.mine_page import MinePage
from page.category_page import CategoryPage
from page.search_page import SearchPage
from page.goods_list_page import GoodsListPage
from page.goods_info_page import GoodsInfoPage
from page.confirm_order_page import ConfirmOrderPage
from page.address_page import AddressPage


class TestMinePage:
    def setup(self):
        self.driver = get_driver()
        self.mine_page = MinePage(self.driver)
        self.mine_page.switch_to_mine_page()

    def teardown(self):
        self.driver.quit()

    @allure.step(title='测试登录的脚本')
    @pytest.mark.parametrize('args', data_with_key('test_login'))
    def test_login(self, args):
        username = args['username']
        password = args['password']
        toast = args['toast']
        screenshot_name = username + '_login'
        # 输入用户名
        allure.attach('', '输入用户名')
        self.login_page.input_username(username)
        # 输入密码
        allure.attach('', '输入密码')
        self.login_page.input_password(password)
        # 点击登录按钮
        allure.attach('', '点击登录按钮')
        self.login_page.click_login()
        # 判断是否登录成功
        allure.attach(toast, '判断是否登录成功')
        res = self.login_page.is_toast_exist(toast, True, screenshot_name)
        # 上传截图
        allure.attach(open('screen/' + screenshot_name + '.png', 'rb').read(), '截图', allure.attachment_type.PNG)
        assert res