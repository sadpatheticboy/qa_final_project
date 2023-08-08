from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",  # default language = en
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nStart browser for test..")
    user_language = request.config.getoption("language")
    if user_language:  # Передан ли параметр --language.
        options = Options()  # Если передан, то объявление браузера
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be correct language")  # Если нет, то возбуждение исключения

    yield browser
    print("\nQuit browser..")
    time.sleep(5)
    browser.quit()
