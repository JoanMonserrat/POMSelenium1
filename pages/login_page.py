from selenium.webdriver.common.by import By
import time


class login_page:
    def __init__(self, driver):
        self.driver =  driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")


    def login(self):
        self.driver.find_element(*self.username).send_keys("standard_user")
        self.driver.find_element(*self.password).send_keys("secret_sauce")

