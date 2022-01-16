from selenium.webdriver.common.by import By
from AmazonProject.base import BaseClass

class AmazonLogin:
    """Website login page for users to logging in"""
    email = 'alpaylui78@gmail.com'
    password = 'Zemmenilone123'
    EMAIL = (By.ID, 'ap_email')
    PASS_EMAIL = (By.ID, 'continue')
    PASSWORD = (By.ID, 'ap_password')
    PASS_PASSWORD = (By.ID, 'signInSubmit')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def login_into_account(self):
        """
        Logging into the account.
        Filling the needed informations.
        """
        sleep(2)
        self.methods.wait_for_element(self.EMAIL).send_keys(self.email)
        self.methods.wait_for_element(self.PASS_EMAIL).click()
        self.methods.wait_for_element(self.PASSWORD).send_keys(self.password)
        self.methods.wait_for_element(self.PASS_PASSWORD).click()



