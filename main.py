from todo import add_task, list_tasks, remove_task

def main():
    while True:
        print("\nTo-Do List:")
        tasks = list_tasks()
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
        
        print("\nOptions: 1) Add Task 2) Remove Task 3) Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            index = int(input("Enter task number to remove: ")) - 1
            if not remove_task(index):
                print("Invalid task number.")
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()