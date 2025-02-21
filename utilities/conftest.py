# import pytest
# from selenium import webdriver
#
# @pytest.fixture(scope='class')
# def browser_setup(request):
#     options_upd = webdriver.ChromeOptions()
#     options_upd.add_argument('--start-maximized')
#     options_upd.add_argument('--disable-popup-blocking')
#     options_upd.add_argument('--disable-notifications')
#     driver = webdriver.Chrome(options=options_upd)
#     driver.get('https://login.salesforce.com/')
#     request.cls.driver = driver
#     yield driver
#     driver.close()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def browser_setup(context):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-notifications')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://login.salesforce.com/")
    return driver


