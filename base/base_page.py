from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class BaseClass(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 35)

    def wait_for_element(self, selector):
        """
        Wait for element to present
        :param selector: locator of the element to find.
        """
        return self.wait.until(ec.element_to_be_clickable(selector))

    def presence_for_element(self, selector):
        """
        Presence for element to present
        :param selector: locator of the element to find
        """
        return self.wait.until(ec.presence_of_element_located(selector))

    def wait_till_element_disappears(self, selector):
        """
        Wait for element to disappears
        :param selector: locator of the element to find
        """
        return self.wait.until(ec.invisibility_of_element_located(selector))




