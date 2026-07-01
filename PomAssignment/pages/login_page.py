
class LoginPage:
    def __init__(self,page):
        self.page=page
        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"


    def open_url(self):
        self.page.goto("https://saucedemo.com")
        self.page.locator(self.username).wait_for(state="visible")

    # def get_username_placeholder(self):
    #     username_placeholder = self.page.locator('#user-name').get_attribute("placeholder")
    #     return username_placeholder
    #
    # def get_password_placeholder(self):
    #     password_placeholder = self.page.locator('#password').get_attribute("placeholder")
    #     return password_placeholder

    def login(self,username,password):
        self.page.fill(self.username,username)
        self.page.fill(self.password,password)
        self.page.click(self.login_button)