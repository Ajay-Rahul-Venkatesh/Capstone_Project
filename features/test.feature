Feature: Lead and Account Management
  To test the creation, conversion, and verification of leads, accounts, contacts, and opportunities.

  Scenario Outline: Convert a lead and verify the converted account
    Given Login with username "<username>" and password "<password>"
    When Created a lead with "<first_name>", last name "<last_name>", and company "<company>"
    Then Convert the lead and verify the recently converted account with first name "<first_name>", last name "<last_name>", and company "<company>"

    Examples:
    | username                      | password          | first_name | last_name | company        |
    | ajayRahul-mal0@force.com      | ajayRahul@123    | Ajay       | Rahul     | Tiger         |

  Scenario Outline: Lead Creation and Conversion by creating a new account
    Given Login with username "<username>" and password "<password>"
    When Created a lead with "<first_name>", last name "<last_name>", and company "<company>"
    Then Converting the lead to an account successfully by creating a new account

    Examples:
      | username                      | password       | first_name | last_name | company |
      | ajayRahul-mal0@force.com      | ajayRahul@123 | Ajay       | Rahul     | Tiger   |

  Scenario Outline: Account, Contact, and Opportunity Management
    Given Login with username "<username>" and password "<password>"
    When Create an account "<account_name>"
    And Create a contact with account name "<account_name>" and last name "<contact_last_name>"
    And Opportunity named "<opportunity_name>" is created for account "<account_name>"
    Then Verify contact "<contact_last_name>" should be listed under account "<account_name>"
    And The opportunity "<opportunity_name>" should be verified

    Examples:
      | username                    | password  | account_name | contact_last_name | opportunity_name |
      | ajrahul80-yhef@force.com    | Baba@123 | ajay         | Rahul             | XYZ              |
