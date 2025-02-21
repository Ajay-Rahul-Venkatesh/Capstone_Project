from selenium.webdriver.common.by import By


class Locators:
    username = (By.XPATH, "//div/input[@id='username']")
    password = (By.XPATH, "//input[@id='password']")
    login = (By.XPATH,"//input[@id='Login']")
    lead_header = (By.XPATH,"(//span[@class='slds-truncate'])[3]")
    lead_dropdown = (By.XPATH, "(//a[@class='slds-button slds-button_reset'])[1]")
    new_lead_icon = (By.XPATH,"(//div[@class='menuItemsWrapper']//a)[1]")
    salutation = (By.XPATH,"//button[@name='salutation']")
    salutation_option = (By.XPATH,"//span[text()='Mr.']")
    firstname = (By.XPATH,"//input[@name='firstName']")
    lastname = (By.XPATH,"//input[@name='lastName']")
    company = (By.XPATH,"//input[@name='Company']")
    saveedit = (By.XPATH,"//button[@name='SaveEdit']")
    convert_dropdown = (By.XPATH,"//span[text()='Show more actions']/parent::button")
    convert_text = (By.XPATH,"//span[text()='Convert']/parent::a")
    convert_title = (By.XPATH, "//div[@class='title']")
    convert_button = (By.XPATH,"//button[text()='Convert']/parent::span")
    close_window = (By.XPATH,"//button[@title='Close this window']")
    go_to_leads = (By.XPATH,"//button[@class='slds-button slds-button_brand']")
    accounts_dropdown = (By.XPATH,"(//a[@class='slds-button slds-button_reset'])[2]")
    new_account_icon = (By.XPATH,"//span[text()='New Account']")
    account_name_field = (By.XPATH,"//input[@name='Name']")
    contact_dropdown = (By.XPATH, "(//a[@class='slds-button slds-button_reset'])[3]")
    new_contact_icon = (By.XPATH, "//span[text()='New Contact']")
    search_icon = (By.XPATH,"//flexipage-field[@data-field-id='RecordAccountIdField']//lightning-icon[@icon-name='utility:search']")
    opportunity_dropdown = (By.XPATH, "(//a[@class='slds-button slds-button_reset'])[4]")
    new_opportunity_icon = (By.XPATH, "//span[text()='New Opportunity']")
    opportunity_name_field = (By.XPATH,"//input[@name='Name']")
    opportunity_date_field = (By.XPATH,"//input[@name='CloseDate']")
    stage_dropdown = (By.XPATH,"//button[@aria-label='Stage']")
    qualification_option=(By.XPATH,"//lightning-base-combobox-item[@data-value='Qualification']/span[@class='slds-media__body']")
    @staticmethod
    def recent_method(text):
        recent_account=(By.XPATH,f"//span[text()='{text}']/parent::span/parent::a")
        return recent_account

    @staticmethod
    def recentAccountName(text):
        account_name=(By.XPATH,f"(//span[text()='{text}']/parent::span/parent::span/parent::lightning-base-combobox-item/parent::li)[1]")
        return account_name

    @staticmethod
    def contactOrOpportunity(text):
        contact_or_opportunity=(By.XPATH,f"//slot[text()='{text}']")
        return contact_or_opportunity

    account_name=(By.XPATH,"(//a[@class='slds-truncate']/span/slot/span/slot)[1]")
    # contact_link=(By.XPATH,"((//records-hoverable-link[@class='slds-grow']//a))[2]")
    # opportunity_link=(By.XPATH,"((//records-hoverable-link[@class='slds-grow']//a))[3]")
    # contact_name=(By.XPATH,"//lightning-formatted-name[@slot='primaryField']")
    # opportunity_name=(By.XPATH,"(//lightning-formatted-text[@slot='primaryField'])[2]")

