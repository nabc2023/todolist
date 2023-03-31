tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added.")

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task deleted.")
    else:
        print("Task not found.")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in tasks:
            print("-", task)

while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. Delete task")
    print("3. View tasks")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        task = input("Enter task: ")
        add_task(task)
    elif choice == 2:
        task = input("Enter task to delete: ")
        delete_task(task)
    elif choice == 3:
        view_tasks()
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
