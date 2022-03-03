from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class AmazonWishlist:
    """

        Get the text of recently added item into the Shopping List.
        Deleting recently added item from the Shopping List.
        After deleting the item, getting 'Undo' text for assertion.

    """
    DELETE_BUTTON = (By.NAME, "submit.deleteItem")
    DELETED_ITEM_TEXT = (By.CSS_SELECTOR, "span[id='undo-delete']")
    CHOSEN_PRODUCT_NAME_WISHLIST_NAME = (By.XPATH, "//h2/a[@class='a-link-normal']")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def getting_the_product_name_text(self):
        """Get the text of recently added item into the Shopping List."""

        self.methods.get_text(self.CHOSEN_PRODUCT_NAME_WISHLIST_NAME, 0)

    def deleting_the_product(self):
        """Deleting recently added item from the Shopping List."""

        self.methods.click_the_element(self.DELETE_BUTTON, 0)

    def getting_the_text_after_delete(self):
        """After deleting the item, getting 'Undo' text for assertion."""

        return self.methods.get_text(self.DELETED_ITEM_TEXT, 0)
