# we are  making the to do list for our tasks
FILE_NAME = "tasks.txt"


# File se tasks load karna
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = [task.strip() for task in file.readlines()]
        return tasks

    except FileNotFoundError:
        return []


# Tasks ko file me save karna
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Task add karna
def add_task(tasks):
    task = input("Enter your task: ").strip()

    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added successfully!")
    else:
        print("❌ Task cannot be empty.")


# Tasks display karna
def view_tasks(tasks):
    if len(tasks) == 0:
        print("\n📭 No tasks available.")
        return

    print("\n----- YOUR TASKS -----")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


# Task delete karna
def delete_task(tasks):
    if len(tasks) == 0:
        print("\n📭 No tasks to delete.")
        return

    view_tasks(tasks)

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted_task = tasks.pop(number - 1)
            save_tasks(tasks)

            print(f"🗑️ Deleted: {deleted_task}")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a number.")


# ---------------- MAIN PROGRAM ----------------

tasks = load_tasks()

while True:

    print("\n======================")
    print("       TO-DO LIST")
    print("======================")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please try again.")