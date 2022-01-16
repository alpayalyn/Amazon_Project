from selenium.webdriver.common.by import By
from AmazonProject.base import BaseClass  # Thanks to this importing process, I can benefit from the methods defined in BaseClass.

class AmazonWishlist:
    """Website login page for users to logging in"""
    DELETE_BUTTON = (By.NAME, "submit.deleteItem")[0]
    PRODUCT_LIST = []
    ITEMS_LIST = (By.XPATH, "//h2/a[@class='a-link-normal']") # Items listed in the wishlist
    CHOSEN_PRODUCT_NAME_WISHLIST_NAME = (By.XPATH, "//h2/a[@class='a-link-normal']")[0]

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)  # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?

    def deleting_the_product(self):
        self.methods.wait_for_element(self.DELETE_BUTTON).click()

    def deleting_validation(self):
        self.PRODUCT_LIST = self.methods.wait_for_element(self.ITEMS_LIST).text
        for product in self.PRODUCT_LIST:
            if product == self.methods.wait_for_element(self.CHOSEN_PRODUCT_NAME_WISHLIST_NAME):
                assert False, "Product couldn't be deleted"
        assert True


