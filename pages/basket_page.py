from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MSG), "Empty basket message is not present"

    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTAINS_GOODS),\
            "Empty basket should not contain goods"

