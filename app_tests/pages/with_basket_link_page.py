from app_tests.pages.locators import WithBasketLinkPageLocators


class WithBasketLinkPage:
    def go_to_basket_page(self):
        link = self.browser.find_element(*WithBasketLinkPageLocators.BASKET_LINK)
        link.click()

    def should_be_basket_link(self):
        assert self.is_element_present(*WithBasketLinkPageLocators.BASKET_LINK), "Basket link is not presented"
