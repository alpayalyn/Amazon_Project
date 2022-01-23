import unittest
from test.amazon_setup import Setup
from pages.login_page import *
from pages.category_page import *
from pages.search_page import *
from pages.product_page import *
from pages.home_page import *
from pages.wish_list import *

class TestRun(unittest.TestCase, Setup):
    """
    1. Go to given site.
    2. Check it by assertion whether we are on the Home Page or not.
    3. Open Login Screen & Login into an account
    4. Type 'samsung' into the Search Bar.
    5. It will validate, there is a result related to the Searched text.
    6. Then it will be navigated to the second page of the results.
    7. Then it will choose the third item in the list & click 'Add to List' button.
    8. It will validate the item which was added into the list, was correctly added.
    9. Item which was added into wishlist will be deleted.
    10. At last it will validate there is no longer the item which was just added, in the wishlist.

    """

    def setUp(self):
        Setup.__init__(self)

    def test_amazon(self):
        AmazonHome(self.driver).home_page_loaded_successfully()
        AmazonHome(self.driver).navigating_to_login_page()
        AmazonLogin(self.driver).login_into_account()
        AmazonSearch(self.driver).texting_samsung_in_searchbar()
        AmazonCategory(self.driver).clicking_the_second_page()
        AmazonCategory(self.driver).clicking_the_third_item()
        AmazonProduct(self.driver).adding_product()
        AmazonWishlist(self.driver).deleting_the_product()
        AmazonWishlist(self.driver).deleting_validation()

    def tearDown(self):
        # To do the cleanup after test has executed.
        self.driver.close()


if __name__ == '__main__':
    # specify path where the HTML reports for testcase execution are to be generated
    unittest.main()
