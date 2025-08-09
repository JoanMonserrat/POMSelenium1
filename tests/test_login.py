from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


def test_login_successfully(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

def test_wrong_credentials(driver):
    login = LoginPage(driver)
    login.login("wrong_credential", "wrong_credential")
    error_wrong_credentials = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]').text
    assert error_wrong_credentials == "Epic sadface: Username and password do not match any user in this service"

def test_blank_username(driver):
    login = LoginPage(driver)
    login.login("", "secret_sauce")
    error_blank_username = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]').text
    assert error_blank_username == "Epic sadface: Username is required"
