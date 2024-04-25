from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from module.config import MediConf
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MediCover:

    def __init__(self):
        self.config = MediConf()
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.set_window_size(3440, 1440)

    def login(self) -> None:
        # INITIALIZATION FOR LOGIN TO MEDICOVER
        self.driver.get(self.config.homepage)
        self.driver.implicitly_wait(3)

        # ACCEPT COOKIES IF NECESSARY
        try:
            shadow = self.driver.find_element(By.ID, self.config.shadow_host).shadow_root
            shadow.find_element(By.CLASS_NAME, self.config.cookie_button).click()
        except NoSuchElementException:
            pass

        # REDIRECT TO SECOND PAGE
        self.driver.find_element(By.XPATH, self.config.redirect_button).click()
        WebDriverWait(self.driver, 3).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # CLICK ON PROBLEMATIC LOGIN BUTTON THAT IS REDIRECTING TO ANOTHER THIRD WINDOW
        while True:
            if len(self.driver.window_handles) == 2:
                WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable(
                        self.driver.find_element(By.XPATH, self.config.online_button)
                    )
                ).send_keys(Keys.ENTER)
                self.driver.implicitly_wait(3)
            else:
                break

        # WAIT UNTIL THERE WOULD BE THREE WINDOWS IF SO SWITCH
        WebDriverWait(self.driver, 3).until(EC.number_of_windows_to_be(3))
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # PROVIDE USERNAME
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(
                self.driver.find_element(By.ID, self.config.username_button)
            )
        ).send_keys(self.config.username)

        # PROVIDE PASSWORD
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(
                self.driver.find_element(By.ID, self.config.password_button)
            )
        ).send_keys(self.config.password)

        # CLICK ON LOGIN BUTTON AND LOG IN
        login_button = self.driver.find_element(By.ID, self.config.login_button)
        self.driver.execute_script("arguments[0].removeAttribute('disabled')", login_button)
        login_button.click()

    def search(self) -> list:
        # ENTER PAGE FOR SEARCHING APPOINTMENTS
        WebDriverWait(self.driver, 3).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # TRY TO GRANT TO USELESS INFO IF PRESENCE
        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    self.driver.find_element(By.XPATH, self.config.granted_button)
                )
            ).click()
        except NoSuchElementException:
            pass

        # SEARCHING FOR AN APPOINTMENT
        self.driver.get(self.config.search_url)
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
            (By.XPATH, self.config.search_button)
        )).send_keys(Keys.ENTER)

        # PARSE RESULTS
        app_row, appointments = self.driver.find_elements(By.CLASS_NAME, self.config.app_row), []
        if app_row:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(app_row[0]))
            for element in app_row:
                appointments.append(element.get_attribute("innerHTML"))
        return appointments

    def close(self):
        self.driver.quit()
