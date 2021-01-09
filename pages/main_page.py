from .base_page import BasePage
from .with_basket_link_page import WithBasketLinkPage


class MainPage(BasePage, WithBasketLinkPage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
