from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#COnfirm there are 3 products added, remove 1, confirm there are 2, checkout

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.sort_locator = (By.CSS_SELECTOR, ".product_sort_container")
        self.inventory_list = (By.CSS_SELECTOR, ".inventory_list")
        self.inventory_item = (By.CSS_SELECTOR, ".inventory_item")

    def select_sort_option(self, visible_text):
        sort_list = self.driver.find_element(*self.sort_locator)
        select = Select(sort_list)
        select.select_by_visible_text(visible_text)

    def get_prices_list(self):
        prices = []
        prices_list = self.driver.find_elements(*self.inventory_list)
        items = prices_list.find_elements(*self.inventory_item)

        for item in items:
            price_text = item.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
            price_value = float(price_text.replace("$", ""))
            prices.append(price_value)

        return prices







