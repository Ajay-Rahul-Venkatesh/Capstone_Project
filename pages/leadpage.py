import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import Locators
from utilities.ReusableMethod import Utility


class Leadpage(Utility):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    def createLead(self, firstname, lastname, company):
        # header_element=self.wait_for_element(Locators.lead_header,30)
        time.sleep(10)
        # self.driver.execute_script('arguments[0].click();', header_element)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.lead_header))
        # drop_down_element=self.wait_for_element(Locators.lead_dropdown,30)
        time.sleep(10)
        # drop_down_element.click()
        self.driver.find_element(*Locators.lead_dropdown).click()
        # new_lead_element=self.wait_for_element(Locators.new_lead_icon,30)
        time.sleep(10)
        # self.driver.execute_script('arguments[0].click();', new_lead_element)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.new_lead_icon))
        # self.wait_for_element(Locators.salutation,30)
        time.sleep(10)
        self.driver.find_element(*Locators.salutation).click()
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.salutation_option))
        # self.wait_for_element(Locators.firstname,30)
        time.sleep(10)
        self.driver.find_element(*Locators.firstname).send_keys(firstname)
        self.driver.find_element(*Locators.lastname).send_keys(lastname)
        self.driver.find_element(*Locators.company).send_keys(company)
        self.driver.find_element(*Locators.saveedit).click()

    def convertLead(self):
        time.sleep(10)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.convert_dropdown))
        time.sleep(5)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.convert_text))
        time.sleep(5)
        self.driver.find_element(*Locators.convert_button).click()
        time.sleep(5)
        self.driver.find_element(*Locators.close_window).click()

    def convertLeadAccount(self, data):
        try:
            time.sleep(2)
            converted = self.driver.find_element(Locators.convert_title)
            success_msg = converted.text
            expected_message = data['lead_converttitle']
            print("done: ", success_msg)
            assert success_msg == expected_message, f"Expected: '{expected_message}', but got: '{success_msg}'"

        except Exception as e:
            print(f"Error: {e}")
            raise e


