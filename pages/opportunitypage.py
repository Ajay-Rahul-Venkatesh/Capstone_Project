import time
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime, timedelta
from pages.locators import Locators
from utilities.ReusableMethod import Utility


class Opportunitypage(Utility):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def createOpportunity(self,account_name,opportunity_name):
        time.sleep(5)
        self.driver.find_element(*Locators.opportunity_dropdown).click()
        time.sleep(5)
        self.driver.execute_script('arguments[0].click();',self.driver.find_element(*Locators.new_opportunity_icon))
        time.sleep(5)
        self.driver.find_element(*Locators.search_icon).click()
        time.sleep(10)
        self.driver.find_element(*Locators.recentAccountName(account_name)).click()
        time.sleep(5)
        self.driver.find_element(*Locators.opportunity_name_field).send_keys(opportunity_name)
        current_date_plus_10 = (datetime.now() + timedelta(days=10)).strftime("%d/%m/%Y")
        self.driver.find_element(*Locators.opportunity_date_field).send_keys(current_date_plus_10)
        time.sleep(5)
        self.driver.execute_script('arguments[0].click();',self.driver.find_element(*Locators.stage_dropdown))
        time.sleep(10)
        self.driver.find_element(*Locators.qualification_option).click()
        self.driver.find_element(*Locators.saveedit).click()
