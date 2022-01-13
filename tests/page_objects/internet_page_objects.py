class InternetElements:
    """Elements on the internet page"""
    internet_header_xpath = "//h1[normalize-space()='Welcome to the-internet']"
    available_example_xpath = "//h2[normalize-space()='Available Examples']"
    form_authentication_xpath = "//a[normalize-space()='Form Authentication']"
    login_page_header_xpath = "//h2[normalize-space()='Login Page']"
    username_input_field_xpath = "//input[@id='username']"
    password_input_field_xpath = "//input[@id='password']"
    login_button_xpath = "//button[@type='submit']"
    error_message_xpath = "//div[@id='flash']"
