from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators


class ProductPage(BasePage):
    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_page(self):
        self.should_be_product_page_url()
        self.should_be_product_name()
        self.should_be_product_price()

    def should_be_product_page_url(self):
        assert "catalogue" in self.browser.current_url, "There is no product name in url"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"

    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"

    def click_view_basket_button(self):
        self.should_be_view_basket_button()
        view_basket_button = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON)
        view_basket_button.click()

    def should_be_view_basket_button(self):
        assert self.is_element_present(*BasePageLocators.VIEW_BASKET_BUTTON), "View basket button is not presented"

    def should_be_product_added_to_basket_message(self):
        assert f"{self.product_name()}" and "has been added to your basket" in self.browser.find_element(
            *ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE).text, \
            "Product added to basket message is not presented"

    def should_not_be_product_added_to_basket_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE), \
            "Product added to basket message is presented, but should not be"

    def should_dissapear_product_added_to_basket_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE), \
            "Product added to basket message is presented, but should disappear"