from selenium.webdriver.common.by import By

from .base_page import BasePage


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, '#content_inner > p'), 'Basket is not empty'
