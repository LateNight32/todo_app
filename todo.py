from storage import load_tasks, save_tasks

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    return tasks

def remove_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        return True
    return False