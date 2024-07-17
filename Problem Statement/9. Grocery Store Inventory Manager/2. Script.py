def display_menu():
    print("\nWelcome to the Grocery Store Inventory Manager!")
    print("Please choose an option:")
    print("1. Add an item to the inventory")
    print("2. View all items in the inventory")
    print("3. Update an item quantity")
    print("4. Calculate the total inventory value")
    print("5. Find the item with the highest and lowest stock")
    print("6. Search for an item by name")
    print("7. Exit")

def add_item(inventory):
    name = input("Enter the item name: ")
    try:
        quantity = int(input("Enter the item quantity: "))
        price = float(input("Enter the item price: "))
        inventory.append({"name": name, "quantity": quantity, "price": price})
        print("Item added successfully!")
    except ValueError:
        print("Invalid input! Quantity should be an integer and price should be a number.")

def view_items(inventory):
    if not inventory:
        print("No items to display.")
    else:
        print("Item List:")
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")

def update_item(inventory):
    if not inventory:
        print("No items to update.")
        return

    try:
        index = int(input("Enter the index number of the item to update: "))
        if 1 <= index <= len(inventory):
            new_quantity = int(input("Enter the new quantity: "))
            inventory[index - 1]['quantity'] = new_quantity
            print("Item quantity updated successfully!")
        else:
            print("Invalid index number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def calculate_total_value(inventory):
    if not inventory:
        print("No items to calculate total value.")
    else:
        total_value = sum(item['quantity'] * item['price'] for item in inventory)
        print(f"The total inventory value is: ${total_value:.2f}")

def find_highest_lowest(inventory):
    if not inventory:
        print("No items to find highest and lowest.")
    else:
        highest = max(inventory, key=lambda x: x['quantity'])
        lowest = min(inventory, key=lambda x: x['quantity'])
        print(f"Highest Stock Item: Name: {highest['name']}, Quantity: {highest['quantity']}")
        print(f"Lowest Stock Item: Name: {lowest['name']}, Quantity: {lowest['quantity']}")

def search_items(inventory):
    search_term = input("Enter an item name to search: ").lower()
    results = [item for item in inventory if search_term in item['name'].lower()]
    if not results:
        print("No items found with that name.")
    else:
        print("Search Results:")
        for item in results:
            print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")

def main():
    inventory = []
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
            calculate_total_value(inventory)
        elif choice == '5':
            find_highest_lowest(inventory)
        elif choice == '6':
            search_items(inventory)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
Explanation:
display_menu(): Prints the menu options to the screen.
add_item(inventory): Prompts the user to enter the item name, quantity, and price, and adds the item to the inventory list. Uses try and except to handle invalid inputs.
view_items(inventory): Displays all items with their index numbers, names, quantities, and prices. If the list is empty, it informs the user.
update_item(inventory): Prompts the user to enter the index number of the item to update and the new quantity. It updates the quantity in the list and handles invalid input.
calculate_total_value(inventory): Calculates and displays the total inventory value if the list is not empty.
find_highest_lowest(inventory): Finds and displays the item(s) with the highest and lowest quantities if the list is not empty.
search_items(inventory): Prompts the user to enter an item name and displays the items that match the search term using a list comprehension.
main(): Contains the main loop that displays the menu, captures user input, and calls the respective functions based on the user's choice. It continues running until the user chooses to exit.
