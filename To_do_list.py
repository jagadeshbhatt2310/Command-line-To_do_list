import json
tasks = []
def add_task():
    task_text = input("Enter task description: ")
    priority = input("Enter priority (high/medium/low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    task = {
        "task_text": task_text,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Removed task: {removed_task['task_text']}")
    else:
        print("Invalid task number!")

def complete_task():
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTask List:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. Task: {task['task_text']}")
            print(f"   Priority: {task['priority']}")
            print(f"   Due Date: {task['due_date']}")
            print(f"   Status: {status}\n")

while True:
    print("\nCommand Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. List Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        list_tasks()
    elif choice == "5":
        # Save tasks to a JSON file for persistence
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")
