from .base_page import BasePage
from .locators import BasePageLocators


class MainPage(BasePage):
    def click_view_basket_button(self):
        view_basket_button = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON)
        view_basket_button.click()




