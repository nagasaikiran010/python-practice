Python Script:
python
Copy code
def display_menu():
    print("\nWelcome to the Grocery List Manager!")
    print("Please choose an option:")
    print("1. Add an item")
    print("2. View the grocery list")
    print("3. Remove an item")
    print("4. Update item quantity")
    print("5. Search for an item")
    print("6. Exit")

def add_item(grocery_list):
    name = input("Enter the item name: ")
    try:
        quantity = int(input("Enter the item quantity: "))
        grocery_list.append({"name": name, "quantity": quantity})
        print("Item added successfully!")
    except ValueError:
        print("Invalid input! Quantity should be a number.")

def view_grocery_list(grocery_list):
    if not grocery_list:
        print("Your grocery list is empty.")
    else:
        print("Your grocery list:")
        for index, item in enumerate(grocery_list, start=1):
            print(f"{index}. Name: {item['name']}, Quantity: {item['quantity']}")

def remove_item(grocery_list):
    if not grocery_list:
        print("Your grocery list is empty. Nothing to remove.")
        return
    
    try:
        index = int(input("Enter the index number of the item to remove: "))
        if 1 <= index <= len(grocery_list):
            removed_item = grocery_list.pop(index - 1)
            print(f"Item '{removed_item['name']}' removed successfully!")
        else:
            print("Invalid index number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def update_item_quantity(grocery_list):
    if not grocery_list:
        print("Your grocery list is empty. Nothing to update.")
        return

    try:
        index = int(input("Enter the index number of the item to update: "))
        if 1 <= index <= len(grocery_list):
            new_quantity = int(input("Enter the new quantity: "))
            grocery_list[index - 1]['quantity'] = new_quantity
            print("Item quantity updated successfully!")
        else:
            print("Invalid index number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def search_items(grocery_list):
    search_term = input("Enter a search term: ").lower()
    results = [item for item in grocery_list if search_term in item['name'].lower()]
    if not results:
        print("No items found matching your search term.")
    else:
        print("Search results:")
        for index, item in enumerate(results, start=1):
            print(f"{index}. Name: {item['name']}, Quantity: {item['quantity']}")

def main():
    grocery_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(grocery_list)
        elif choice == '2':
            view_grocery_list(grocery_list)
        elif choice == '3':
            remove_item(grocery_list)
        elif choice == '4':
            update_item_quantity(grocery_list)
        elif choice == '5':
            search_items(grocery_list)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
Explanation:
display_menu(): Prints the menu options to the screen.
add_item(grocery_list): Prompts the user to enter the item's name and quantity, and adds the item to the grocery_list. It uses try and except to handle invalid quantity inputs.
view_grocery_list(grocery_list): Displays all items in the grocery_list with their index numbers, names, and quantities. If the list is empty, it informs the user.
remove_item(grocery_list): Prompts the user to enter the index number of the item to remove and removes it from the list. It handles invalid input and informs the user if the index is out of range or if the list is empty.
update_item_quantity(grocery_list): Prompts the user to enter the index number of the item to update and the new quantity. It updates the quantity in the list and handles invalid input.
search_items(grocery_list): Prompts the user to enter a search term and displays the items that match the search term in their name using a list comprehension.
main(): Contains the main loop that displays the menu, captures user input, and calls the respective functions based on the user's choice. It continues running until the user chooses to exit.
This script introduces basic concepts such as lists, dictionaries, loops, conditionals, list comprehensions, and error handling, making it suitable for beginners and intermediate learners.
