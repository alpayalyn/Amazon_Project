from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BaseClass(object):
    """
        Functions in the Base page will be called by other pages to perform actions.

    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 35)

    def click_the_element(self, selector, index):
        """Performs the click function"""
        self.wait_for_element(selector, index).click()

    def wait_for_element(self, selector, index):
        """Allows the page to load and find the element"""
        if index >= 0:
            return self.wait.until(ec.presence_of_all_elements_located(selector))[int(index)]
        return self.wait.until(ec.presence_of_all_elements_located(selector))

    def scrolling_the_page(self, y_coordinate):
        """
        Scrolling page towards down.
        """
        self.driver.execute_script("window.scrollTo(0, " + str(y_coordinate) + ")")

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

    def get_text(self, selector, index):
        """
        Returning the requested text
        """
        element = self.wait.until(ec.presence_of_all_elements_located(selector))[int(index)]
        return element.text


