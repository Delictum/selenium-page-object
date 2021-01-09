import time

import pytest
from faker import Faker

from app_tests.pages.basket_page import BasketPage
from app_tests.pages.login_page import LoginPage
from app_tests.pages.product_page import ProductPage


@pytest.mark.login_guest
class TestLoginFromProductPage:
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.add_product
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

        page = LoginPage(browser, link)
        page.open()

        fake = Faker()
        email = fake.email()
        password = fake.password()

        page.register_new_user(email, password)
        page.should_be_authorized_user()

        # yield
        # time.sleep(5)

    def test_user_cant_see_success_message(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

        page = ProductPage(browser, link)
        page.open()

        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'

        page = ProductPage(browser, link)
        page.open()

        page.add_item_to_basket()
        page.solve_quiz_and_get_code()

        page.should_be_alert_info_about_added_product()
        page.should_info_equal_name_product()

        page.should_be_alert_info_about_total_in_basket()
        page.should_info_basket_total_equal_price()


@pytest.mark.parametrize('num', [*range(1, 7), pytest.param(7, marks=pytest.mark.xfail), *range(8, 10)])
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


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_empty_basket_text()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    page = ProductPage(browser, link)
    page.open()

    page.add_item_to_basket()

    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    page = ProductPage(browser, link)
    page.open()

    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    page = ProductPage(browser, link)
    page.open()

    page.add_item_to_basket()

    page.should_disappear_of_success_message()
