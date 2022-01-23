from selenium.webdriver.common.by import By
from base.base_page import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec


class AmazonCategory:
    """  Website login page for users to logging in """
    PAGES = (By.CLASS_NAME, 's-pagination-button')  # There will be more than 1 class with this name so. It should be a list.
    # SELECTED = (By.XPATH, "//span[@class='s-pagination-item s-pagination-selected']")
    PRODUCT_THIRD = (By.CSS_SELECTOR, ".s-asin")  # [2] will be  chosen
    PRODUCT_LIST = (By.CLASS_NAME, "a-size-medium")  # product lists on category page. need to get their text version.
    listpages = []
    listpages1 = []
    listproducts = []

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)  # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?
        self.wait = WebDriverWait(self.driver, 10)

    def clicking_the_second_page(self):
        """
        Navigating to second page on the category page.

        """
        self.methods.wait_for_element(self.PAGES)
        PAGES_TUPLE = self.driver.find_elements(*self.PAGES)
        for PAGES_RESULT in PAGES_TUPLE:
            self.listpages.append(PAGES_RESULT)
            self.listpages1.append(PAGES_RESULT.text)
            SELECTED_TEXT = self.listpages1[0]
        assert SELECTED_TEXT == "2", "Fault by 2"
        self.listpages[0].click()

    def clicking_the_third_item(self):
        """
        Clicking the third item in the Product List.
        """
        # self.methods.wait_for_element(self.PRODUCT_THIRD)[2].
        print(type(self.PRODUCT_THIRD))
        # self.methods.wait_for_element(self.PRODUCT_THIRD)
        # PRODUCTS = self.driver.find_elements(*self.PRODUCT_THIRD)
        PRODUCTS = self.wait.until(ec.presence_of_element_located(*self.PRODUCT_THIRD))
        for PRODUCT in PRODUCTS:
            self.listproducts.append(PRODUCT)
        print(self.listproducts)
        self.listproducts[2].click()

