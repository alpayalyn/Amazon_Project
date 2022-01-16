from selenium.webdriver.common.by import By
from AmazonProject.base import BaseClass

class AmazonSearch:
    """Website Search Page is for 'samsung' text to be searched in the search bar."""
    TEXT_TO_BE_SEARCHED = 'samsung'
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    SEARCH_RESULTS = (By.CLASS_NAME, ".a-color-state.a-text-bold")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)  # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?

    def texting_samsung_in_searchbar(self):
        """
        This function is used to search for 'samsung' text and click the search button.
        """
        assert self.methods.wait_for_element(self.SEARCH_RESULTS).text in "samsung"
        self.methods.wait_for_element(self.SEARCH_BOX).send_keys(self.TEXT_TO_BE_SEARCHED)
        self.methods.wait_for_element(self.SEARCH_BUTTON).click()
