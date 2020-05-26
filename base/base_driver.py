from appium import webdriver

def get_driver():
    caps = {
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'platformVersion': '6.0',
        'deviceName': 'abc',
        'appPackage': 'com.tpshop.malls',
        'appActivity': '.SPMainActivity',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
    return driver