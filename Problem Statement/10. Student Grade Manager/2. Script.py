def display_menu():
    print("\nWelcome to the Student Grades Manager!")
    print("Please choose an option:")
    print("1. Add a student and their grade")
    print("2. View all student grades")
    print("3. Update a student grade")
    print("4. Calculate the class average grade")
    print("5. Find the highest and lowest grades")
    print("6. Search for a student by name")
    print("7. Exit")

def add_student(grades):
    name = input("Enter the student's name: ")
    try:
        grade = float(input("Enter the student's grade: "))
        grades.append({"name": name, "grade": grade})
        print("Student added successfully!")
    except ValueError:
        print("Invalid input! Grade should be a number.")

def view_grades(grades):
    if not grades:
        print("No grades to display.")
    else:
        print("Student Grades List:")
        for index, student in enumerate(grades, start=1):
            print(f"{index}. Name: {student['name']}, Grade: {student['grade']}")

def update_grade(grades):
    if not grades:
        print("No grades to update.")
        return

    try:
        index = int(input("Enter the index number of the student to update: "))
        if 1 <= index <= len(grades):
            new_grade = float(input("Enter the new grade: "))
            grades[index - 1]['grade'] = new_grade
            print("Student grade updated successfully!")
        else:
            print("Invalid index number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def calculate_average(grades):
    if not grades:
        print("No grades to calculate average.")
    else:
        average = sum(student['grade'] for student in grades) / len(grades)
        print(f"The class average grade is: {average:.2f}")

def find_highest_lowest(grades):
    if not grades:
        print("No grades to find highest and lowest.")
    else:
        highest = max(grades, key=lambda x: x['grade'])
        lowest = min(grades, key=lambda x: x['grade'])
        print(f"Highest Grade: Name: {highest['name']}, Grade: {highest['grade']}")
        print(f"Lowest Grade: Name: {lowest['name']}, Grade: {lowest['grade']}")

def search_students(grades):
    search_term = input("Enter a student's name to search: ").lower()
    results = [student for student in grades if search_term in student['name'].lower()]
    if not results:
        print("No students found with that name.")
    else:
        print("Search Results:")
        for student in results:
            print(f"Name: {student['name']}, Grade: {student['grade']}")

def main():
    grades = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(grades)
        elif choice == '2':
            view_grades(grades)
        elif choice == '3':
            update_grade(grades)
        elif choice == '4':
            calculate_average(grades)
        elif choice == '5':
            find_highest_lowest(grades)
        elif choice == '6':
            search_students(grades)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()



Explanation:
display_menu(): Prints the menu options to the screen.
add_student(grades): Prompts the user to enter the student's name and grade, and adds the student to the grades list. Uses try and except to handle invalid inputs.
view_grades(grades): Displays all students with their index numbers, names, and grades. If the list is empty, it informs the user.
update_grade(grades): Prompts the user to enter the index number of the student to update and the new grade. It updates the grade in the list and handles invalid input.
calculate_average(grades): Calculates and displays the class average grade if the list is not empty.
find_highest_lowest(grades): Finds and displays the student(s) with the highest and lowest grades if the list is not empty.
search_students(grades): Prompts the user to enter a student's name and displays the students that match the search term using a list comprehension.
main(): Contains the main loop that displays the menu, captures user input, and calls the respective functions based on the user's choice. It continues running until the user chooses to exit.
This script covers basic sy
