from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span > a")


# class MainPageLocators:
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE_PAGE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_NAME_PAGE = (By.CSS_SELECTOR, " div > h1")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")


class BasketPageLocators:
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
