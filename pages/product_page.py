from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class AmazonProduct:
    """
        Get the text of third product
        Clicking the Add to List button on the product page.
        Clicking the Shopping List button on the Wishlist frame.

    """
    ADD_TO_LIST_BUTTON = (By.ID, 'wishlistButtonStack')
    WISH_LIST_LINK = (By.ID, "WLHUC_result_listName")
    CHOSEN_PRODUCT_NAME = (By.ID, "productTitle")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def getting_the_product_name_text(self):
        """Get the text of third product."""

        self.methods.get_text(self.CHOSEN_PRODUCT_NAME, 0)

    def clicking_add_to_list(self):
        """Clicking the Add to List button on the product page."""

        self.methods.click_the_element(self.ADD_TO_LIST_BUTTON, 0)

    def clicking_the_list(self):
        """Clicking the Shopping List button on the Wishlist frame."""

        self.methods.click_the_element(self.WISH_LIST_LINK, 0)
