import time
from page_objects.internet_uichecks import InternetUiChecks
from page_objects.internet_functionality_checks import InternetFunctionalityChecks
from test_cases.configtest import setup
from utilities.read_properties import ReadConfig

base_url = ReadConfig.get_application_url()

class TestinternetPage:
    """This class specifies UI Checks and functionality checks on the internet application"""

    def test_internet_ui_checks(self, setup):
        """This method specifies UI Checks on the internet page """
        self.driver = setup
        self.driver.get(base_url)
        # Testcase 001
        #Instantiation
        uichecks = InternetUiChecks(self.driver)
        functionalitychecks = InternetFunctionalityChecks(self.driver)
        
        #performing ui checks
        try:   
            uichecks.check_internet_header_label()
            uichecks.check_available_example_header_label()
            uichecks.check_form_authentication_header_label()
            uichecks.check_form_authentication_header_link()
            time.sleep(2)
            functionalitychecks.click_form_authentication_link()
            uichecks.check_login_header_label()
            uichecks.check_username_input_field()
            uichecks.check_password_input_field()
            uichecks.check_login_button()
        except:
            self.driver.close()    
 
    def test_internet_login_successful_functionality_checks(self, setup):
        """This method specifies functionality Checks on the internet page """
        self.driver = setup
        self.driver.get(base_url)
        # Testcase 001
        #Instantiation
        uichecks = InternetUiChecks(self.driver)
        functionalitychecks = InternetFunctionalityChecks(self.driver)
        
        #performing ui checks
        try:   
            functionalitychecks.click_form_authentication_link()
            functionalitychecks.input_validusername()
            functionalitychecks.input_validpassword()
            functionalitychecks.click_login_button()
        except:
            self.driver.close()    

    def test_internet_login_unsuccessful_functionality_checks(self, setup):
        """This method specifies functionality Checks on the internet page """
        self.driver = setup
        self.driver.get(base_url)
        # Testcase 001
        #Instantiation
        uichecks = InternetUiChecks(self.driver)
        functionalitychecks = InternetFunctionalityChecks(self.driver)
        
        #performing ui checks
        try:   
            functionalitychecks.click_form_authentication_link()
            functionalitychecks.input_invalidusername()
            functionalitychecks.input_invalidpassword()
            functionalitychecks.click_login_button()
            time.sleep(2)
            uichecks.check_invalid_login_error_message()
        except:
            self.driver.close()    
 