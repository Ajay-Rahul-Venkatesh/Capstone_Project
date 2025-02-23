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


@given('Login with username "{string}" and password "{string}"')
def step_login(context, username, password):
    context.driver = browser_setup(context)
    context.login = Loginpage(context.driver)
    context.login.loginPage(username, password)
    context.lead = Leadpage(context.driver)


@when('Created a lead with "{string}", last name "{string}", and company "{string}"')
def step_create_lead(context, firstname, lastname, company):
    context.lead.createLead(firstname, lastname, company)


@then('Convert the lead and verify the recently '
      'converted account with first name "{string}", last name "{string}", and company "{string}"')
def step_convert_the_lead_and_verify_recent_account(context, firstname, lastname, company):
    context.lead.convertLead()
    context.account = Accountspage(context.driver)
    context.account.verifyConvertedLead(firstname, lastname, company)


@when('Create an account "{string}"')
def step_create_account(context, account_name):
    context.account = Accountspage(context.driver)
    context.account.createAccount(account_name)
    context.contactpage = Contactspage(context.driver)


@when('Create a contact with account name "{string}" and last name "{string}"')
def step_create_contact(context, account_name, lastname):
    context.contactpage.createContact(account_name, lastname)
    context.opportunity = Opportunitypage(context.driver)


@when('Opportunity named "{string}" is created for account "{string}"')
def step_create_opportunity(context, account_name, opportunity_name):
    context.opportunity.createOpportunity(account_name, opportunity_name)
    context.accountspage = Accountspage(context.driver)


@then('Verify contact "{string}" should be listed under account "{string}"')
def step_verify_contact(context, account_name, contact_name):
    context.accountspage.verifyContact(account_name, contact_name)


@then('The opportunity "{string}" should be verified')
def step_verify_opportunity(context, opportunity_name):
    context.accountspage.verifyOpportunity(opportunity_name)


@then('Converting the lead to account successfully by creating new account')
def convert_lead_with_newaccount(context):
    data = input_data()
    context.lead.convertLeadAccount(context, data)
