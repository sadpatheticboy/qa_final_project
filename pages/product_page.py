from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_correct_price(self):
        product_price_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_PAGE)
        product_price_value = product_price_page.text

        product_price_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET)
        product_price_basket_value = product_price_basket.text[14:-12]

        assert product_price_value == product_price_basket_value, \
            f"Expeсted price: {product_price_value}. Actual price: {product_price_basket_value}."

        print("Correct price")

    def should_be_correct_name(self):
        product_name_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_PAGE)
        product_name_value = product_name_page.text

        product_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET)
        product_name_basket_value = product_name_basket.text

        assert product_name_value == product_name_basket_value, \
            f"Expected name: {product_name_value}. Actual name: {product_name_basket_value}."

        print("Correct name")
