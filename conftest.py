import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language: ru, en-gb, ar, etc.")

@pytest.fixture(scope="function")
def language(request):
    l=["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-hans"]
    language = request.config.getoption("language")
    if language in l:
        return language
    else:
        raise pytest.UsageError("--language should be correct")

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome('C:/chromedriver/chromedriver')
    yield browser
    print("\nquit browser..")
    browser.quit()
