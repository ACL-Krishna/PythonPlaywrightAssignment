
import pytest
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright, expect

#       -------pytest fixture ----------
@pytest.fixture(scope="session")
def login_once(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator('input[name=username]').wait_for(state="visible", timeout=10000)
    page.fill('input[name=username]', 'Admin')
    page.fill('input[type=password]', 'admin123')
    page.locator('input[name=username]').wait_for(state="visible", timeout=10000)
    page.click('button[type=submit]')
    yield page
    browser.close()

def test_dashboard(login_once):
    page = login_once
    assert page.title() == "OrangeHRM" , f"Expected 'OrangeHRM', got '{page.title()}'"

def test_admin(login_once):
    page = login_once
    page.click("text=Admin")
    page.locator('(//input[@class="oxd-input oxd-input--active"])[2]').fill("raj")
    select=page.locator('(//div[@class="oxd-select-text--after"])[1]')
    select.click()

def test_pim(login_once):
    page = login_once
    page.click("text=PIM")


#       --------  Parallel Execution  ----------
def test_validate_google_login(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://google.com")
    print(f"Title of google login page : {page.title()}")
    assert page.title() == "Google" , f"Expected 'Google', got '{page.title()}'"

def test_validate_login_saucedemo(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://saucedemo.com")
    page.locator('input[id=user-name]').wait_for(state="visible", timeout=10000)
    page.fill('input[id=user-name]', 'standard_user')
    page.fill('input[id="password"]', 'secret_sauce')
    page.click('input[id="login-button"]')
    print(f"Title of saucedemo login page : {page.title()}")
    assert page.title() == 'Swag Labs' , f"Expected 'Swag Labs , got {page.title()}"
    # command for parallel execution : pytest -v -s -n 2 day6assignment.py

