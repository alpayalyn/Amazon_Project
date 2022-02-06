import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from base.base_page import BaseClass
from pages.product_page import *

class AmazonWishlist:
    """Website login page for users to logging in"""
    DELETE_BUTTON = (By.XPATH, "//span/span/input[@class='a-button-input a-declarative']")
    WISH_LIST_LINK = (By.ID, "WLHUC_result_listName")
    listpages4 = []

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)  # Self driver is being sent, because YOU NEED it. It cant benefit from the driver definition which is in BaseClass?

    def deleting_the_product(self):
        texts = self.driver.find_elements(*self.DELETE_BUTTON)
        for texts3 in texts:
            self.listpages4.append(texts3)
        self.listpages4[1].click()
        time.sleep(10)
