# Todo App

A simple command-line todo application written in Python.

## Features

- Add new todo items
- List all todo items
- Mark todo items as completed
- Delete todo items
- Save todo items to a file for persistence
- Interactive and command-line modes

## Installation

No installation required. Just make sure you have Python 3.6+ installed.

## Usage

### Interactive Mode

Run the application without any arguments to enter interactive mode:

```bash
python todo.py
```

In interactive mode, you can use the following commands:

- `add <title>` - Add a new todo item
- `list` - List all todo items
- `complete <id>` - Mark a todo item as completed
- `delete <id>` - Delete a todo item
- `help` - Show help information
- `quit` or `exit` - Exit the application

### Command-line Mode

You can also use the application in command-line mode:

```bash
# Add a new todo item
python todo.py add "Buy groceries"
# or
python main.py add "Buy groceries"

# List all todo items
python todo.py list
# or
python main.py list

# Mark a todo item as completed
python todo.py complete 1
# or
python main.py complete 1

# Delete a todo item
python todo.py delete 2
# or
python main.py delete 2

# Show help information
python todo.py help
# or
python main.py help
```

## File Structure

- `todo.py` - The main application file with the CLI interface
- `main.py` - An alternative entry point for the application
- `todo_manager.py` - A class to manage todo items
- `todo_item.py` - A class representing a single todo item
- `test_todo.py` - Unit tests for the application
- `test_main.py` - Unit tests for the main module

## Running Tests

Run the unit tests with:

```bash
python -m unittest test_todo.py test_main.py
```