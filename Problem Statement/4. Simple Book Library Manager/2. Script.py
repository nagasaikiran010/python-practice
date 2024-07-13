Sure! Here is a Python script for a simple book library manager application based on the problem statement:

```python
def display_menu():
    print("\nWelcome to the Book Library Manager!")
    print("Please choose an option:")
    print("1. Add a book")
    print("2. View books")
    print("3. Search for a book")
    print("4. Delete a book")
    print("5. Exit")

def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of publication: ")
    library.append({"title": title, "author": author, "year": year})
    print("Book added successfully!")

def view_books(library):
    if not library:
        print("Your book list is empty.")
    else:
        print("Your books:")
        for index, book in enumerate(library, start=1):
            print(f"{index}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

def search_books(library):
    search_term = input("Enter a search term: ").lower()
    results = [book for book in library if search_term in book['title'].lower() or search_term in book['author'].lower()]
    if not results:
        print("No books found matching your search term.")
    else:
        print("Search results:")
        for index, book in enumerate(results, start=1):
            print(f"{index}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

def delete_book(library):
    if not library:
        print("Your book list is empty. Nothing to delete.")
        return
    
    try:
        index = int(input("Enter the index number of the book to delete: "))
        if 1 <= index <= len(library):
            removed_book = library.pop(index - 1)
            print(f"Book '{removed_book['title']}' deleted successfully!")
        else:
            print("Invalid index number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    library = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            view_books(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            delete_book(library)
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
2. **`add_book(library)`**: Prompts the user to enter the title, author, and year of publication for a book, and adds it to the `library` list.
3. **`view_books(library)`**: Displays all books in the library with their index numbers, titles, authors, and years of publication. If the library is empty, it informs the user.
4. **`search_books(library)`**: Prompts the user to enter a search term, and displays the books that match the search term in either the title or the author's name.
5. **`delete_book(library)`**: Prompts the user to enter the index number of the book to delete and removes it from the list. It handles invalid input and informs the user if the index is out of range or if the library is empty.
6. **`main()`**: Contains the main loop that displays the menu, captures user input, and calls the respective functions based on the user's choice. It continues running until the user chooses to exit.

This script provides a basic yet functional book library manager application that allows users to add, view, search, and delete books. It's suitable for beginners and demonstrates fundamental concepts such as lists, dictionaries, loops, conditionals, and user input handling in Python.
