from selenium import  webdriver
from selenium.webdriver.common.by import By

import unittest
from pages.home.login_page import LoginPage

class LoginTests(unittest.TestCase):

    def test_valid_login(self):
        base_url = 'https://www.letskodeit.com/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)

        lp = LoginPage(driver)
        lp.login("abhi.rath39@gmail.com", "abhishek@123")

        user_icon = driver.find_element(By.XPATH, "//img[@class='zl-navbar-rhs-img ']")
        if user_icon is not None:
            print("login successful")
        else:
            print("login failed")


