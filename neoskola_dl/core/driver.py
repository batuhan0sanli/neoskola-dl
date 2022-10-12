import time
from selenium import webdriver


class Driver:
    def __init__(self, config):
        self.chrome_driver_path = config.chrome_driver_path
        self.chrome_options = config.chrome_options
        self.main_url = config.main_url
        self.driver = None
        self._token = None

    def __enter__(self):
        if self.driver is None:
            self.driver = webdriver.Chrome(self.chrome_driver_path, chrome_options=self.chrome_options)
            self.get(self.main_url)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.driver.close()
        self.driver.quit()
        self.driver = None

    def _authenticate(self):
        # todo: Bunu yalnızca login olunca yapılmalı.
        self.driver.execute_script("window.localStorage.setItem('Meteor.loginToken', '{}');".format(self._token))
        self.driver.implicitly_wait(5)
        return self.driver.execute_script("return window.localStorage.getItem('Meteor.loginToken');")

    def _is_token_exists(self):
        if self._token is None:
            return False
        return True

    def is_login(self):
        if self.driver and len(self.driver.find_elements("id", "profile-fields")) > 0:
            return True
        return False

    def get(self, url):
        self.driver.get(url)
        if self._is_token_exists():
            self._authenticate()

    @property
    def token(self):
        if self.driver is None or self.driver.current_url == 'data:,':
            return self._token
        return self.driver.execute_script("return window.localStorage.getItem('Meteor.loginToken');")

    @token.setter
    def token(self, token):
        self._token = token
        if self.driver is None:
            return
        self.driver.execute_script("window.localStorage.setItem('Meteor.loginToken', '{}');".format(token))

    @token.deleter
    def token(self):
        self._token = None
        if self.driver is None:
            return
        self.driver.execute_script("window.localStorage.removeItem('Meteor.loginToken');")

    def new_token(self, email, password):
        self.driver.get(self.main_url)
        time.sleep(1)
        self.driver.find_element("id", "top-login").click()
        self.driver.find_element("name", "emailAddress").send_keys(email)
        self.driver.find_element("name", "password").send_keys(password)
        time.sleep(1)
        self.driver.find_element("name", "password").submit()
        time.sleep(3)
        # todo: add invalid username or password check
        self.token = self.driver.execute_script("return window.localStorage.getItem('Meteor.loginToken');")
        return self.token
