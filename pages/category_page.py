from selenium.webdriver.common.by import By
from AmazonProject.base import BaseClass

class AmazonCategory:
    """  Website login page for users to logging in """
    PAGES = (By.CLASS_NAME, 'a-normal')  # There will be more than 1 class with this name so. It should be a list.
    SELECTED = (By.XPATH, "//li[@class='a-selected']/a")
    PRODUCT_THIRD = (By.CLASS_NAME, ".s-result-item.s-asin")  # [2] will be  chosen
    PRODUCT_LIST = (By.CLASS_NAME,"a-size-medium")  # product lists on category page. need to get their text version.

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)  # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?


    def clicking_the_second_page(self):
        """
        Navigating to second page on the category page.

        """
        self.methods.wait_for_element(self.PAGES)[0].click()
        assert self.SELECTED.text in "2"


    def clicking_the_third_item(self):
        """
        Clicking the third item in the Product List.

        """
        self.methods.wait_for_element(self.PRODUCT_THIRD)[2].click()
