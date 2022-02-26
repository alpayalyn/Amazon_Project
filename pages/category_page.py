from selenium.webdriver.common.by import By
from base.base_page import BaseClass
from selenium.webdriver.support.ui import WebDriverWait


class AmazonCategory:
    """
        Scrolling down on the page & navigating to second page on the category page.
        Returning the text of the Page 'Second' to be able to validate.
        Clicking the third item in the category page.

    """
    SECOND_PAGE = (By.CLASS_NAME, 's-pagination-button')
    SELECTED_PAGE = (By.CLASS_NAME, "s-pagination-selected")
    PRODUCT_THIRD = (By.CSS_SELECTOR, ".s-link-style.a-text-normal")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def clicking_the_second_page(self):
        """Scrolling down on the page & navigating to second page on the category page."""

        self.methods.scrolling_the_page(2000)
        self.methods.click_the_element(self.SECOND_PAGE, 0)

    def getting_the_second_page_text(self):
        """Returning the text of the Page 'Second' to be able to validate."""

        return self.methods.get_text(self.SELECTED_PAGE, 0)

    def clicking_the_third_product(self):
        """Clicking the third item in the category page."""

        self.methods.click_the_element(self.PRODUCT_THIRD, 4)
