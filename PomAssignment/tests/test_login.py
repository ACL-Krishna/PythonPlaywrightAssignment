
from pages.login_page import LoginPage
def test_saucedemo(page_setup):
    login_page = LoginPage(page_setup)
    login_page.open_url()
    page_setup.locator('#user-name').wait_for(state="visible")
    page_setup.screenshot(path="screenshots/screenshot.png") # taking screenshot
    login_page.login('standard_user','secret_sauce')
    print("----------login successful---------------")
