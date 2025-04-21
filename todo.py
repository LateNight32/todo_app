from storage import load_tasks, save_tasks
import logging

def add_task(task):
    logging.debug(f"Attempting to add task: {task}")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    logging.info(f"Task added: {task}")

def list_tasks():
    logging.debug("Listing all tasks")
    tasks = load_tasks()
    logging.info(f"Total number of tasks: {len(tasks)}")
    return tasks

def remove_task(index):
    logging.debug(f"Attempting to remove task at index: {index}")
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        logging.info(f"Task removed: {removed_task}")
        return True
    logging.warning(f"Invalid task index: {index}")
    return False
