import pytest
from pages.base_page import main_page_link
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
basket_page_link = f"{main_page_link}basket/"



@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, main_page_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, main_page_link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.click_view_basket_button()
    page = BasketPage(browser, basket_page_link)
    page.should_be_your_basket_is_empty_message()
    page.should_not_be_items_in_basket()
