from selenium.webdriver.common.by import By

"""
Variable locators to find them in pages
"""


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini span.btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    FIELD_REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    FIELD_REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    FIELD_REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION_USER = (By.CSS_SELECTOR, "[name='registration_submit']")
    ICON_OK_SIGN = (By.CSS_SELECTOR, ".icon-ok-sign")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_STORE = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE_IN_STORE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages div:first-child strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    SUCCESS_MESSAGE_ADD_PRODUCT = (By.CSS_SELECTOR, "#messages div:first-child")
    SUCCESS_MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) .alertinner > p")


class BasketPageLocators():
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset > div > div > div.col-sm-4 > h3 > a")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset > div > div > div:nth-child(5) > p")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    PRESENCE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
