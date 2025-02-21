from pages.homepage import Homepage
from utilities.BaseClass import Baseclass


class Test(Baseclass):

    def setup_method(self, method):
        self.home = Homepage(self.driver)

    def test_login(self, browser_setup):
        self.driver = browser_setup
        self.home = Homepage(self.driver)
        self.home.login("ajrahul80-yhef@force.com", "Baba@123")

    def test_generate_lead(self):
        self.home.create_lead("Ajay", "Rahul", "Tiger")

    def test_modify_lead(self):
        self.home.convert_lead()

    def test_verify_new_account(self):
        self.home.verify_converted_lead("Ajay", "Rahul", "Tiger")

    def test_create_account(self):
        self.home.create_account("Ajay")

    def test_create_new_contact(self):
        self.home.create_contact("Ajay", "Rahul")

    def test_create_new_opportunity(self):
        self.home.create_opportunity("Ajay", "XYZ")

    def test_verify_new_contact(self):
        self.home.verify_contact("Ajay", "Rahul")

    def test_verify_new_opportunity(self):
        self.home.verify_opportunity("XYZ")
