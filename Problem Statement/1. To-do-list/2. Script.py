def display_menu():
    print("\nWelcome to the To-Do List Application!")
    print("Please choose an option:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task(tasks):
    if not tasks:
        print("Your to-do list is empty. Nothing to delete.")
        return
    
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' deleted successfully!")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
