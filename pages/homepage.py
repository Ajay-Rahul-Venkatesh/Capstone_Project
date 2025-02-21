from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from pages.locators import Locators
from utilities.ReusableMethod import Utility


# class Homepage(Utility):
#
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#         self.wait = WebDriverWait(self.driver, 10)
#
#     def wait_for_element_to_be_clickable(self, locator):
#         self.wait.until(EC.element_to_be_clickable(locator))
#
#     def wait_for_element_to_be_present(self, locator):
#         self.wait.until(EC.presence_of_element_located(locator))
#
#     def login(self, username, password):
#         self.driver.find_element(*Locators.username).send_keys(username)
#         self.driver.find_element(*Locators.password).send_keys(password)
#         self.driver.find_element(*Locators.login).click()
#
#     def createLead(self, firstname, lastname, company):
#         self.wait_for_element_to_be_clickable(Locators.lead_header)
#         self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.lead_header))
#         self.wait_for_element_to_be_clickable(Locators.lead_dropdown)
#         self.driver.find_element(*Locators.lead_dropdown).click()
#         self.wait_for_element_to_be_clickable(Locators.new_lead_icon)
#         self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.new_lead_icon))
#         self.wait_for_element_to_be_clickable(Locators.salutation)
#         self.driver.find_element(*Locators.salutation).click()
#         self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.salutation_option))
#         self.wait_for_element_to_be_clickable(Locators.firstname)
#         self.driver.find_element(*Locators.firstname).send_keys(firstname)
#         self.driver.find_element(*Locators.lastname).send_keys(lastname)
#         self.driver.find_element(*Locators.company).send_keys(company)
#         self.driver.find_element(*Locators.saveedit).click()
#
#     def convertLead(self):
#         self.wait_for_element_to_be_clickable(Locators.convert_dropdown)
#         self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.convert_dropdown))
#         self.wait_for_element_to_be_clickable(Locators.convert_text)
#         self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.convert_text))
#         self.wait_for_element_to_be_clickable(Locators.convert_button)
#         self.driver.find_element(*Locators.convert_button).click()
#         self.wait_for_element_to_be_clickable(Locators.close_window)
#         self.driver.find_element(*Locators.close_window).click()
#
#     def verifyConvertedLead(self, first_name, last_name, company):
#         self.wait_for_element_to_be_clickable(Locators.accounts_dropdown)
#         self.driver.find_element(*Locators.accounts_dropdown).click()
#         self.wait_for_element_to_be_clickable(Locators.recent_method(company))
#         self.driver.execute_script(
#             'arguments[0].click();',
#             self.driver.find_element(*Locators.recent_method(company))
#         )
#         self.wait_for_element_to_be_present(Locators.account_name)
#         name = self.driver.find_element(*Locators.account_name).text
#
#         assert name == f"{first_name} {last_name}", \
#             f"Expected {first_name} {last_name}, but got {name}"
#         print(f"Verified lead: {name}")
#
#     def createAccount(self, account_name):
#         self.wait_for_element_to_be_clickable(Locators.accounts_dropdown)
#         self.driver.find_element(*Locators.accounts_dropdown).click()
#         self.wait_for_element_to_be_clickable(Locators.new_account_icon)
#         self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.new_account_icon))
#         self.wait_for_element_to_be_clickable(Locators.account_name_field)
#         self.driver.find_element(*Locators.account_name_field).send_keys(account_name)
#         self.driver.find_element(*Locators.saveedit).click()
#
#     def createContact(self, contact_name, last_name):
#         self.wait_for_element_to_be_clickable(Locators.contact_dropdown)
#         self.driver.find_element(*Locators.contact_dropdown).click()
#         self.wait_for_element_to_be_clickable(Locators.new_contact_icon)
#         self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.new_contact_icon))
#         self.wait_for_element_to_be_clickable(Locators.search_icon)
#         self.driver.find_element(*Locators.search_icon).click()
#         self.wait_for_element_to_be_clickable(Locators.recentAccountName(contact_name))
#         self.driver.find_element(*Locators.recentAccountName(contact_name)).click()
#         self.wait_for_element_to_be_clickable(Locators.lastname)
#         self.driver.find_element(*Locators.lastname).send_keys(last_name)
#         self.driver.find_element(*Locators.saveedit).click()
#
#     def createOpportunity(self, account_name, opportunity_name):
#         self.wait_for_element_to_be_clickable(Locators.opportunity_dropdown)
#         self.driver.find_element(*Locators.opportunity_dropdown).click()
#         self.wait_for_element_to_be_clickable(Locators.new_opportunity_icon)
#         self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.new_opportunity_icon))
#         self.wait_for_element_to_be_clickable(Locators.search_icon)
#         self.driver.find_element(*Locators.search_icon).click()
#         self.wait_for_element_to_be_clickable(Locators.recentAccountName(account_name))
#         self.driver.find_element(*Locators.recentAccountName(account_name)).click()
#         self.wait_for_element_to_be_clickable(Locators.opportunity_name_field)
#         self.driver.find_element(*Locators.opportunity_name_field).send_keys(opportunity_name)
#         current_date_plus_10 = (datetime.now() + timedelta(days=10)).strftime("%d/%m/%Y")
#         self.driver.find_element(*Locators.opportunity_date_field).send_keys(current_date_plus_10)
#         self.wait_for_element_to_be_clickable(Locators.stage_dropdown)
#         self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.stage_dropdown))
#         self.wait_for_element_to_be_clickable(Locators.qualification_option)
#         self.driver.find_element(*Locators.qualification_option).click()
#         self.driver.find_element(*Locators.saveedit).click()
#
#     def verifyContact(self, account_name, contact_name):
#         self.wait_for_element_to_be_clickable(Locators.accounts_dropdown)
#         self.driver.find_element(*Locators.accounts_dropdown).click()
#         self.wait_for_element_to_be_clickable(Locators.recent_method(account_name))
#         self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.recent_method(account_name)))
#         self.wait_for_element_to_be_present(Locators.contactOrOpportunity(contact_name))
#         actual_contact_name = self.driver.find_element(*Locators.contactOrOpportunity(contact_name)).text
#
#         assert contact_name == actual_contact_name, f"Expected {contact_name}, but got {actual_contact_name}"
#
#     def verifyOpportunity(self, opportunity):
#         self.wait_for_element_to_be_present(Locators.contactOrOpportunity(opportunity))
#         actual_opportunity_name = self.driver.find_element(*Locators.contactOrOpportunity(opportunity)).text
#
#         assert actual_opportunity_name == opportunity, f"Expected {opportunity}, but got {actual_opportunity_name}"

class Homepage(Utility):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element_to_be_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_be_present(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def login(self, username, password):
        self.driver.find_element(*Locators.username).send_keys(username)
        self.driver.find_element(*Locators.password).send_keys(password)
        self.driver.find_element(*Locators.login).click()

    def create_lead(self, firstname, lastname, company):
        self.wait_for_element_to_be_clickable(Locators.lead_header)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.lead_header))
        self.wait_for_element_to_be_clickable(Locators.lead_dropdown)
        self.driver.find_element(*Locators.lead_dropdown).click()
        self.wait_for_element_to_be_clickable(Locators.new_lead_icon)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.new_lead_icon))
        self.wait_for_element_to_be_clickable(Locators.salutation)
        self.driver.find_element(*Locators.salutation).click()
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.salutation_option))
        self.wait_for_element_to_be_clickable(Locators.firstname)
        self.driver.find_element(*Locators.firstname).send_keys(firstname)
        self.driver.find_element(*Locators.lastname).send_keys(lastname)
        self.driver.find_element(*Locators.company).send_keys(company)
        self.driver.find_element(*Locators.saveedit).click()

    def convert_lead(self):
        self.wait_for_element_to_be_clickable(Locators.convert_dropdown)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.convert_dropdown))
        self.wait_for_element_to_be_clickable(Locators.convert_text)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.convert_text))
        self.wait_for_element_to_be_clickable(Locators.convert_button)
        self.driver.find_element(*Locators.convert_button).click()
        self.wait_for_element_to_be_clickable(Locators.close_window)
        self.driver.find_element(*Locators.close_window).click()

    def verify_converted_lead(self, first_name, last_name, company):
        self.wait_for_element_to_be_clickable(Locators.accounts_dropdown)
        self.driver.find_element(*Locators.accounts_dropdown).click()
        self.wait_for_element_to_be_clickable(Locators.recent_method(company))
        self.driver.execute_script(
            'arguments[0].click();',
            self.driver.find_element(*Locators.recent_method(company))
        )
        self.wait_for_element_to_be_present(Locators.account_name)
        name = self.driver.find_element(*Locators.account_name).text

        assert name == f"{first_name} {last_name}", \
            f"Expected {first_name} {last_name}, but got {name}"
        print(f"Verified lead: {name}")

    def create_account(self, account_name):
        self.wait_for_element_to_be_clickable(Locators.accounts_dropdown)
        self.driver.find_element(*Locators.accounts_dropdown).click()
        self.wait_for_element_to_be_clickable(Locators.new_account_icon)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.new_account_icon))
        self.wait_for_element_to_be_clickable(Locators.account_name_field)
        self.driver.find_element(*Locators.account_name_field).send_keys(account_name)
        self.driver.find_element(*Locators.saveedit).click()

    def create_contact(self, contact_name, last_name):
        self.wait_for_element_to_be_clickable(Locators.contact_dropdown)
        self.driver.find_element(*Locators.contact_dropdown).click()
        self.wait_for_element_to_be_clickable(Locators.new_contact_icon)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.new_contact_icon))
        self.wait_for_element_to_be_clickable(Locators.search_icon)
        self.driver.find_element(*Locators.search_icon).click()
        self.wait_for_element_to_be_clickable(Locators.recentAccountName(contact_name))
        self.driver.find_element(*Locators.recentAccountName(contact_name)).click()
        self.wait_for_element_to_be_clickable(Locators.lastname)
        self.driver.find_element(*Locators.lastname).send_keys(last_name)
        self.driver.find_element(*Locators.saveedit).click()

    def create_opportunity(self, account_name, opportunity_name):
        self.wait_for_element_to_be_clickable(Locators.opportunity_dropdown)
        self.driver.find_element(*Locators.opportunity_dropdown).click()
        self.wait_for_element_to_be_clickable(Locators.new_opportunity_icon)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.new_opportunity_icon))
        self.wait_for_element_to_be_clickable(Locators.search_icon)
        self.driver.find_element(*Locators.search_icon).click()
        self.wait_for_element_to_be_clickable(Locators.recentAccountName(account_name))
        self.driver.find_element(*Locators.recentAccountName(account_name)).click()
        self.wait_for_element_to_be_clickable(Locators.opportunity_name_field)
        self.driver.find_element(*Locators.opportunity_name_field).send_keys(opportunity_name)
        current_date_plus_10 = (datetime.now() + timedelta(days=10)).strftime("%d/%m/%Y")
        self.driver.find_element(*Locators.opportunity_date_field).send_keys(current_date_plus_10)
        self.wait_for_element_to_be_clickable(Locators.stage_dropdown)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.stage_dropdown))
        self.wait_for_element_to_be_clickable(Locators.qualification_option)
        self.driver.find_element(*Locators.qualification_option).click()
        self.driver.find_element(*Locators.saveedit).click()

    def verify_contact(self, account_name, contact_name):
        self.wait_for_element_to_be_clickable(Locators.accounts_dropdown)
        self.driver.find_element(*Locators.accounts_dropdown).click()
        self.wait_for_element_to_be_clickable(Locators.recent_method(account_name))
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.recent_method(account_name)))
        self.wait_for_element_to_be_present(Locators.contactOrOpportunity(contact_name))
        actual_contact_name = self.driver.find_element(*Locators.contactOrOpportunity(contact_name)).text

        assert contact_name == actual_contact_name, f"Expected {contact_name}, but got {actual_contact_name}"

    def verify_opportunity(self, opportunity):
        self.wait_for_element_to_be_present(Locators.contactOrOpportunity(opportunity))
        actual_opportunity_name = self.driver.find_element(*Locators.contactOrOpportunity(opportunity)).text

        assert actual_opportunity_name == opportunity, f"Expected {opportunity}, but got {actual_opportunity_name}"
