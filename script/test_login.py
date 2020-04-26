import allure, pytest, os, sys

sys.path.append(os.getcwd())

from base.base_driver import get_driver
from page.login_page import LoginPage
from base.base_yaml import get_yaml_data

def data_with_key(key):
    return get_yaml_data('login_data', key)


class TestLogin:
    def setup(self):
        self.driver = get_driver()
        self.login_page = LoginPage(self.driver)

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
        allure.attach(username, '输入用户名')
        self.login_page.input_username(username)
        # 输入密码
        allure.attach(password, '输入密码')
        self.login_page.input_password(password)
        # 点击登录按钮
        allure.attach('', '点击登录按钮')
        self.login_page.click_login()
        # 判断是否登录成功
        allure.attach(toast, '判断是否登录成功')
        res = self.login_page.is_toast_exist(toast, True, screenshot_name)
        allure.attach(open('screen/' + screenshot_name + '.png', 'rb').read(), '截图', allure.attachment_type.PNG)
        assert res