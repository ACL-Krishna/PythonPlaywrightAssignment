"""
#  -----Load product data from JSON file------

import json

json_string = '''{"students": [
             {"id":1,
             "name": "krishna",
             "age":35
             },
             
             {"id":2,
             "name":"ram",
             "age":39
             }
]
}
'''

#print(json_string)
data = json.loads(json_string)
print(data)
print(data["students"])
print(data["students"][0])
print(data["students"][0]["id"])
"""


"""
#   --------Modify login to handle incorrect input via exceptions-------

try:
    Valid_Username = "krishna"
    Valid_Password = "@123"

    username = input("Enter username")
    pwd = input("Enter password")

    if username == Valid_Username and pwd == Valid_Password:
        print("--login successful---")

    else:
        raise Exception("invalid username or password")


except Exception as e:
    print(e)
print("-----end of try except block----------")
"""



"""
#  ---------Build Login class with validation method--------

class Login:

    def __init__(self):
        self.username = "krishna"
        self.password = "@123"


    def validate(self,user,pwd):
        if user == self.username and pwd == self.password:
            print("login successful")

        else:
            print("invalid username or password")


obj = Login()
username = input("Enter username")
password = input("Enter password")
obj.validate(username,password)

"""


"""
# --------Create reusable login module--------
import pythonAssignments
obj = pythonAssignments.Login()
username = input("Enter username")
password = input("Enter password")
obj.validate(username,password)
"""

"""
# ---------Call GET API and print response--------
import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
print("status code:", response.status_code)
print(response)
print(response.text)
"""


"""
#    --------Filter products with price < 50 -------

products =[

    {"id":1, "name" : "pen", "price" : 10},
    {"id":2, "name" : "book", "price" : 90},
    {"id":3, "name" : "pencil", "price" : 20},
    {"id":3, "name" : "bag", "price" : 200}
]

filter_products = [product for product in products if product["price"]<50]

print(filter_products)

"""
