import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    browser_name = request.param
    driver = None

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        ValueError("Can't create browser isinstance for this name")

    driver.maximize_window()
    yield driver

    driver.quit()
