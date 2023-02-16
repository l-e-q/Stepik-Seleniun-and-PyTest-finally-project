from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini >  span > a')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, '#register_form > button')


class ProductPageLocators:
    PRODUCT_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    SUCCESS_ALERT = (By.CSS_SELECTOR, '.alert-success:nth-child(1)')
    PRODUCT_COST = (By.CSS_SELECTOR, 'div.col-sm-6 > p.price_color')
    BASKET_ALERT = (By.CSS_SELECTOR, '#messages > div.alert-info')
    PRODUCT_COST_IN_ALERT = (By.CSS_SELECTOR, '.alertinner > p:nth-child(1) >strong')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
