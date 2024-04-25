import sys
from configparser import ConfigParser


# CONFIGURATION CLASS
class MediConf:

    def __init__(self):
        # INITIALIZE CONFIGPARSER
        self.config = ConfigParser(strict=True, interpolation=None)
        self.config.read(sys.path[0] + '//config.ini')

        # GLOBAL SECTION
        self.telegram_token = self.config.get('GLOBAL', 'TELEGRAM_TOKEN')
        self.telegram_chat_id = self.config.get('GLOBAL', 'TELEGRAM_CHAT_ID')

        # SHADOW COOKIE SECTION
        self.cookie_button = self.config.get('LOCATORS', 'CLASS_COOKIE_BTN')
        self.shadow_host = self.config.get('LOCATORS', 'ID_SHADOW_HOST')

        # LOGIN SECTION
        self.homepage = self.config.get('LOGIN', 'URL')
        self.redirect_button = self.config.get('LOCATORS', 'XPATH_REDIRECT_BTN')
        self.online_button = self.config.get('LOCATORS', 'XPATH_ONLINE_BTN')
        self.username = self.config.get('LOGIN', 'USERNAME')
        self.password = self.config.get('LOGIN', 'PASSWORD')
        self.username_button = self.config.get('LOCATORS', 'ID_USER_BTN')
        self.password_button = self.config.get('LOCATORS', 'ID_PASSWORD_BTN')
        self.login_button = self.config.get('LOCATORS', 'ID_LOGIN_BTN')
        self.granted_button = self.config.get('LOCATORS', 'XPATH_GRANTED_BTN')

        # SEARCH SECTION
        self.search_button = self.config.get('LOCATORS', 'XPATH_SEARCH_BTN')
        self.search_url = self.config.get('GLOBAL', 'SEARCH_URL')
        self.app_row = self.config.get('LOCATORS', 'CLASS_APP_ROW')
        self.app_time = self.config.get('LOCATORS', 'APP_TIME')
        self.app_localization = self.config.get('LOCATORS', 'APP_LOCALIZATION')
        self.app_doctor = self.config.get('LOCATORS', 'APP_DOCTOR')
