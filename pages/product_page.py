from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_cart_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to cart btn is not presented"

    def add_to_cart(self):
        cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        cart.click()

    def should_be_product_added_to_curt_msg(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME), "No Add to cart Message"

    def should_be_equal_price_product_and_added_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
        assert product_price == added_product_price, "Product prices are not equal"

    def should_be_equal_name_product_and_added_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert product_name == added_product_name, "Product names are not equal"

    def should_be_cart_value(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def success_message_should_be_disappeared_add_to_cart(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_NAME), \
            "Success message didn't disappeared"
