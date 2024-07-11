Certainly! Here's the Python script implementing the simple contact book application based on the problem statement:

```python
def display_menu():
    print("\nWelcome to the Contact Book Application!")
    print("Please choose an option:")
    print("1. Add a contact")
    print("2. View contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")

def add_contact(contacts):
    name = input("Enter contact name: ")
    number = input("Enter contact phone number: ")
    contacts[name] = number
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("Your contact list is empty.")
    else:
        print("Your contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")

def search_contact(contacts):
    name = input("Enter the name to search: ")
    if name in contacts:
        print(f"{name}'s phone number: {contacts[name]}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(contacts):
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print(f"{name} not found in contacts.")

def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
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
2. **`add_contact(contacts)`**: Prompts the user to enter a contact's name and phone number, then adds it to the `contacts` dictionary.
3. **`view_contacts(contacts)`**: Displays all contacts stored in the `contacts` dictionary.
4. **`search_contact(contacts)`**: Prompts the user to enter a name to search for in the `contacts` dictionary and displays the corresponding phone number if found.
5. **`delete_contact(contacts)`**: Prompts the user to enter a name to delete from the `contacts` dictionary and removes it if found.
6. **`main()`**: Contains the main loop that displays the menu, captures user input, and calls the respective functions based on the user's choice. It continues running until the user chooses to exit (`choice == '5'`).

This script provides a basic yet functional contact book application where users can add, view, search, and delete contacts using a dictionary to store the contacts. It's suitable for beginners and demonstrates fundamental concepts such as dictionaries, loops, conditionals, and user input handling in Python.
