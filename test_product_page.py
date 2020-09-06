import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.base_page import main_page_link
product_page_link = f"{main_page_link}catalogue/the-city-and-the-stars_95/"
login_page_link = f"{main_page_link}accounts/login/"
basket_page_link = f"{main_page_link}basket/"

@pytest.mark.need_review
class TestNeedReview():
    def test_user_can_add_product_to_basket(self, browser):
        page = LoginPage(browser, login_page_link)
        page.open()
        email = page.generate_email()
        password = page.generate_password()
        page.register_new_user(email, password)
        page.should_be_thanks_for_registering_message()
        page = ProductPage(browser, product_page_link)
        page.open()
        page.should_be_product_page()
        page.add_product_to_basket()
        page.should_be_product_added_to_basket_message()

    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_page_link)
        page.open()
        page.should_be_product_page()
        page.add_product_to_basket()
        page.should_be_product_added_to_basket_message()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, product_page_link)
        page.open()
        page.click_view_basket_button()
        page = BasketPage(browser, basket_page_link)
        page.should_not_be_products_in_basket()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, product_page_link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, login_page_link)
        page.should_be_login_page()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_added_to_basket_message(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.should_not_be_product_added_to_basket_message()


@pytest.mark.user_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = LoginPage(browser, login_page_link)
        self.page.open()
        email = self.page.generate_email()
        password = self.page.generate_password()
        self.page.register_new_user(email, password)
        self.page.should_be_thanks_for_registering_message()

    def test_user_can_add_product_to_basket(self, browser):
        self.page = ProductPage(browser, product_page_link)
        self.page.open()
        self.page.should_be_product_page()
        self.page.add_product_to_basket()
        self.page.should_be_product_added_to_basket_message()

    def test_user_cant_see_product_added_to_basket_message(self, browser):
        self.page = ProductPage(browser, product_page_link)
        self.page.open()
        self.page.click_view_basket_button()
        self.page.should_not_be_product_added_to_basket_message()