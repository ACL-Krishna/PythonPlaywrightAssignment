
import pytest

@pytest.fixture(scope="session")
def page_setup(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    yield page
    context.close()
    browser.close()


