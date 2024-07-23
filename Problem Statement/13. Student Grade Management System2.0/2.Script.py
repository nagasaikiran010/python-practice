def display_menu():
    print("\nWelcome to the Student Grade Management System!")
    print("Please choose an option:")
    print("1. Add a student record")
    print("2. View all student records")
    print("3. Update a student record")
    print("4. Delete a student record")
    print("5. Calculate average grade")
    print("6. Find the highest and lowest grades")
    print("7. Exit")

def add_record(grades):
    name = input("Enter the student's name: ").strip().title()
    try:
        grade = float(input("Enter the student's grade: "))
        grades[name] = grade
        print("Record added successfully!")
    except ValueError:
        print("Invalid input! Grade should be a number.")

def view_records(grades):
    if not grades:
        print("No records to display.")
    else:
        print("Student Records:")
        for name, grade in grades.items():
            print(f"Name: {name}, Grade: {grade}")

def update_record(grades):
    if not grades:
        print("No records to update.")
        return

    name = input("Enter the student's name to update: ").strip().title()
    if name in grades:
        try:
            new_grade = float(input("Enter the new grade: "))
            grades[name] = new_grade
            print("Record updated successfully!")
        except ValueError:
            print("Invalid input! Grade should be a number.")
    else:
        print("Student not found.")

def delete_record(grades):
    if not grades:
        print("No records to delete.")
        return

    name = input("Enter the student's name to delete: ").strip().title()
    if name in grades:
        del grades[name]
        print("Record deleted successfully!")
    else:
        print("Student not found.")

def calculate_average(grades):
    if not grades:
        print("No records to calculate average.")
    else:
        average = sum(grades.values()) / len(grades)
        print(f"The average grade is: {average:.2f}")

def find_high_low(grades):
    if not grades:
        print("No records to find high and low grades.")
    else:
        highest = max(grades.values())
        lowest = min(grades.values())
        highest_students = [name for name, grade in grades.items() if grade == highest]
        lowest_students = [name for name, grade in grades.items() if grade == lowest]

        print(f"The highest grade is {highest} by: {', '.join(highest_students)}")
        print(f"The lowest grade is {lowest} by: {', '.join(lowest_students)}")

def main():
    grades = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_record(grades)
        elif choice == '2':
            view_records(grades)
        elif choice == '3':
            update_record(grades)
        elif choice == '4':
            delete_record(grades)
        elif choice == '5':
            calculate_average(grades)
        elif choice == '6':
            find_high_low(grades)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
Explanation:
display_menu(): Prints the menu options to the screen.
add_record(grades): Prompts the user to enter the student's name and grade, and adds the record to the grades dictionary. Uses try and except to handle invalid inputs.
view_records(grades): Displays all student records with their names and grades. If the dictionary is empty, it informs the user.
update_record(grades): Prompts the user to enter the student's name and updates the grade. Handles invalid input.
delete_record(grades): Prompts the user to enter the student's name to delete and removes the record from the dictionary. Handles invalid input.
calculate_average(grades): Calculates and displays the average grade of all students if the dictionary is not empty.
find_high_low(grades): Finds and displays the student(s) with the highest and lowest grades if the dictionary is not empty.
main(): Contains the main loop that displays the menu, captures user input, and calls the respective functions based on the user's choice. It continues running until the user chooses to exit.
