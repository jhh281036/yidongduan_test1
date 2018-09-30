from time import sleep

from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'

desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



driver.tap([(356, 940), (360, 2033)], 1000)

sleep(3)
driver.quit()
