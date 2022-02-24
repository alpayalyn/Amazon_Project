from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import AmazonLogin
from pages.home_page import AmazonHome
from pages.category_page import AmazonCategory
from pages.product_page import AmazonProduct
from pages.search_page import AmazonSearch
from pages.wish_list import AmazonWishlist


class Setup:
    """
    Customizations will be adjusted.

    """
    driver_location = "/usr/bin/chromedriver"
    binary_location = "/usr/bin/google-chrome"
    option = webdriver.ChromeOptions()
    option.binary_location = binary_location
    driver = webdriver.Chrome(executable_path=driver_location, options=option)
    driver.maximize_window()
    url = "https://www.amazon.com/"
    AmazonHome = AmazonHome(driver)
    AmazonLogin = AmazonLogin(driver)
    AmazonSearch = AmazonSearch(driver)
    AmazonCategory = AmazonCategory(driver)
    AmazonProduct = AmazonProduct(driver)
    AmazonWishlist = AmazonWishlist(driver)

    def __init__(self):
        self.wait = WebDriverWait(self.driver, 15)

    def home_page_loaded_successfully(self):
        """Driver has been started."""

        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 15)


if __name__ == '__main__':
    Setup()
