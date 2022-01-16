from selenium.webdriver.common.by import By
from AmazonProject.base import BaseClass


class AmazonProduct:
    """Website product page for adding the item to your WishList"""

    ADD_TO_LIST_BUTTON = (By.ID, 'wishlistButtonStack')
    WISH_LIST_LINK = (By.ID, "WLHUC_result_listName")
    CHOSEN_PRODUCT_NAME = (By.ID, "productTitle")
    CHOSEN_PRODUCT_NAME_WISHLIST = (By.XPATH, "//h2/a[@class='a-link-normal']")[0]

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)  # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?

    def adding_product(self):
        """
        Clicking the Add to List & the clicking the link which redirects you to the Wish List.
        """
        CHOSEN_PRODUCT_NAME_TEXT = self.CHOSEN_PRODUCT_NAME.text
        self.methods.wait_for_element(self.WISH_LIST).click()
        self.methods.wait_for_element(self.WISH_LIST_LINK).click()
        assert CHOSEN_PRODUCT_NAME_TEXT in self.methods.wait_for_element(self.CHOSEN_PRODUCT_NAME_WISHLIST).text, 'Item you added, couldnt be added successfully.'
