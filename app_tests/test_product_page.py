import time

from app_tests.pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()

    page.add_item_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_alert_info_about_added_product()
    page.should_info_contain_name_product("The shellcoder's handbook")

    page.should_be_alert_info_about_total_in_basket()
    page.should_info_basket_total_equal_price(9.99)

    time.sleep(3)
