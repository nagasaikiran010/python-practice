Sure! Here is a Python script for a simple expense tracker application based on the problem statement:

```python
def display_menu():
    print("\nWelcome to the Expense Tracker!")
    print("Please choose an option:")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. Delete an expense")
    print("4. Calculate total expenses")
    print("5. Exit")

def add_expense(expenses):
    description = input("Enter the description of the expense: ")
    try:
        amount = float(input("Enter the amount of the expense: "))
        expenses.append({"description": description, "amount": amount})
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_expenses(expenses):
    if not expenses:
        print("Your expense list is empty.")
    else:
        print("Your expenses:")
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. {expense['description']}: ${expense['amount']:.2f}")

def delete_expense(expenses):
    if not expenses:
        print("Your expense list is empty. Nothing to delete.")
        return
    
    try:
        index = int(input("Enter the index number of the expense to delete: "))
        if 1 <= index <= len(expenses):
            removed_expense = expenses.pop(index - 1)
            print(f"Expense '{removed_expense['description']}' deleted successfully!")
        else:
            print("Invalid index number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def calculate_total_expenses(expenses):
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total expenses: ${total:.2f}")

def main():
    expenses = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            delete_expense(expenses)
        elif choice == '4':
            calculate_total_expenses(expenses)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
```

### Explanation:

1. **`display_menu()`**: Prints the menu options to the screen.
2. **`add_expense(expenses)`**: Prompts the user to enter an expense description and amount, and adds the expense to the list. It handles invalid input for the amount.
3. **`view_expenses(expenses)`**: Displays all expenses with their index numbers, descriptions, and amounts. If the list is empty, it informs the user.
4. **`delete_expense(expenses)`**: Prompts the user to enter the index number of the expense to delete and removes it from the list. It handles invalid input and informs the user if the index is out of range or if the list is empty.
5. **`calculate_total_expenses(expenses)`**: Calculates and displays the total amount of all expenses in the list.
6. **`main()`**: Contains the main loop that displays the menu, captures user input, and calls the respective functions based on the user's choice. It continues running until the user chooses to exit.

This script provides a basic yet functional expense tracker application that allows users to add, view, delete, and calculate total expenses. It's suitable for beginners and demonstrates fundamental concepts such as lists, dictionaries, loops, conditionals, and user input handling in Python.
