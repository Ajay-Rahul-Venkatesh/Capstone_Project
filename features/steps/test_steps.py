import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.loginpage import Loginpage
from pages.leadpage import Leadpage
from pages.accountspage import Accountspage
from pages.contactspage import Contactspage
from pages.opportunitypage import Opportunitypage
from test_data.read_data import input_data
from utilities.conftest import browser_setup


@given('I log in to the application with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.driver = browser_setup(context)
    context.login = Loginpage(context.driver)
    context.login.loginPage(username, password)
    context.lead = Leadpage(context.driver)


@when('I create a lead with first name "{firstname}", last name "{lastname}", and company "{company}"')
def step_create_lead(context, firstname, lastname, company):
    context.lead.createLead(firstname, lastname, company)


@when('I convert the lead')
def step_convert_lead(context):
    context.lead.convertLead()
    context.account = Accountspage(context.driver)


@then('I should verify the recently converted account with first name "{firstname}", last name "{lastname}", '
      'and company "{company}"')
def step_verify_recent_account(context, firstname, lastname, company):
    context.account.verifyConvertedLead(firstname, lastname, company)



@when('I create an account with name "{account_name}"')
def step_create_account(context, account_name):
    context.account = Accountspage(context.driver)
    context.account.createAccount(account_name)
    context.contactpage = Contactspage(context.driver)


@when('I create a contact with account name "{account_name}" and last name "{lastname}"')
def step_create_contact(context, account_name, lastname):
    context.contactpage.createContact(account_name, lastname)
    context.opportunity = Opportunitypage(context.driver)


@when('I create an opportunity with account name "{account_name}" and opportunity name "{opportunity_name}"')
def step_create_opportunity(context, account_name, opportunity_name):
    context.opportunity.createOpportunity(account_name, opportunity_name)
    context.accountspage = Accountspage(context.driver)


@then('I should verify the contact "{contact_name}" under account "{account_name}"')
def step_verify_contact(context, account_name, contact_name):
    context.accountspage.verifyContact(account_name, contact_name)


@then('I should verify the opportunity "{opportunity_name}"')
def step_verify_opportunity(context, opportunity_name):
    context.accountspage.verifyOpportunity(opportunity_name)


@then('I am converting the lead to account successfully by creating new account')
def convert_lead_with_newaccount(browser, context):
    data = input_data()
    context.lead.convertLeadAccount(context, data)
