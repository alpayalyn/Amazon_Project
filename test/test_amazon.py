import unittest
from test.amazon_setup import Setup


class TestRun(unittest.TestCase, Setup):
    """Test case is:

        1. Go to given site.
        2. Check it by assertion whether we are on the Home Page or not.
        3. Open Login Screen & Login into an account
        4. Type 'samsung' into the Search Bar.
        5. It will validate, there is a result related to the Searched text.
        6. Then it will be navigated to the second page of the results.
        7. Then it will choose the third item in the list & click 'Add to List' button.
        8. It will validate the item which was added into the list, was correctly added.
        9. Item which was added into wishlist will be deleted.
        10. At last, it will validate there is no longer the item which was just added, in the wishlist.

    """

    def setUp(self):
        Setup.__init__(self)

    def test_amazon(self):
        assert self.url == self.driver.current_url, "URL ERROR"
        self.AmazonHome.navigating_to_login_page()
        self.AmazonLogin.login_into_account()
        self.AmazonSearch.texting_samsung_in_searchbar()
        text_control_samsung_search = self.AmazonSearch.searchbar_result()
        assert "Samsung" in text_control_samsung_search, "Samsung text doesn't match."
        self.AmazonCategory.clicking_the_second_page()
        text_control_second_page = self.AmazonCategory.getting_the_second_page_text()
        assert text_control_second_page == "2", "Text doesn't match."
        self.AmazonCategory.clicking_the_third_product()
        text_control_product_name_product_page = self.AmazonProduct.getting_the_product_name_text()
        self.AmazonProduct.clicking_add_to_list()
        self.AmazonProduct.clicking_the_list()
        text_control_product_name_wishlist_page = self.AmazonWishlist.getting_the_product_name_text()
        assert text_control_product_name_product_page == text_control_product_name_wishlist_page, \
            "Product that was added doesn't match."
        self.AmazonWishlist.deleting_the_product()
        text_control_wishlist_item_delete = self.AmazonWishlist.getting_the_text_after_delete()
        assert "Undo" == text_control_wishlist_item_delete, "Item wasn't deleted successfully."

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
