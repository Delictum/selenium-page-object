import time

import pytest

from app_tests.pages.product_page import ProductPage


@pytest.mark.parametrize('num', [*range(1,7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
def test_guest_can_add_product_to_basket(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'

    page = ProductPage(browser, link)
    page.open()

    page.add_item_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_alert_info_about_added_product()
    page.should_info_equal_name_product()

    page.should_be_alert_info_about_total_in_basket()
    page.should_info_basket_total_equal_price()
