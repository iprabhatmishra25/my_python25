from datetime import datetime
import json
import os

FILENAME = "todos.json"


# ===================================================================
# 1. Load Todos
# ===================================================================
def load_todos():
    """Loads and returns todos from JSON file. Returns empty list if file doesn't exist."""
    if not os.path.exists(FILENAME):
        return []

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


# ===================================================================
# Helper: Save Todos
# ===================================================================
def save_todos(todos):
    """Saves the current todos list back to the JSON file."""
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(todos, file, indent=4)


# ===================================================================
# 2. Add Todo
# ===================================================================
def add_todo(text):
    """Appends a new task item with text, done status, and timestamp, then saves."""
    todos = load_todos()

    # Generate current ISO timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_item = {"text": text, "done": False, "added": timestamp}

    todos.append(new_item)
    save_todos(todos)
    print(f"Added: '{text}'")


# ===================================================================
# 3. Mark Done
# ===================================================================
def mark_done(index):
    """Marks the todo item at the given 0-based index as done: True and saves."""
    todos = load_todos()

    if 0 <= index < len(todos):
        todos[index]["done"] = True
        save_todos(todos)
        print(f"✓ Marked done: Task #{index + 1} ('{todos[index]['text']}')")
    else:
        print(f" Invalid index: {index}")


# ===================================================================
# 4. Print Todos
# ===================================================================
def print_todos():
    """Displays the current list of todos in a clean format."""
    todos = load_todos()

    print("\n" + "=" * 50)
    print("                 CURRENT TO-DO LIST               ")
    print("=" * 50)

    if not todos:
        print("No tasks found.")
    else:
        for i, item in enumerate(todos):
            status = "✔ [DONE]" if item["done"] else "✘ [PENDING]"
            print(f"{i + 1}. {status} {item['text']}")
            print(f"   Added on: {item['added']}")
    print("=" * 50 + "\n")


# ===================================================================
# Demo Execution
# ===================================================================
if __name__ == "__main__":
    # Clean up any existing file from previous runs for a fresh demo
    if os.path.exists(FILENAME):
        os.remove(FILENAME)

    print("🚀 Running To-Do List Manager Demo...\n")

    # Add 3 items
    add_todo("Set up server infrastructure")
    add_todo("Complete code review for PR #42")
    add_todo("Update technical documentation")

    # Mark the second item (index 1) as done
    print()
    mark_done(1)

    # Print the final to-do list
    print_todos()