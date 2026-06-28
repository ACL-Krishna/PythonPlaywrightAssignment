import pytest
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright, expect

# ------Open Google, verify title using pytest ------
def test_validate_google_login(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://google.com")
    print("Title of the page is : ", page.title())
    assert page.title() == "Google" , f"Expected 'Google', got '{page.title()}'"


# -------Open saucedemo.com, locate username/password/login, print placeholder------
def test_saucedemo(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://saucedemo.com")  #opening saucedemo.com,
    page.locator('input[id=user-name]').wait_for(state="visible", timeout=10000)
    username_placeholder = page.locator('#user-name').get_attribute("placeholder")
    print(f"Username_Placeholder : {username_placeholder}") #printing username placeholder
    password_placeholder = page.locator('#password').get_attribute("placeholder")
    print(f"Password_Placeholder : {password_placeholder}") #printing password placeholder
    page.fill('input[id=user-name]', 'standard_user') # locating username
    page.fill('input[id="password"]', 'secret_sauce') # locating password
    page.click('input[id="login-button"]') # locating login


# ----------Perform login, validate success & error scenarios---------
def test_login(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://saucedemo.com")
    page.locator('input[id=user-name]').wait_for(state="visible", timeout=10000)
    page.fill('input[id=user-name]', 'standard_user')
    page.fill('input[id="password"]', 'secret_sauce')
    page.click('input[id="login-button"]')
    print("----------login successful-------")
    assert page.title() == "Swag Labs", f"Expected 'Swag Labs', got '{page.title()}'"
    #-------error scenarios-------
    #assert page.title() == "Swag Lab", f"Expected 'Swag Labs', got '{page.title()}'"


# ---------Verify title, inventory visibility, product count ≥ 6 -----
def test_saucedemo(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://saucedemo.com")
    page.locator('input[id=user-name]').wait_for(state="visible", timeout=10000)
    page.fill('input[id=user-name]', 'standard_user')
    page.fill('input[id="password"]', 'secret_sauce')
    page.click('input[id="login-button"]')
    #verify title
    assert page.title() == "Swag Labs", f"Expected 'Swag Labs', got '{page.title()}'"
    # verify inventory is visible
    assert page.locator(".inventory_item").count() > 0
    products = page.locator(".inventory_item")
    #verify product count >=6
    total_count = products.count()
    print("Total products on page are :", total_count)
    assert total_count >= 6 , f"Expected at least 6 products, found {total_count}"


#  -------Sort products, add items, validate cart of saucedemo.com in python with playwright----
def test_saucedemo(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://saucedemo.com")
    page.locator('input[id=user-name]').wait_for(state="visible", timeout=10000)
    page.fill('input[id=user-name]', 'standard_user')
    page.fill('input[id="password"]', 'secret_sauce')
    page.click('input[id="login-button"]')
    #-----------Add items---------------
    add_items = page.locator(".inventory_item_name").all_text_contents()
    add_items.append("laptop")
    add_items.append("mobile")
    add_items.append("keyboard")
    #-----------------sort products--------------
    print("---------before sort------------")
    print(add_items)
    add_items.sort()
    print()
    print("---------after sort------------")
    print(add_items)
    #-------------validate cart------------
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator("#add-to-cart-sauce-labs-bike-light").click()
    page.locator(".shopping_cart_link").click()
    cart = page.locator(".cart_item").count()
    print()
    print("Total item added to cart are : ", cart)
    assert cart == 2 , f" Expected 2 items in cart, but found {cart}"

# --------Checkout flow, validate confirmation------
def test_saucedemo(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://saucedemo.com")
    page.locator('input[id=user-name]').wait_for(state="visible", timeout=10000)
    page.fill('input[id=user-name]', 'standard_user')
    page.fill('input[id="password"]', 'secret_sauce')
    page.click('input[id="login-button"]')  # login
    page.locator("#add-to-cart-sauce-labs-backpack").wait_for(state="visible", timeout=10000)
    page.locator("#add-to-cart-sauce-labs-backpack").click() # Add product to cart
    page.locator("#add-to-cart-sauce-labs-bike-light").click() # Add product to cart
    page.locator(".shopping_cart_link").click() #open cart
    page.locator("#checkout").wait_for(state="visible", timeout=10000)
    page.locator("#checkout").click()
    page.locator("#first-name").wait_for(state="visible", timeout=10000)
    page.fill("#first-name","Raj")
    page.fill("#last-name", "Sharma")
    page.fill("#postal-code", "411045")
    page.locator("#continue").click()
    page.locator("#finish").click()
    confirmation_text = page.locator(".complete-header").text_content()
    print(confirmation_text)
    assert confirmation_text == "Thank you for your order!"
    print("order placed successfully")


