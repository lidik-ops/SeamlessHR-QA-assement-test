import configparser

config = configparser.RawConfigParser()
config.read("../tests/configurations/config.ini")

class ReadConfig:
    """This class consists of methods that retrieve information from the configuration file"""
    @staticmethod
    def get_application_url():
        """This method retrieves the URL from config file"""
        url = config.get('Common required information', 'base_url')
        return url

    @staticmethod
    def get_internet_page_title():
        internet_page_title = config.get(
            'Common required information',
            'internet_page_title'
        )
        return internet_page_title
