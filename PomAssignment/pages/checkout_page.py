
class CheckoutPage:
    def __init__(self,page):
        self.page=page
        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.postal_code = "#postal-code"
        self.continue_btn = "#continue"
        self.finish_btn   = "#finish"
        self.confirmation = ".complete-header"


    def enter_details(self, fname, lname,code):
        self.page.fill(self.first_name,fname)
        self.page.fill(self.last_name, lname)
        self.page.fill(self.postal_code,code)

    def finish_order(self):
        self.page.click(self.continue_btn)
        self.page.click(self.finish_btn)

    def get_confirmation_text(self):
        return self.page.locator(self.confirmation).text_content()

