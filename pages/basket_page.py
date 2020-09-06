from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        self.should_be_your_basket_is_empty_message()
        self.should_not_be_items_in_basket()

    def should_be_your_basket_is_empty_message(self):
        assert self.is_element_present(*BasketLocators.YOUR_BASKET_IS_EMPTY_MESSAGE),  \
            "Your basket is is empty message is not presented"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketLocators.ITEMS_TO_BY), \
            "Items in basket is presented, but should not be"