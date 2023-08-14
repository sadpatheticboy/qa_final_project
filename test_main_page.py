from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:
    """
    Тест-кейсы с действиями гостя на главной странице
    """

    def test_guest_can_go_to_login_page(self, browser):
        """
        Проверка того, что гость может перейти на страницу логина с главной страницы
        """
        link = "https://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()

        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        """
        Проверка того, что гость видит кнопку авторизации
        """
        link = "https://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()

        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Проверка того, что у гостя корзина пустая. Переход в корзину идет с главной страницы
    """
    link = "https://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, link)
    page.open()

    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
