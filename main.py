#!/usr/bin/env python3
"""
Main entry point for the Todo App.

This module provides a command-line interface for managing todo items.
It delegates the actual functionality to the todo.py module.
"""

import sys
from todo_manager import TodoManager

def add(title):
    """
    Add a new todo item.
    
    Args:
        title (str): The title or description of the todo item.
        
    Returns:
        TodoItem: The newly created TodoItem.
    """
    manager = TodoManager()
    todo = manager.add_todo(title)
    print(f"Added todo: {todo}")
    return todo

def list_todos():
    """
    List all todo items.
    """
    manager = TodoManager()
    todos = manager.list_todos()
    if not todos:
        print("No todos found.")
    else:
        print("Todo List:")
        for todo in todos:
            print(f"  {todo}")

def complete(todo_id):
    """
    Mark a todo item as completed.
    
    Args:
        todo_id (int): The ID of the todo item to mark as completed.
    """
    manager = TodoManager()
    try:
        todo_id = int(todo_id)
        if manager.complete_todo(todo_id):
            print(f"Marked todo {todo_id} as completed.")
        else:
            print(f"Todo with ID {todo_id} not found.")
    except ValueError:
        print("Error: Todo ID must be a number.")

def delete(todo_id):
    """
    Delete a todo item.
    
    Args:
        todo_id (int): The ID of the todo item to delete.
    """
    manager = TodoManager()
    try:
        todo_id = int(todo_id)
        if manager.delete_todo(todo_id):
            print(f"Deleted todo {todo_id}.")
        else:
            print(f"Todo with ID {todo_id} not found.")
    except ValueError:
        print("Error: Todo ID must be a number.")

def print_help():
    """Print help information for the todo app."""
    print("Todo App - A simple command-line todo application")
    print("\nUsage:")
    print("  python main.py [command] [arguments]")
    print("\nCommands:")
    print("  add <title>     Add a new todo item")
    print("  list            List all todo items")
    print("  complete <id>   Mark a todo item as completed")
    print("  delete <id>     Delete a todo item")
    print("  help            Show this help message")
    print("\nExamples:")
    print("  python main.py add \"Buy groceries\"")
    print("  python main.py list")
    print("  python main.py complete 1")
    print("  python main.py delete 2")

def main():
    """Main entry point for the todo app."""
    # If no arguments are provided, show help
    if len(sys.argv) == 1:
        print_help()
        return
        
    # Process command-line arguments
    command = sys.argv[1].lower()
    
    if command == "help":
        print_help()
        
    elif command == "add":
        if len(sys.argv) < 3:
            print("Error: Missing todo title. Usage: python main.py add <title>")
            return
            
        title = " ".join(sys.argv[2:])
        add(title)
        
    elif command == "list":
        list_todos()
                
    elif command == "complete":
        if len(sys.argv) < 3:
            print("Error: Missing todo ID. Usage: python main.py complete <id>")
            return
            
        complete(sys.argv[2])
            
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Missing todo ID. Usage: python main.py delete <id>")
            return
            
        delete(sys.argv[2])
            
    else:
        print(f"Unknown command: {command}")
        print('Type "python main.py help" for a list of commands.')

if __name__ == "__main__":
    main()