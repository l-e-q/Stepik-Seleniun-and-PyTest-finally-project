import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def guest_should_see_product_added_to_basket(self):
        self.should_be_product_added_to_basket_alert()
        self.product_name_equals_product_name_in_product_added_to_basket_alert()
        self.should_be_basket_alert()
        self.basket_cost_equals_product_cost()

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_product_added_to_basket_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ALERT), 'Product added ' \
                                                                                            'to basket alert not found'

    def product_name_equals_product_name_in_product_added_to_basket_alert(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.\
            find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text, 'Product name in alert isn\'t correct'

    def should_be_basket_alert(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_ALERT), 'Basket alert isn\'t presented'

    def basket_cost_equals_product_cost(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_COST_IN_ALERT).text, 'Cost in alert isn\' correct'

