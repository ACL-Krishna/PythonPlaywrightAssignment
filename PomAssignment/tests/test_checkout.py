
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.json_reader import read_json

def test_checkout(page_setup):
    login_data = read_json("test_data/login_data.json")
    checkout_data = read_json("test_data/checkout_data.json")
    login = LoginPage(page_setup)
    product =ProductsPage(page_setup)
    cart =CartPage(page_setup)
    checkout = CheckoutPage(page_setup)
    login.open_url()
    login.login(login_data["valid_user"]["username"],login_data["valid_user"]["password"])
    page_setup.screenshot(path="screenshots/screenshot.png")
    product.add_products()
    product.open_cart()
    cart.click_checkout()
    checkout.enter_details(checkout_data["checkout_user"]["first_name"],
                           checkout_data["checkout_user"]["last_name"],
                           checkout_data["checkout_user"]["postal_code"])
    checkout.finish_order()
    assert checkout.get_confirmation_text() == "Thank you for your order!"
