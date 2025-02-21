Feature: Lead and Account Management
  To test the creation, conversion, and verification of leads, accounts, contacts, and opportunities.

  Scenario: Lead Creation and Conversion
    Given I log in to the application with username "ajayRahul-mal0@force.com" and password "ajayRahul@123"
    When I create a lead with first name "Ajay", last name "Rahul", and company "Tiger"
    And I convert the lead
    Then I should verify the recently converted account with first name "ajay", last name "Rahul", and company "Tiger"

  Scenario: Lead Creation and Conversion by create new account
    Given I log in to the application with username "ajayRahul-mal0@force.com" and password "ajayRahul@123"
    When I create a lead with first name "Ajay", last name "Rahul", and company "Tiger"
    Then I am converting the lead to account successfully by creating new account

  Scenario: Account, Contact, and Opportunity Management
    Given I log in to the application with username "ajrahul80-yhef@force.com" and password "Baba@123"
    When I create an account with name "ajay"
    And I create a contact with account name "ajay" and last name "Rahul"
    And I create an opportunity with account name "ajay" and opportunity name "XYZ"
    Then I should verify the contact "Rahul" under account "ajay"
    And I should verify the opportunity "XYZ"
