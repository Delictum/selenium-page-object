from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_text(self):
        basket_text = self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT)
        assert basket_text, "Text about basket is empty is not presented."

    def should_not_be_items_in_basket(self):
        items_list = self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
        assert items_list, "List items is presented."
