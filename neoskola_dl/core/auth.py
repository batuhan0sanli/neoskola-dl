from neoskola_dl.core.driver import Driver
from neoskola_dl.constants import Constants


class Auth:
    def __init__(self, email=None, password=None, token=None, config=Constants()):
        self.email = email
        self.password = password
        self.token = token
        self.config = config
        self.driver = Driver(self.config)

    def login(self):
        with self.driver as driver:
            if self.email and self.password:
                driver.new_token(self.email, self.password)
            elif self.token:
                driver.token = self.token
            else:
                raise Exception("Email and Password or Token is required.")

    def logout(self):
        with self.driver as driver:
            driver.get(self.config.logout_url)  # This url expires the token
            del driver.token  # Delete the expired token from the driver

    def is_login(self):
        with self.driver as driver:
            return driver.is_login()
