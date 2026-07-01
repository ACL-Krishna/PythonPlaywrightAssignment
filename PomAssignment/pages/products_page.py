

class ProductsPage:
    def __init__(self,page):
        self.page=page
        self.backpack = "#add-to-cart-sauce-labs-backpack"
        self.bike_light = "#add-to-cart-sauce-labs-bike-light"
        self.cart = ".shopping_cart_link"


    def add_products(self):
        self.page.click(self.backpack)
        self.page.click(self.bike_light)

    def open_cart(self):
        self.page.click(self.cart)