from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class AmazonLogin:
    """
        Logging into the account & filling the needed information.

    """
    EMAIL_DATA = 'alpaylui78@gmail.com'
    PASSWORD_DATA = '---'
    EMAIL = (By.ID, 'ap_email')
    PASS_EMAIL = (By.ID, 'continue')
    PASSWORD = (By.ID, 'ap_password')
    PASS_PASSWORD = (By.ID, 'signInSubmit')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def login_into_account(self):
        """Logging into the account & filling the needed information."""

        self.methods.wait_for_element(self.EMAIL, 0).send_keys(self.EMAIL_DATA)
        self.methods.click_the_element(self.PASS_EMAIL, 0)
        self.methods.wait_for_element(self.PASSWORD, 0).send_keys(self.PASSWORD_DATA)
        self.methods.click_the_element(self.PASS_PASSWORD, 0)
