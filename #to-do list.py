#to-do list 
import json
def load_task():
    try:
        with open("task json","r") as file:
            task=json.load(file)
    except(json.JSONDECODEERROR,FileNotFoundError):
        task=[]
    return task
def save_task():
    with open("task.json","w") as file:
        json.dump(tasks,file)
def display_task(task):
    if not tasks:
        print("No task found")
    else:
        print("your to-do list")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks, new_task):
    tasks.append(new_task)
    print(f"Task added: {new_task}")

def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Task deleted: {deleted_task}")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            display_tasks(tasks)
            task_index = int(input("Enter the task index to delete: "))
            delete_task(tasks, task_index)
        elif choice == "4":
            save_tasks(tasks)
            print("Exiting the To-Do List Application. Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()