from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver):
        self.driver = driver

    def base_get_element(self, loc, timeout=30, poll=0.5):

        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda X: X.find_element(*loc))

    def base_click(self, loc):
        self.base_get_element(loc).click()

    def base_input(self, loc, text):
        self.base_get_element(loc).send_keys(text)
