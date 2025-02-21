import time
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import Locators
from utilities.ReusableMethod import Utility


class Accountspage(Utility):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def verifyConvertedLead(self,first_name,last_name,company):
        time.sleep(5)
        self.driver.find_element(*Locators.accounts_dropdown).click()
        time.sleep(5)

        self.driver.execute_script(
            'arguments[0].click();',
            self.driver.find_element(*Locators.recent_method(company))
        )
        time.sleep(5)
        name = self.driver.find_element(*Locators.account_name).text

        # Compare the retrieved name with the generated name
        assert name == f"{first_name} {last_name}", \
            f"Expected {first_name} {last_name}, but got {name}"
        print(f"Verified lead: {name}")

    def createAccount(self,account_name):
        time.sleep(10)
        self.driver.find_element(*Locators.accounts_dropdown).click()
        time.sleep(10)
        self.driver.execute_script('arguments[0].click();',self.driver.find_element(*Locators.new_account_icon))
        time.sleep(5)
        self.driver.find_element(*Locators.account_name_field).send_keys(account_name)
        self.driver.find_element(*Locators.saveedit).click()

    def verifyContact(self,account_name,contact_name):
        time.sleep(5)
        self.driver.find_element(*Locators.accounts_dropdown).click()
        time.sleep(5)
        self.driver.execute_script('arguments[0].click();',self.driver.find_element(*Locators.recent_method(account_name)))
        time.sleep(5)
        actual_contact_name=self.driver.find_element(*Locators.contactOrOpportunity(contact_name)).text

        assert contact_name == actual_contact_name,f"Expected {contact_name} , but got {actual_contact_name}"

    def verifyOpportunity(self,opportunity):
        time.sleep(10)
        actual_opportunity_name = self.driver.find_element(*Locators.contactOrOpportunity(opportunity)).text

        assert actual_opportunity_name == opportunity, f"Expected {opportunity} , but got {actual_opportunity_name}"

