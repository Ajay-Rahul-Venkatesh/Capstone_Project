import time
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import Locators
from utilities.ReusableMethod import Utility


class Contactspage(Utility):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def createContact(self,contact_name,last_name):
        time.sleep(5)
        self.driver.find_element(*Locators.contact_dropdown).click()
        time.sleep(5)
        self.driver.execute_script('arguments[0].click();',self.driver.find_element(*Locators.new_contact_icon))
        time.sleep(5)
        self.driver.find_element(*Locators.search_icon).click()
        time.sleep(5)
        self.driver.find_element(*Locators.recentAccountName(contact_name)).click()
        time.sleep(5)
        self.driver.find_element(*Locators.lastname).send_keys(last_name)
        self.driver.find_element(*Locators.saveedit).click()
