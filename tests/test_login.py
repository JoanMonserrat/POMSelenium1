from selenium import webdriver

from pages.login_page import login_page

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")

def test_login_successfully():
login = login_page(driver)
login.login()

def test_wrong_credentials():

def test_blank_username():

def test_blank_password():