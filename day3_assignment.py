
#    -----Day3Assignment----
# Build system:
# - Login module
# - Product list
# - Cart system
# - Checkout logic

Valid_Username = "krishna"
Valid_Password = "@123"
username = input("Enter username")
pwd      = input("Enter password")
if username == Valid_Username and pwd == Valid_Password :
    print("--login successful---")
    products = ["laptop","mobile","mouse","keyboard","headphones"]
    print("\nAvailable products:")
    for product in products:
        print(product)
    print()
    cart = []
    item1 = input("Enter first item")
    cart.append(item1)
    item2 = input("Enter second item")
    cart.append(item2)
    item3 = input("Enter third item")
    cart.append(item3)
    print("\nitems in cart")
    for item in cart:
        print(item)
    choice = input("Proceed to checkout?(yes/no):")
    if choice == "yes":
        print("checkout successful")
        print("thank you for shopping")
    else:
        print("checkout canceled")

else:
    print("Invalid username or password")

