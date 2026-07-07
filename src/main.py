import json
import sys
import os
from datetime import datetime

def load_tasks():
    if not os.path.exists("tasks.json"):
        with open("tasks.json", "w") as f:
            json.dump([], f)
    with open("tasks.json", "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)

def find_task(task_id, tasks):
    try:
        target_id = int(task_id)
    except ValueError:
        print("Task id must be a number.")
        return None

    found = False
    for task in tasks:
        if task["id"] == target_id:
            found = True
            break
    
    if not found:
        print("ID not found.")
        return None
    
    return task

def add():
    tasks = load_tasks()
    if tasks:
        max_id = max(task["id"] for task in tasks) + 1
    else:
        max_id = 1
    currTime = datetime.now().isoformat()

    new_task = {
        "id":max_id,
        "description":sys.argv[2],
        "status": "todo",
        "createdAt": currTime,
        "updatedAt": currTime
        }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Successfully created new task with id {max_id}")

def list_tasks():
    tasks = load_tasks()

    if len(sys.argv) > 2:
            status_filter = sys.argv[2]
            tasks = [task for task in tasks if task["status"] == status_filter]
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f'{task["id"]}: {task["description"]} [{task["status"]}]')

def update():
    task_id = sys.argv[2]
    new_desc = sys.argv[3]
    tasks = load_tasks()

    task = find_task(task_id, tasks)
    if task is None:
        return
    
    task["description"] = new_desc
    task["updatedAt"] = datetime.now().isoformat()
    save_tasks(tasks)
    print(f"Updated task with id {task_id} to: {new_desc}")

def delete():
    task_id = sys.argv[2]
    tasks = load_tasks()

    if task_id == "all":
        tasks = []
        save_tasks(tasks)
        print("Deleted all tasks.")
        return

    task = find_task(task_id, tasks)
    if task is None:
        return
    
    tasks = [task for task in tasks if task["id"] != int(task_id)]
    save_tasks(tasks)
    print(f"Deleted task with id {task_id}")

def mark_in_progress():
    task_id = sys.argv[2]
    tasks = load_tasks()

    task = find_task(task_id, tasks)
    if task is None:
        return

    task["status"] = "in-progress"
    task["updatedAt"] = datetime.now().isoformat()
    save_tasks(tasks)
    print(f"Marked task with id {task_id} as in-progress")

def mark_done():
    task_id = sys.argv[2]
    tasks = load_tasks()

    task = find_task(task_id, tasks)
    if task is None:
        return
    
    task["status"] = "done"
    task["updatedAt"] = datetime.now().isoformat()
    save_tasks(tasks)
    print(f"Marked task with id {task_id} as done")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a command.")
    else:
        command = sys.argv[1]

        commands = {
            "add": add,
            "list": list_tasks,
            "update": update,
            "delete": delete,
            "mark-in-progress": mark_in_progress,
            "mark-done": mark_done
        }

        if command in commands:
            commands[command]()
        else:
            print(f"Unknown command: {command}")