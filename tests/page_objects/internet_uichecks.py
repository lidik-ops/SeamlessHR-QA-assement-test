from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from .internet_page_objects import InternetElements

#instantiating internet page elements
internet_elements = InternetElements

class InternetUiChecks(BasePage):
    """Class describes ui test actions for internet Page"""
    def check_internet_header_label(self):
        """ Method tests for internet header label """
        element = internet_elements.internet_header_xpath
        self.driver.find_element(By.XPATH, element).is_displayed()
        internet_label_txt = self.driver.find_element(By.XPATH, element).text
        assert internet_label_txt == "Welcome to the-internet"

    def check_available_example_header_label(self):
        """ Method tests for available example header label """
        element = internet_elements.available_example_xpath
        self.driver.find_element(By.XPATH, element).is_displayed()
        availablle_label_txt = self.driver.find_element(By.XPATH, element).text
        assert availablle_label_txt == "Available Examples"

    def check_form_authentication_header_label(self):
        """ Method tests for form authentication link title  label """
        element = internet_elements.form_authentication_xpath
        self.driver.find_element(By.XPATH, element).is_displayed()
        form_authentication_label_txt = self.driver.find_element(By.XPATH, element).text
        assert form_authentication_label_txt == "Form Authentication"

    def check_form_authentication_header_link(self):
        """ Method tests if form authentication link is enabled """
        element = self.driver.find_element(
            By.XPATH,
            internet_elements.form_authentication_xpath
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )
        element.is_displayed()
        element.is_enabled()

    def check_login_header_label(self):
        """ Method tests for login title label """
        element = internet_elements.login_page_header_xpath
        self.driver.find_element(By.XPATH, element).is_displayed()
        login_label_txt = self.driver.find_element(By.XPATH, element).text
        assert login_label_txt == "Login Page"

    def check_username_input_field(self):
        """ Method tests if username input field is enabled """
        element = self.driver.find_element(
            By.XPATH,
            internet_elements.username_input_field_xpath
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )
        element.is_displayed()
        element.is_enabled()

    def check_password_input_field(self):
        """ Method tests if password input field is enabled """
        element = self.driver.find_element(
            By.XPATH,
            internet_elements.password_input_field_xpath
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )
        element.is_displayed()
        element.is_enabled()

    def check_login_button(self):
        """ Method tests if login button is enabled """
        element = self.driver.find_element(
            By.XPATH,
            internet_elements.login_button_xpath
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )
        element.is_displayed()
        element.is_enabled()

    def check_invalid_login_error_message(self):
        """ Method tests for error message """
        element = internet_elements.error_message_xpath
        self.driver.find_element(By.XPATH, element).is_displayed()
        error_message_txt = self.driver.find_element(By.XPATH, element).text
        assert error_message_txt == " Your username is invalid!"
