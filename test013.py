from appium import webdriver
#
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
battery=driver.find_element_by_xpath("//*[@text='电池']")









driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)