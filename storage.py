import json
from config import CONFIG
import logging

# Add logging to track loading and saving tasks
def load_tasks():
    try:
        logging.debug(f"Loading tasks from {CONFIG['data_file']}")
        with open(CONFIG["data_file"], "r") as file:
            tasks = json.load(file)
        logging.info(f"Successfully loaded {len(tasks)} tasks.")
        return tasks
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.warning(f"Error loading tasks: {e}. Returning empty task list.")
        return []

def save_tasks(tasks):
    try:
        logging.debug(f"Saving {len(tasks)} tasks to {CONFIG['data_file']}")
        with open(CONFIG["data_file"], "w") as file:
            json.dump(tasks, file, indent=4)
        logging.info(f"Successfully saved {len(tasks)} tasks.")
    except Exception as e:
        logging.error(f"Error saving tasks: {e}")
