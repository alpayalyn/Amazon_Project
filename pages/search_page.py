from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class AmazonSearch:
    """
        Website Search Page is for 'samsung' text to be searched in the search bar.

    """
    TEXT_TO_BE_SEARCHED = 'Samsung'
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    SEARCH_RESULTS = (By.CLASS_NAME, "a-color-state")
    SAMSUNG_TEXT = (By.CSS_SELECTOR, ".a-size-medium.a-color-base.a-text-normal")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def texting_samsung_in_searchbar(self):
        """Text will be written in the Searchbar & Button will be clicked."""

        self.methods.wait_for_element(self.SEARCH_BOX, 0).send_keys(self.TEXT_TO_BE_SEARCHED)
        self.methods.click_the_element(self.SEARCH_BUTTON, 0)

    def searchbar_result(self):
        """Searched text will be checked on the page"""

        return self.methods.get_text(self.SAMSUNG_TEXT, 0)
