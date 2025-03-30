import json
from config import CONFIG

def load_tasks():
    try:
        with open(CONFIG["data_file"], "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(CONFIG["data_file"], "w") as file:
        json.dump(tasks, file, indent=4)