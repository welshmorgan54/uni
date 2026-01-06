import json

FILENAME = "inventory.json"


def loadInventory(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("No inventory file found. Starting with empty inventory.")
        return []
    except json.JSONDecodeError:
        print("Error reading inventory file.")
        return []


def saveInventory(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print("Inventory saved successfully.")


def showMenu():
    print("\n--- Inventory Management System ---")
    print("1. Add Item")
    print("2. View Stock")
    print("3. Update Item")
    print("4. Search Item")
    print("5. Save & Exit")


def addItem(data):
    try:
        productId = int(input("Enter product ID: "))
        for item in data:
            if item['id'] == productId:
                print("Error: ID already exists.")
                return

        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        newItem = {
            "id": productId,
            "name": name,
            "price": price,
            "quantity": quantity
        }

        data.append(newItem)
        print("Item added successfully.")

    except ValueError:
        print("Invalid input. Please enter correct values.")


def viewStock(data):
    if not data:
        print("Inventory is empty.")
        return

    print("\nID   Name            Price    Quantity")
    print("--------------------------------------")
    for item in data:
        print(f"{item['id']}   {item['name']}   £{item['price']}    {item['quantity']}")


def updateItem(data):
    try:
        productId = int(input("Enter product ID to update: "))

        for item in data:
            if item['id'] == productId:
                print("Leave blank to keep current value.")

                newName = input("New name: ")
                if newName != "":
                    item['name'] = newName

                newPrice = input("New price: ")
                if newPrice != "":
                    item['price'] = float(newPrice)

                newQuantity = input("New quantity: ")
                if newQuantity != "":
                    item['quantity'] = int(newQuantity)

                print("Item updated successfully.")
                return

        print("Item not found.")

    except ValueError:
        print("Invalid input.")


def searchItem(data):
    searchName = input("Enter name to search: ").lower()

    found = False
    for item in data:
        if searchName in item['name'].lower():
            print("\nItem found:")
            print(item)
            found = True

    if not found:
        print("No matching items found.")


def main():
    inventory = loadInventory(FILENAME)

    while True:
        showMenu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            addItem(inventory)
        elif choice == "2":
            viewStock(inventory)
        elif choice == "3":
            updateItem(inventory)
        elif choice == "4":
            searchItem(inventory)
        elif choice == "5":
            saveInventory(FILENAME, inventory)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
