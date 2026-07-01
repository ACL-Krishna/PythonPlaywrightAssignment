
import pytest

@pytest.fixture(scope="session")
def page_setup(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    yield page
    context.close()
    browser.close()


