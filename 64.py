# Python Program to Manage a Mobile Phone Dictionary Using Functions (Add, Search, Remove, and Sort Phones by Price).


phone_price = {}
def add_phone(name,price):
    phone_price[name]=price
    print(f"Added{name} with price ${price}")
    
def search_phone(name):
    if name in phone_price:
        return f"the price of {name} is ${phone_price[name]}"
    else:
        return f"{name} not found in the dictionary."
    
def find_phones_by_price(price):
    matching_phone=[phone for phone,p in phone_price.items() if p==price]
    if matching_phone:
        return f"phone with price ${price}:{','.join(matching_phone)}"
    else:
        return f"not phone found with price ${price}."
    
def remove_phone(name):
    if name in phone_price:
        del phone_price[name]
        print(f"removed{name} from the dictionary.")
    else:
        print(f"{name} not found in the dictionary,cannot removed.")

def display_all_phone_sorted():
    if not phone_price:
        print("The dictionary is empty.")
        return
    sorted_phone=sorted(phone_price.items(),key=lambda items:items[1])
    print("All phone sorted  by price:")
    print(sorted_phone)
    for name,price in sorted_phone:
        print(f"-{name}:${price}")
        
add_phone("iphone 15",999)
add_phone("samsung Galaxy$24",899)
add_phone("Google pixel 8",799)
add_phone("onePlus 8",799)

print(search_phone("iphone 15"))
print(search_phone("Nokia 3310"))

print(find_phones_by_price(799))
print(find_phones_by_price(500))

remove_phone("Samsung Galaxy $24")
remove_phone("Xiaomi Mi 13")

display_all_phone_sorted()


