import time
import pytest
from pages.cart_page import CartPage
from pages.login_page import LoginPage

@pytest.mark.skip(reason="Temporarily disabled, flaky test that sometimes fails")
def test_logout(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    cart = CartPage(driver)
    cart.logout()

    assert "index.html" in driver.current_url

def test_order_price(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    cart = CartPage(driver)
    cart.select_sort_option("Price (low to high)")

    prices_list = cart.get_prices_list()
    assert prices_list == sorted(prices_list)

#@pytest.mark.skip(reason="Temporarily disabled, flaky test that sometimes fails")
def test_add_products(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    cart = CartPage(driver)
    cart.select_sort_option("Price (low to high)")

    products_in_cart = cart.add_3_first_products()
    assert products_in_cart == 3

def test_remove_product_inventory(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    cart = CartPage(driver)
    cart.select_sort_option("Price (low to high)")
    products_in_cart = cart.add_3_first_products()
    print("Products in cart after add:", products_in_cart)
    products_in_cart = cart.remove_first_product()

    assert products_in_cart == 2


