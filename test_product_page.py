from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import time


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    """
    Проверка того, что гость может добавить товар в корзину
    """
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()

    page.add_product_to_basket()
    # page.solve_quiz_and_get_code() # Здесь вызывается метод для решения математической задачи. Я решил
    # закомментировать это, т.к. уже нет необходимости в данном методе, но пусть будет в случае чего, может захочу
    # в будущем перепройти курс
    page.should_be_correct_price()
    page.should_be_correct_name()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    (Отрцитательный тест) Проверка того, что гость не видит сообщение об успешности после добавления в корзинк
    """
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    (Отрицательный тест) Проверка того, что сообщение о добавлении товара исчезает со временем
    """
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    page.add_product_to_basket()
    page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    """
    Проверка того, что у гостя отображается кнопка авторизации
    """
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    Проверка того, что гость может зайти на страницу авторизации со страницы товара
    """
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Проверка того, что гость вид изначально пустую корзину
    """
    link = "https://selenium1py.pythonanywhere.com/en-gb/"
    page = ProductPage(browser, link)
    page.open()

    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()


@pytest.mark.product_user
class TestUserAddToBasketFromProductPage:
    """
    Тест-кейсы с действиями зарегистрированного пользователя на странице товаров
    """

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()

        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, 'adinWQye236sao')
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """
        Проверка возможности того, что пользователь смог добавить товар в коризну
        """
        link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()

        page.add_product_to_basket()
        page.should_be_correct_price()
        page.should_be_correct_name()

    def test_user_cant_see_success_message(self, browser):
        """
        Проверка того, что пользователь не видит сообщение об успехе без действий добавления в корзину
        """
        link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()

        page.should_not_be_success_message()
