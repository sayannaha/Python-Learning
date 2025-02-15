global user_name
global interest
cart = []
def getUser():
    return user_name
def buyProducts(user_name):
    if(user_name):
        return True
def getCategory():
    categories = ["MOBILE", "ELECTRONICS", "FASHION", "EARPHONES", "COMPUTER"]
    if(categories.__contains__ (interest)):
        return interest
    else:
        return None
def getProducts():
    if(getCategory()):
        if(interest == "MOBILE"):
            mobiles = ["APPLE IPHOEN 13", "SAMSUNG S22", "GOOGLE PIXEL 8", "ONEPLUS 11"]
            return mobiles
        elif(interest == "ELECTRONICS"):
            electronics = ["TV", "WASHING MACHINE", "CHIMNEY", "AC", "CHARGERS"]
            return electronics
        elif(interest == "FASHION"):
            clothes = ["JEANS", "T-SHIRT", "SHIRTS", "BLAZERS", "JACKETS", "FORMAL TROUSERS"]
            return clothes
        elif(interest == "EARPHONES"):
            clothes = ["OPPO", "APPLE", "SAMSUNG", "MOTO", "ONEPLUS", "NOTHING"]
            return clothes
        elif(interest == "COMPUTER"):
            clothes = ["APPLE", "HP", "LENOVO", "SAMSUNG", "DELL", "INFINIX"]
            return clothes
        else:
            return None
def addToCart(product):
    cart.append(product)
user_name = "sayannaha"
interest = input("Enter the kind of Product you want to Buy: ")
all_products = getProducts()
if(all_products):
    print(all_products)
    product = input("Choose a Product From Above: ")
    addToCart(product)
for item in cart:
    print("Product Added to Cart: " + item + ", for user " + user_name)