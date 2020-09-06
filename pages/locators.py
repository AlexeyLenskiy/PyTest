from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.XPATH, "//i[@class='icon-user']")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.XPATH, "//input[@id='id_registration-email']")
    REGISTER_PASSWORD = (By.XPATH, "//input[@id='id_registration-password1']")
    REGISTER_CONFIRM_PASSWORD = (By.XPATH, "//input[@id='id_registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")
    THANKS_FOR_REGISTERING_MESSAGE = (By.XPATH, "//div[contains(text(),'Thanks for registering!')]")


class BasketLocators():
    ITEMS_TO_BY = (By.XPATH, "//div[@class='basket-items']")
    YOUR_BASKET_IS_EMPTY_MESSAGE = (By.XPATH, "//p[contains(text(),'Your basket is empty.')]")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[@value='Add to basket']")
    PRODUCT_NAME = (By.XPATH, "//article[1]/div[1]/div[2]/h1[1]")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_ADDED_TO_BASKET_MESSAGE = (By.XPATH, "//div[@id='messages']//div[1]//div[1]")
