import pytest
from base.webdriverfactory import WebDriverFactory
import sys

print(sys.path)

@pytest.yield_fixture()
def setup():
    print("once before every test method")
    yield
    print("once after every test method")


@pytest.yield_fixture(scope="class")
def ontimesetup(request, browser):
    print("once before every test module")
    wb = WebDriverFactory(browser)
    driver = wb.getDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("once after every test module")


def pytest_addoption(parser):
    parser.addoption("--browser",help="Chrome")


@pytest.fixture(scope="session")
def browser(request):
    print("once before Session")
    return request.config.getoption("--browser")
