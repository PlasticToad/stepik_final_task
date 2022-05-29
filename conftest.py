import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
	
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
						help="Choose language: es")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
						

@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("language")
    user_browser = request.config.getoption("browser_name")
    browser = None
    if user_browser == "chrome":
        print("\nstart chrome browser for test..")
        languages = Options()
        languages.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=languages)
    elif user_browser == "firefox":
        print("\nstart firefox browser for test..")
        languages = webdriver.FirefoxProfile()
        languages.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=languages)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()