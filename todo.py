"""A tiny command-line to-do list. Tasks are saved in tasks.json."""
import json
import sys
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks(path=DATA_FILE):
    if path.exists():
        return json.loads(path.read_text())
    return []


def save_tasks(tasks, path=DATA_FILE):
    path.write_text(json.dumps(tasks, indent=2))


def add_task(tasks, text):
    tasks.append({"text": text, "done": False})
    return tasks


def complete_task(tasks, index):
    tasks[index]["done"] = True
    return tasks


def format_tasks(tasks):
    if not tasks:
        return "No tasks yet."
    lines = []
    for i, task in enumerate(tasks):
        mark = "x" if task["done"] else " "
        lines.append(f"{i}. [{mark}] {task['text']}")
    return "\n".join(lines)


def main(argv):
    if len(argv) < 2:
        print("Usage: python todo.py add <text> | done <number> | list")
        return
    command = argv[1]
    tasks = load_tasks()
    if command == "add":
        add_task(tasks, " ".join(argv[2:]))
        save_tasks(tasks)
    elif command == "done":
        complete_task(tasks, int(argv[2]))
        save_tasks(tasks)
    print(format_tasks(tasks))


if __name__ == "__main__":
    main(sys.argv)
