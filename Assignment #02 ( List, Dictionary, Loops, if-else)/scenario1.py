grocery_list = []


# Display Grocery List

def get_grocery_list():
    grocery_text = ""
    for index, item in enumerate(grocery_list):
        grocery_text += f"\nItem#: {index + 1} Name: {item['name']} Quantity: {item['quantity']} Price: Rs{item['price']}"

    if len(grocery_list) == 0:
        grocery_text = "No items found"

    return grocery_text


# Add Item

def add_item():
    name = input("\nEnter item name: ")
    quantity = input("Enter item quantity: ")
    price = input("Enter item price: ")
    item = {"name": name, "price": price, "quantity": quantity}
    grocery_list.append(item)
    return get_grocery_list()


# Delete Item

def delete_item():
    if len(grocery_list) != 0:
        item_no = int(input("\nEnter the item number you want to delete: "))
        grocery_list.pop(item_no - 1)

    return get_grocery_list()

def start():
    user_input = input("\na for add item\nd for delete item\nq for quit: ")
    if user_input == "a":
        print(add_item())
    elif user_input == "d":
        print(f"\n{delete_item()}")
    elif user_input != "q":
        print("\nInvalid Input")

    if user_input != "q":
        start()


print(get_grocery_list())
start()