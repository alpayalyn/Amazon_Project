import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from base.base_page import BaseClass
from pages.category_page import *

class AmazonProduct:
    """Website product page for adding the item to your WishList"""

    ADD_TO_LIST_BUTTON = (By.ID, 'WLHUC_result_listName')
    ADD_TO_LIST_BUTTON2 = (By.ID, 'wishListMainButton')
    CHOSEN_PRODUCT_NAME = (By.CLASS_NAME, "productTitle")
    CHOSEN_PRODUCT_NAME2 = (By.XPATH, "//div/h2/a[@class='a-link-normal']")
    listpages2 = []
    listpages3 = []
    SELECTED_TEXT = 0
    TEXTT = 0

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)  # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?

    def adding_product(self):
        """
        Clicking the Add to List & the clicking the link which redirects you to the Wish List.
        """

        self.methods.wait_for_element(self.ADD_TO_LIST_BUTTON2).click()

        texts = self.driver.find_elements(*self.CHOSEN_PRODUCT_NAME)
        for texti in texts:
            self.listpages3.append(texti.text)
            self.SELECTED_TEXT = self.listpages3[0]
            print(self.SELECTED_TEXT)

        self.methods.wait_for_element(self.ADD_TO_LIST_BUTTON).click()

        texts2 = self.driver.find_elements(*self.CHOSEN_PRODUCT_NAME)
        for texts2 in texts:
            self.listpages3.append(texts2.text)
            self.TEXTT = self.listpages3[0]
            print(self.TEXTT)

        assert self.SELECTED_TEXT == self.TEXTT


