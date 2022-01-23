from selenium.webdriver.common.by import By
from base.base_page import BaseClass

class AmazonHome:
    """  The class lands on the HomePage - validates its actually on the Homepage & directs you to Login Page. """
    LOGIN_SCREEN = (By.ID, "nav-link-accountList")
    BASE_URL = "https://www.amazon.com"

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)  # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?

    def home_page_loaded_successfully(self):
        """
        Navigates to the Home Page
        """
        self.methods.driver.get(self.BASE_URL)  # Open the web page

    def navigating_to_login_page(self):
        """
        Website navigates to the login page.
        """
        self.methods.wait_for_element(self.LOGIN_SCREEN).click()
