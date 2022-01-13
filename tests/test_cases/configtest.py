import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def setup():
    """This method runs before every test method."""

    # Run tests in Headless Chrome
    options = webdriver.ChromeOptions()
    try :
        options.headless = False
        chrome_prefs = {}
        options.experimental_options["prefs"] = chrome_prefs
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
  
    except:
        options.headless = True
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--dist=loadfile")
        chrome_prefs = {}
        options.experimental_options["prefs"] = chrome_prefs
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


    driver.implicitly_wait(20)
    driver.maximize_window()
    
    return driver
