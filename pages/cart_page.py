import time

from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


#COnfirm there are 3 products added, remove 1, confirm there are 2, checkout

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.sort_locator = (By.CSS_SELECTOR, ".product_sort_container")
        self.inventory_list = (By.CSS_SELECTOR, ".inventory_list")
        self.inventory_item = (By.CSS_SELECTOR, ".inventory_item")
        self.left_menu = (By.XPATH, '//button[text()="Open Menu"]')
        self.logout_button = (By.ID, "logout_sidebar_link")
        self.first_inventory_item = (By.XPATH, "//div[@class='inventory_list']//div[1]//div[3]//button[1]")
        self.second_inventory_item = (By.XPATH, "//div[@class='inventory_list']//div[2]//div[3]//button[1]")
        self.third_inventory_item = (By.XPATH, "//div[@class='inventory_list']//div[3]//div[3]//button[1]")
        self.number_products = (By.XPATH, "//span[@class='fa-layers-counter shopping_cart_badge']")


    def select_sort_option(self, visible_text):
        sort_list = self.driver.find_element(*self.sort_locator)
        select = Select(sort_list)
        select.select_by_visible_text(visible_text)

    def get_prices_list(self):
        prices = []
        prices_list = self.driver.find_element(*self.inventory_list)
        items = prices_list.find_elements(*self.inventory_item)

        for item in items:
            price_text = item.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
            price_value = float(price_text.replace("$", ""))
            prices.append(price_value)

        return prices

    def logout(self):
        wait = WebDriverWait(self.driver, 10)

        menu_button = wait.until(expected_conditions.element_to_be_clickable(self.left_menu))
        menu_button.click()

        wait.until(expected_conditions.visibility_of_element_located(self.logout_button))
        logout_button = wait.until(expected_conditions.element_to_be_clickable(self.logout_button))
        logout_button.click()

        print("Current URL after logout:", self.driver.current_url)

    def add_3_first_products(self):
        self.driver.find_element(*self.first_inventory_item).click()
        self.driver.find_element(*self.second_inventory_item).click()
        self.driver.find_element(*self.third_inventory_item).click()

        wait = WebDriverWait(self.driver, 10)
        badge = wait.until(expected_conditions.visibility_of_element_located(self.number_products))
        products_in_cart = int(badge.text)

        return products_in_cart











