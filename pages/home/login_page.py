from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):

    log = cl.custom_logger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//a[normalize-space()='Sign In']"
    _email_field = "email"
    _password_field = "login-password"
    _login_button = "login"

    # def getLoginLink(self):
    #     return self.driver.find_element(By.XPATH, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.ID, self._login_button)

    # Actions
    def clickLoginLink(self):
        # self.getLoginLink().click()
        self.elementClick(self._login_link, "XPATH")
    def enterEmail(self, email):
        # self.getEmailField().send_keys(email)
        self.sendKeys(email, self._email_field, "id")
    def enterPassword(self, password):
        # self.getPasswordField().send_keys(password)
        self.sendKeys(password, self._password_field, "id")
    def clickLoginButton(self):
        # self.getLoginButton().click()
        self.elementClick(self._login_button, "id")
    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()