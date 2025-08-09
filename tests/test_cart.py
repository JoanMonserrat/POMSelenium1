from pages.cart_page import CartPage
from pages.login_page import LoginPage


def test_order_price(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    cart = CartPage(driver)
    cart.select_sort_option("Price (low to high)")

    prices_list = cart.get_prices_list()
    assert prices_list == sorted(prices_list)


