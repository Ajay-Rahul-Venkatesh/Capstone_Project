from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import Locators
from utilities.ReusableMethod import Utility


class Loginpage(Utility):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    def loginPage(self,username,password):
        self.driver.find_element(*Locators.username).send_keys(username)
        self.driver.find_element(*Locators.password).send_keys(password)
        self.driver.find_element(*Locators.login).click()
