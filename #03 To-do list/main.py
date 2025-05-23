tasks = []

def add_task():
    print("\nWhat task would you like to add?")
    task = input()
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    if len(tasks) == 0:
        print("\nYour to-do list is empty!")
        return
    
    print("\nYour tasks:")
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")
    
    print("\nWhich task number do you want to remove?")
    try:
        task_number = int(input())
        if task_number < 1 or task_number > len(tasks):
            print("That task number doesn't exist!")
        else:
            removed_task = tasks.pop(task_number - 1)
            print(f"You removed: {removed_task}")
    except:
        print("Please enter a number!")

def view_tasks():
    if len(tasks) == 0:
        print("\nYour to-do list is empty!")
        return
    
    print("\nYour tasks:")
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")

def main():
    while True:
        print("\n=== TO-DO LIST ===")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View all tasks")
        print("4. Exit")
        
        choice = input("\nWhat would you like to do? (1-4): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Please enter a number between 1 and 4!")

if __name__ == "__main__":
    main()
