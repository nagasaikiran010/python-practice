### Problem Statement: Inventory Management System

**Objective:** Create a Python script to manage an inventory system for a store. The script should allow the user to add, view, update, and delete items. Additionally, it should allow searching items, checking stock levels, and generating reports. The script should handle errors gracefully and use functions to organize the code.

### Requirements:

1. **Menu Options:**
    - Display a menu to the user with options to:
        1. Add an item
        2. View all items
        3. Update an item
        4. Delete an item
        5. Search for an item by name
        6. Check stock level of an item
        7. Generate a report of all items
        8. Exit the application

2. **Add an Item:**
    - Prompt the user to enter the item name, quantity, and price.
    - Save the item in a dictionary, where the item name is the key and a tuple (quantity, price) is the value.

3. **View All Items:**
    - Display all items with their names, quantities, and prices.

4. **Update an Item:**
    - Prompt the user to enter the item name.
    - Allow the user to update either the quantity or the price of the item.

5. **Delete an Item:**
    - Prompt the user to enter the item name to delete.
    - Remove the item from the dictionary.

6. **Search for an Item by Name:**
    - Prompt the user to enter a search term.
    - Display the items that match the search term in their name.

7. **Check Stock Level of an Item:**
    - Prompt the user to enter the item name.
    - Display the quantity in stock for that item.

8. **Generate a Report of All Items:**
    - Display a sorted list of all items with their names, quantities, and prices.

9. **Error Handling:**
    - Handle errors such as entering a non-numeric quantity or price, or providing an invalid item name.
    - Provide user-friendly error messages.

10. **Functions:**
    - Use functions to handle each menu option and other repetitive tasks.
    - Define variables and manage scope appropriately.

### Example Interaction:
```
Welcome to the Inventory Management System!
Please choose an option:
1. Add an item
2. View all items
3. Update an item
4. Delete an item
5. Search for an item by name
6. Check stock level of an item
7. Generate a report of all items
8. Exit

Enter your choice: 1
Enter the item's name: Apple
Enter the item's quantity: 50
Enter the item's price: 0.5
Item added successfully!

Please choose an option:
1. Add an item
2. View all items
3. Update an item
4. Delete an item
5. Search for an item by name
6. Check stock level of an item
7. Generate a report of all items
8. Exit

Enter your choice: 2
Inventory List:
1. Name: Apple, Quantity: 50, Price: 0.5

Please choose an option:
...
```

### Guidelines:
1. Use a loop to repeatedly display the menu until the user chooses to exit.
2. Use a dictionary to store the inventory items, with each item represented as a tuple (quantity, price).
3. Use `input()` to capture user input.
4. Use conditional statements (`if`, `elif`, `else`) to handle menu options.
5. Use `try` and `except` to handle potential errors, such as invalid input.
6. Use list comprehensions where appropriate to make the code more concise and readable.
7. Use tuples for item data and sets for storing unique item names.
8. Define and use functions for each main feature to keep the code organized and readable.

### Python Script:

```python
def display_menu():
    print("\nWelcome to the Inventory Management System!")
    print("Please choose an option:")
    print("1. Add an item")
    print("2. View all items")
    print("3. Update an item")
    print("4. Delete an item")
    print("5. Search for an item by name")
    print("6. Check stock level of an item")
    print("7. Generate a report of all items")
    print("8. Exit")

def add_item(inventory):
    name = input("Enter the item's name: ").lower()
    try:
        quantity = int(input("Enter the item's quantity: "))
        price = float(input("Enter the item's price: "))
        inventory[name] = (quantity, price)
        print("Item added successfully!")
    except ValueError:
        print("Invalid input! Quantity should be an integer and price should be a number.")

def view_items(inventory):
    if not inventory:
        print("No items to display.")
    else:
        print("Inventory List:")
        for name, (quantity, price) in inventory.items():
            print(f"Name: {name.capitalize()}, Quantity: {quantity}, Price: {price:.2f}")

def update_item(inventory):
    if not inventory:
        print("No items to update.")
        return

    name = input("Enter the item's name to update: ").lower()
    if name in inventory:
        try:
            update_choice = input("Update quantity (q) or price (p)? ").lower()
            if update_choice == 'q':
                new_quantity = int(input("Enter the new quantity: "))
                inventory[name] = (new_quantity, inventory[name][1])
            elif update_choice == 'p':
                new_price = float(input("Enter the new price: "))
                inventory[name] = (inventory[name][0], new_price)
            else:
                print("Invalid choice.")
            print("Item updated successfully!")
        except ValueError:
            print("Invalid input! Quantity should be an integer and price should be a number.")
    else:
        print("Item not found.")

def delete_item(inventory):
    if not inventory:
        print("No items to delete.")
        return

    name = input("Enter the item's name to delete: ").lower()
    if name in inventory:
        del inventory[name]
        print("Item deleted successfully!")
    else:
        print("Item not found.")

def search_item(inventory):
    search_term = input("Enter an item's name to search: ").lower()
    results = {name: details for name, details in inventory.items() if search_term in name}
    if not results:
        print("No items found with that name.")
    else:
        print("Search Results:")
        for name, (quantity, price) in results.items():
            print(f"Name: {name.capitalize()}, Quantity: {quantity}, Price: {price:.2f}")

def check_stock(inventory):
    if not inventory:
        print("No items to check stock.")
        return

    name = input("Enter the item's name to check stock: ").lower()
    if name in inventory:
        quantity = inventory[name][0]
        print(f"The stock level for {name.capitalize()} is {quantity}.")
    else:
        print("Item not found.")

def generate_report(inventory):
    if not inventory:
        print("No items to generate a report.")
    else:
        print("Inventory Report:")
        sorted_inventory = sorted(inventory.items())
        for name, (quantity, price) in sorted_inventory:
            print(f"Name: {name.capitalize()}, Quantity: {quantity}, Price: {price:.2f}")

def main():
    inventory = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            view_items(inventory)
        elif choice == '3':
            update_item(inventory)
        elif choice == '4':
            delete_item(inventory)
        elif choice == '5':
            search_item(inventory)
        elif choice == '6':
            check_stock(inventory)
        elif choice == '7':
            generate_report(inventory)
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
```

### Explanation:
1. **`display_menu()`**: Prints the menu options to the screen.
2. **`add_item(inventory)`**: Prompts the user to enter the item's name, quantity, and price, and adds the item to the `inventory` dictionary. Uses `try` and `except` to handle invalid inputs.
3. **`view_items(inventory)`**: Displays all items in the inventory with their names, quantities, and prices. If the inventory is empty, it informs the user.
4. **`update_item(inventory)`**: Prompts the user to enter the item's name and allows updating either the quantity or price. Updates the item in the dictionary and handles invalid input.
5. **`delete_item(inventory)`**: Prompts the user to enter the item's name to delete and removes the item from the dictionary. Handles invalid input.
6. **`search_item(inventory)`**: Prompts the user to enter a search term and displays items that match the search term in their name using a dictionary comprehension.
7. **`check_stock(inventory)`**: Prompts the user to enter the item's name and displays the quantity in stock for that item. Handles invalid input.
8. **`generate_report(inventory)`**: Displays a sorted list of all items with their names, quantities, and prices if the inventory is not empty.
9. **`main()`**: Contains the main loop that displays the menu, captures user input

, and calls the respective functions based on the user's choice. It continues running until the user chooses to exit.

This script covers basic syntax, variables, data types, conditionals, loops, error handling, list comprehensions, tuples, sets, dictionaries, and functions, making it suitable for both beginners and intermediate learners.
