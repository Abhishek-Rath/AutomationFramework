from selenium import  webdriver
import unittest
from pages.home.login_page import LoginPage
import pytest

class LoginTests(unittest.TestCase):
    base_url = 'https://www.letskodeit.com/'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    # driver.get(base_url)
    lp = LoginPage(driver)

    @pytest.mark.order2
    def test_valid_login(self):
        # self.driver.get(self.base_url)
        self.lp.login("abhi.rath39@gmail.com", "abhishek@123")

        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.driver.quit()
    @pytest.mark.order1
    def test_invalid_login(self):
        self.driver.get(self.base_url)
        self.lp.login("abhi.rath39@gmail.com", "yooyoo")
        result = self.lp.verifyLoginFailed()
        assert result == True
        # self.driver.quit()



