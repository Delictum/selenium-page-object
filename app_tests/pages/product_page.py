from app_tests.pages.base_page import BasePage
from app_tests.pages.locators import ProductPageLocators
from app_tests.utils.price_parser import get_price_from_str


class ProductPage(BasePage):
    def add_item_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_alert_info_about_added_product(self):
        alert_product = self.browser.find_element(*ProductPageLocators.INFO_ABOUT_ADDED_PRODUCT)
        assert alert_product, "Alert info about added product is not presented."

    def should_info_contain_name_product(self, product_name):
        alert_product = self.browser.find_element(*ProductPageLocators.INFO_ABOUT_ADDED_PRODUCT)
        assert product_name in alert_product.text, "Alert doesn't contain the name of the product added to the basket."

    def should_be_alert_info_about_total_in_basket(self):
        total_in_basket = self.browser.find_element(*ProductPageLocators.TOTAL_IN_BASKET)
        assert total_in_basket, "Alert info about total cost in basket is not presented."

    def should_info_basket_total_equal_price(self, price):
        alert_product = self.browser.find_element(*ProductPageLocators.TOTAL_IN_BASKET)
        total_cost = round(get_price_from_str(alert_product.text), 2)
        assert float(price) == total_cost, "Alert doesn't equal total in the basket and the product price."
