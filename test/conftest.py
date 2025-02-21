import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def browser_setup(request):
    options_upd = webdriver.ChromeOptions()
    options_upd.add_argument('--start-maximized')
    options_upd.add_argument('--disable-popup-blocking')
    options_upd.add_argument('--disable-notifications')
    driver = webdriver.Chrome(options=options_upd)
    driver.get('https://login.salesforce.com/')
    request.cls.driver = driver
    yield driver
    driver.close()

