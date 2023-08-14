from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        basket_message_value = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text
        assert "Your basket is not empty" in basket_message_value

    def is_basket_not_empty(self):
        basket_message_value = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text
        assert "Your basket is empty" not in basket_message_value
