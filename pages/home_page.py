from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class AmazonHome:
    """

        Navigates users to the Login Screen.

    """
    LOGIN_SCREEN = (By.ID, "nav-link-accountList")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def navigating_to_login_page(self):
        """Website navigates to the login page."""
        self.methods.click_the_element(self.LOGIN_SCREEN, 0)
