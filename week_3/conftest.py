import pytest
from selenium import webdriver

# этот файл подключается к остальным в заголовке
# аналог глобального объявления, лучше не плодить, как и все глобальное

def pytest_addoption(parser):  #добавление опции при запуске из командной строки
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

#  запуск: pytest -s -v --browser_name=chrome test_parser.py

@pytest.fixture(scope="function")
def browser(request):  #встроенная функция
    browser_name = request.config.getoption("browser_name")  #получаем имя опции
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
