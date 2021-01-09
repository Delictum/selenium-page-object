from .base_page import BasePage
from .locators import ProductPageLocators
from .with_basket_link_page import WithBasketLinkPage


class ProductPage(BasePage, WithBasketLinkPage):
    def add_item_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_alert_info_about_added_product(self):
        alert_product = self.browser.find_element(*ProductPageLocators.INFO_ABOUT_ADDED_PRODUCT)
        assert alert_product, "Alert info about added product is not presented."

    def should_info_equal_name_product(self):
        alert_product = self.browser.find_element(*ProductPageLocators.INFO_ABOUT_ADDED_PRODUCT).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == alert_product, "Alert doesn't equal the name of the product added to the basket."

    def should_be_alert_info_about_total_in_basket(self):
        total_in_basket = self.browser.find_element(*ProductPageLocators.TOTAL_IN_BASKET)
        assert total_in_basket, "Alert info about total cost in basket is not presented."

    def should_info_basket_total_equal_price(self):
        alert_product = self.browser.find_element(*ProductPageLocators.TOTAL_IN_BASKET).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == alert_product, "Alert doesn't equal total in the basket and the product price."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
