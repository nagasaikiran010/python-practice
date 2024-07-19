def display_menu():
    print("\nWelcome to the Personal Budget Manager!")
    print("Please choose an option:")
    print("1. Add a budget item")
    print("2. View all budget items")
    print("3. Update a budget item")
    print("4. Delete a budget item")
    print("5. Calculate total expenses")
    print("6. Check if expenses exceed a budget limit")
    print("7. Exit")

def add_item(budget):
    name = input("Enter the item's name: ")
    try:
        amount = float(input("Enter the item's amount: "))
        budget.append({"name": name, "amount": amount})
        print("Item added successfully!")
    except ValueError:
        print("Invalid input! Amount should be a number.")

def view_items(budget):
    if not budget:
        print("No budget items to display.")
    else:
        print("Budget Items List:")
        for index, item in enumerate(budget, start=1):
            print(f"{index}. Name: {item['name']}, Amount: {item['amount']}")

def update_item(budget):
    if not budget:
        print("No budget items to update.")
        return

    try:
        index = int(input("Enter the index number of the item to update: "))
        if 1 <= index <= len(budget):
            new_amount = float(input("Enter the new amount: "))
            budget[index - 1]['amount'] = new_amount
            print("Budget item updated successfully!")
        else:
            print("Invalid index number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_item(budget):
    if not budget:
        print("No budget items to delete.")
        return

    try:
        index = int(input("Enter the index number of the item to delete: "))
        if 1 <= index <= len(budget):
            budget.pop(index - 1)
            print("Budget item deleted successfully!")
        else:
            print("Invalid index number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def calculate_total(budget):
    if not budget:
        print("No budget items to calculate total.")
    else:
        total = sum(item['amount'] for item in budget)
        print(f"The total expenses are: {total:.2f}")

def check_budget_limit(budget):
    if not budget:
        print("No budget items to check limit.")
        return

    try:
        limit = float(input("Enter your budget limit: "))
        total = sum(item['amount'] for item in budget)
        if total > limit:
            print(f"Expenses exceed the budget limit by {total - limit:.2f}")
        else:
            print("Expenses are within the budget limit.")
    except ValueError:
        print("Invalid input! Budget limit should be a number.")

def main():
    budget = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(budget)
        elif choice == '2':
            view_items(budget)
        elif choice == '3':
            update_item(budget)
        elif choice == '4':
            delete_item(budget)
        elif choice == '5':
            calculate_total(budget)
        elif choice == '6':
            check_budget_limit(budget)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()




Explanation:
display_menu(): Prints the menu options to the screen.
add_item(budget): Prompts the user to enter the item's name and amount, and adds the item to the budget list. Uses try and except to handle invalid inputs.
view_items(budget): Displays all budget items with their index numbers, names, and amounts. If the list is empty, it informs the user.
update_item(budget): Prompts the user to enter the index number of the item to update and the new amount. It updates the amount in the list and handles invalid input.
delete_item(budget): Prompts the user to enter the index number of the item to delete and removes the item from the list. Handles invalid input.
calculate_total(budget): Calculates and displays the total amount of all budget items if the list is not empty.
check_budget_limit(budget): Prompts the user to enter a budget limit, compares the total expenses with the limit, and displays a message indicating whether the expenses are within the limit or exceed it. Uses try and except to handle invalid inputs.
main(): Contains the main loop that displays the menu, captures user input, and calls the respective functions based on the user's choice. It continues running until the user chooses to exit.
