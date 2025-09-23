import os

script_dir = os.path.dirname(os.path.realpath(__file__))
tasks_file = os.path.join(script_dir, 'tasks.txt')

def load_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    return []

def save_tasks(tasks):
    with open(tasks_file, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)

def view_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks found.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_idx = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_idx < len(tasks):
            removed = tasks.pop(task_idx)
            print(f"Task '{removed}' removed!")
            save_tasks(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

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
            print("Invalid choice, please try again.")
