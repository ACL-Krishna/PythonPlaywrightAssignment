
class CartPage:
    def __init__(self,page):
        self.page=page
        self.checkout = "#checkout"

    def click_checkout(self):
        self.page.click(self.checkout)


