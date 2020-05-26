from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def input_text(self, loc, text):
        self.find_element(loc).send_keys(text)

    def click(self, loc):
        self.find_element(loc).click()

    def find_element(self, loc, timeout=5.0, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(loc[0], loc[1]))

    def find_elements(self, loc, timeout=5.0, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(loc[0], loc[1]))

    def is_toast_exist(self, message, is_screenshot=False, screenshot_name=None, timeout=3.0, poll=0.1):
        try:
            self.find_toast(message, is_screenshot, screenshot_name, timeout, poll)
            return True
        except:
            return False

    def find_toast(self, message, is_screenshot=False, screenshot_name=None, timeout=3.0, poll=0.1):
        message = '//*[contains(@text,"' + message + '")]'
        ele = self.find_element((MobileBy.XPATH, message), timeout, poll)
        if is_screenshot:
            self.screenshot(screenshot_name)
        return ele.text

    def screenshot(self, filename):
        self.driver.get_screenshot_as_file('screen/' + filename + '.png')

    def swipe_screen(self, direction):
        if direction == 'up':
            self.driver.swipe(400, 1000, 400, 100, 1000)
        elif direction == 'down':
            self.driver.swipe(400, 100, 400, 1000, 1000)
        elif direction == 'left':
            self.driver.swipe(700, 600, 100, 600, 1000)
        elif direction == 'right':
            self.driver.swipe(100, 600, 700, 600, 1000)