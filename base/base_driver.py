from appium import webdriver

def get_driver():
    caps = {
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'platformVersion': '9.0',
        'deviceName': 'Phone_9.0_28',
        'appPackage': 'com.tpshop.malls',
        'appActivity': '.SPMainActivity',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        # 'noReset': True
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
    return driver