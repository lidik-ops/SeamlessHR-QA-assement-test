from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from .internet_page_objects import InternetElements
from configurations.test_data import LoginTestData
from selenium.webdriver.common.keys import Keys

#instantiating internet page elements
internet_elements = InternetElements

#instantiating internet test data
test_data = LoginTestData()

class InternetFunctionalityChecks(BasePage):
    """Class describes functionality test actions for internet Page"""
    def click_form_authentication_link(self):
        """ Method tests if the form authentication link can be clicked """
        element = internet_elements.form_authentication_xpath
        form_authentication_link = self.driver.find_element(By.XPATH, element)
        self.driver.execute_script("arguments[0].click();",
                                    form_authentication_link)

    def input_validusername(self):
        """ Method tests if username field can be clicked """
        element = internet_elements.username_input_field_xpath
        user = test_data.valid_username
        self.driver.find_element(By.XPATH,
                                 element).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, element).send_keys(Keys.DELETE)
        self.driver.find_element(By.XPATH, element).send_keys(user)

    def input_validpassword(self):
        """ Method tests if password field can be clicked """
        element = internet_elements.password_input_field_xpath
        user = test_data.valid_password
        self.driver.find_element(By.XPATH,
                                 element).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, element).send_keys(Keys.DELETE)
        self.driver.find_element(By.XPATH, element).send_keys(user)
    
    #invalid credentials
    def input_invalidusername(self):
        """ Method tests if invalid username field can be clicked """
        element = internet_elements.username_input_field_xpath
        user = test_data.invalid_username
        self.driver.find_element(By.XPATH,
                                 element).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, element).send_keys(Keys.DELETE)
        self.driver.find_element(By.XPATH, element).send_keys(user)

    def input_invalidpassword(self):
        """ Method tests if invalid password field can be clicked """
        element = internet_elements.password_input_field_xpath
        user = test_data.invalid_password
        self.driver.find_element(By.XPATH,
                                 element).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, element).send_keys(Keys.DELETE)
        self.driver.find_element(By.XPATH, element).send_keys(user)

    def click_login_button(self):
        """ Method tests if the login button can be clicked """
        element = internet_elements.login_button_xpath
        login_button = self.driver.find_element(By.XPATH, element)
        self.driver.execute_script("arguments[0].click();",
                                    login_button)
