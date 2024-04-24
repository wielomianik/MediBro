from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from module.config import MediConf
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchForVisit:

    def __init__(self):
        self.config = MediConf()
        self.options = Options()

        if self.config.headless:
            self.options.headless = True
        else:
            self.options.headless = False

        self.driver = webdriver.Firefox(options=self.options)

    def login(self):
        # INITIALIZATION FOR LOGIN TO MEDICOVER
        self.driver.get(self.config.homepage)
        self.driver.implicitly_wait(5)

        # ACCEPT COOKIES IF NECESSARY
        try:
            shadow = self.driver.find_element(By.ID, self.config.shadow_host).shadow_root
            shadow.find_element(By.CLASS_NAME, self.config.cookie_button).click()
        except NoSuchElementException:
            pass

        # REDIRECT TO LOGIN PAGE
        self.driver.find_element(By.XPATH, self.config.redirect_button).click()
        WebDriverWait(self.driver, 3).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        redirect_to_wait = EC.presence_of_element_located((By.XPATH, self.config.online_button))
        WebDriverWait(self.driver, 3).until(redirect_to_wait)

        # WAIT UNITL ONLINE BUTTON WOULD BE CLICKABLE
        online_button = self.driver.find_element(By.XPATH, self.config.online_button)
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(online_button))
        online_button.click()
        online_button.send_keys(Keys.ENTER)

        # WAIT UNTIL THERE WOULD BE THREE WINDOWS IF SO SWITCH
        WebDriverWait(self.driver, 3).until(EC.number_of_windows_to_be(3))
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # LOGIN TO MEDICOVER
        login_button = self.driver.find_element(By.ID, self.config.login_button)
        self.driver.find_element(By.ID, self.config.username_button).send_keys(self.config.username)
        self.driver.find_element(By.ID, self.config.password_button).send_keys(self.config.password)
        self.driver.execute_script("arguments[0].removeAttribute('disabled')", login_button)
        login_button.click()

    def search(self):
        # ENTER PAGE FOR SEARCHING APPOINTMENTS
        WebDriverWait(self.driver, 3).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(By.XPATH, self.config.home_button).click()
        self.driver.find_element(By.XPATH, self.config.home_button).send_keys(Keys.ENTER)

        # TRY TO GRANT TO USELESS INFO IF NOT SKIP
        try:
            granted_button = self.driver.find_element(By.XPATH, self.config.granted_button)
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(granted_button))
            granted_button.click()
        except NoSuchElementException:
            pass

        # SEARCHING FOR AN APPOINTMENT
        self.driver.get(self.config.search_url)
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
            (By.XPATH, self.config.search_button)
        )).send_keys(Keys.ENTER)

        # PARSE RESULTS
        app_row = self.driver.find_elements(By.CLASS_NAME, self.config.app_row)
        appointments = []

        if app_row:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(app_row[0]))
            for element in app_row:
                appointments.append(element.get_attribute("innerHTML"))

        return appointments
