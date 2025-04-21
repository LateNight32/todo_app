import logging
from todo import add_task, list_tasks, remove_task

# Configure logginggg
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

def main():
    while True:
        logging.debug("Displaying task list")
        print("\nTo-Do List:")
        tasks = list_tasks()
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
        
        print("\nOptions: 1) Add Task 2) Remove Task 3) Exit")
        choice = input("Choose an option: ")
        logging.debug(f"User selected option: {choice}")
        
        if choice == "1":
            task = input("Enter task: ")
            logging.debug(f"User entered task: {task}")
            add_task(task)
            logging.info("Task added successfully.")
        elif choice == "2":
            try:
                index = int(input("Enter task number to remove: ")) - 1
                logging.debug(f"User selected task index: {index}")
                if not remove_task(index):
                    logging.warning("Invalid task number.")
                    print("Invalid task number.")
                else:
                    logging.info("Task removed successfully.")
            except ValueError as e:
                logging.error(f"Invalid input for task index: {e}")
                print("Invalid input.")
        elif choice == "3":
            logging.info("User exited the application.")
            break
        else:
            logging.warning("User entered invalid choice.")
            print("Invalid choice, try again.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.fatal(f"Unhandled exception occurred: {e}")
        raise
