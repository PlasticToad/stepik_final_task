import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
	print("\nstart browser for test..")
	browser = webdriver.Chrome()
	yield browser
	print("\nquit browser..")
	browser.quit()
	
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', #можно задать стандартное значение
						help="Choose language: es")
						

@pytest.fixture(scope="function")
def browser(request):
	language = request.config.getoption("language")
	languages = Options()
	languages.add_experimental_option('prefs', {'intl.accept_languages': language})
	browser = webdriver.Chrome(options=languages)
	yield browser
	print("\nquit browser..")
	browser.quit()