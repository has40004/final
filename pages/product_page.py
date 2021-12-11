from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

"""
Page Object, which is linked to the product page.
"""


class ProductPage(BasePage):
    def add_product_to_basket(self):
        # Adding a product to the basket
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def guest_can_add_product_to_basket(self):
        # Start all checking
        self.add_product_to_basket()
        try:
            self.solve_quiz_and_get_code()
        except NoAlertPresentException:
            print("No alert presented")
        self.guest_can_see_message_product_add_to_basket()
        self.guest_can_see_same_product_name()
        self.guest_can_see_message_price_basket()
        self.guest_can_see_correct_price_basket()

    def guest_can_see_message_product_add_to_basket(self):
        # Checking the display of the message that the item has been added to the basket
        message_product_add_to_basket = self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ADD_PRODUCT)
        assert message_product_add_to_basket, "Product not add to basket."

    def guest_can_see_same_product_name(self):
        # Checking the coincidence of the name of the product in the store and in the basket
        product_name_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_STORE)
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        print(f'Name in store: {product_name_in_store.text}, Name in basket: {product_name_in_basket.text}')
        assert product_name_in_store.text == product_name_in_basket.text, "Product name is no the same"

    def guest_can_see_message_price_basket(self):
        # Checking the display of the message about the price of the basket
        message_price_basket = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_BASKET_PRICE)
        assert message_price_basket, "Not see basket price."

    def guest_can_see_correct_price_basket(self):
        # Checking the coincidence of the cost of goods in the store and the total cost of the basket
        product_prise_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_STORE)
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        print(f'Price in store: {product_prise_in_store.text}, Price in basket: {product_price_in_basket.text}')
        assert product_prise_in_store.text == product_price_in_basket.text, "Price is wrong"

    def should_not_be_success_message(self):
        # not guest_can_see_message_product_add_to_basket()
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ADD_PRODUCT), \
            "Success message is presented, but should not be"

    def should_be_disappear_success_message(self):
        # not guest_can_see_message_product_add_to_basket()
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_ADD_PRODUCT), \
            "Success message should have disappeared, but not gone."

