def display_menu():
    print("\nWelcome to the Contact List Manager!")
    print("Please choose an option:")
    print("1. Add a contact")
    print("2. View contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")

def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("Your contact list is empty.")
    else:
        print("Your contacts:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contacts(contacts):
    search_term = input("Enter a search term: ").lower()
    results = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone'] or search_term in contact['email'].lower()]
    if not results:
        print("No contacts found matching your search term.")
    else:
        print("Search results:")
        for index, contact in enumerate(results, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def delete_contact(contacts):
    if not contacts:
        print("Your contact list is empty. Nothing to delete.")
        return
    
    try:
        index = int(input("Enter the index number of the contact to delete: "))
        if 1 <= index <= len(contacts):
            removed_contact = contacts.pop(index - 1)
            print(f"Contact '{removed_contact['name']}' deleted successfully!")
        else:
            print("Invalid index number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    contacts = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()



Explanation:
display_menu(): Prints the menu options to the screen.
add_contact(contacts): Prompts the user to enter the contact's name, phone number, and email address, and adds the contact to the contacts list.
view_contacts(contacts): Displays all contacts in the contacts list with their index numbers, names, phone numbers, and email addresses. If the list is empty, it informs the user.
search_contacts(contacts): Prompts the user to enter a search term and displays the contacts that match the search term in either the name, phone number, or email address.
delete_contact(contacts): Prompts the user to enter the index number of the contact to delete and removes it from the list. It handles invalid input and informs the user if the index is out of range or if the list is empty.
main(): Contains the main loop that displays the menu, captures user input, and calls the respective functions based on the user's choice. It continues running until the user chooses to exit.
This script provides a basic yet functional contact list manager application that allows users to add, view, search, and delete contacts. It's suitable for beginners and demonstrates fundamental concepts such as lists, dictionaries, loops, conditionals, and user input handling in Python.
