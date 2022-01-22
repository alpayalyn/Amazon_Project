import unittest
from selenium import webdriver

class test_amazon(unittest.TestCase):
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
        # Setting up how we want Chrome to run
        self.driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
        self.driver.maximize_window()

    def test_amazon(self):
        self.home_page.home_page_loaded_successfully()
        self.home_page.navigating_to_login_page()
        self.login_page.login_into_account()
        self.search_page.texting_samsung_in_searchbar()
        self.category_page.clicking_the_second_page()
        self.category_page.clicking_the_third_item()
        self.product_page.adding_product()
        self.wish_list.deleting_the_product()
        self.wish_list.deleting_validation()

    def tearDown(self):
        # To do the cleanup after test has executed.
        self.driver.close()

if __name__ == '__main__':
    # specify path where the HTML reports for testcase execution are to be generated
    unittest.main()