# Task Tracker CLI

A simple command-line tool to track tasks. Functionality includes add, update, delete, and marking as todo, in-progress, or done. Tasks are stored in a local JSON file.

## Setup

1. Clone this repository
2. Navigate to the project folder: `cd todocli/src`
3. Run commands with `python main.py <command> [arguments]`

## Usage

### Add a task
```bash
python main.py add "Buy groceries"
```

### Update a task
```bash
python main.py update 1 "Buy groceries and cook dinner"
```

### Delete a task
```bash
python main.py delete 1
python main.py delete all
```

### Mark a task's status
```bash
python main.py mark-in-progress 1
python main.py mark-done 1
```

### List tasks
```bash
python main.py list
python main.py list done
python main.py list todo
python main.py list in-progress
```

## Task Properties

Each task has:
- **id** — unique identifier (number)
- **description** — short description of the task (string)
- **status** — one of `todo`, `in-progress`, `done`
- **createdAt** — ISO 8601 timestamp of when the task was created
- **updatedAt** — ISO 8601 timestamp of when the task was last updated