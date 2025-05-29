#!/usr/bin/env python3
"""
Todo App - A simple command-line todo application.

This module provides a command-line interface for managing todo items.
"""

import sys
from todo_manager import TodoManager

def print_help():
    """Print help information for the todo app."""
    print("Todo App - A simple command-line todo application")
    print("\nUsage:")
    print("  python todo.py [command] [arguments]")
    print("\nCommands:")
    print("  add <title>     Add a new todo item")
    print("  list            List all todo items")
    print("  complete <id>   Mark a todo item as completed")
    print("  delete <id>     Delete a todo item")
    print("  help            Show this help message")
    print("  quit            Exit the application")
    print("\nExamples:")
    print("  python todo.py add \"Buy groceries\"")
    print("  python todo.py list")
    print("  python todo.py complete 1")
    print("  python todo.py delete 2")

def interactive_mode():
    """Run the todo app in interactive mode."""
    manager = TodoManager()
    
    print("Todo App - Interactive Mode")
    print('Type "help" for a list of commands or "quit" to exit.')
    
    while True:
        try:
            command = input("\nEnter command: ").strip()
            
            if not command:
                continue
                
            parts = command.split(maxsplit=1)
            cmd = parts[0].lower()
            
            if cmd == "quit" or cmd == "exit":
                print("Goodbye!")
                break
                
            elif cmd == "help":
                print_help()
                
            elif cmd == "add":
                if len(parts) < 2:
                    print("Error: Missing todo title. Usage: add <title>")
                    continue
                    
                title = parts[1]
                todo = manager.add_todo(title)
                print(f"Added todo: {todo}")
                
            elif cmd == "list":
                todos = manager.list_todos()
                if not todos:
                    print("No todos found.")
                else:
                    print("Todo List:")
                    for todo in todos:
                        print(f"  {todo}")
                        
            elif cmd == "complete":
                if len(parts) < 2:
                    print("Error: Missing todo ID. Usage: complete <id>")
                    continue
                    
                try:
                    todo_id = int(parts[1])
                    if manager.complete_todo(todo_id):
                        print(f"Marked todo {todo_id} as completed.")
                    else:
                        print(f"Todo with ID {todo_id} not found.")
                except ValueError:
                    print("Error: Todo ID must be a number.")
                    
            elif cmd == "delete":
                if len(parts) < 2:
                    print("Error: Missing todo ID. Usage: delete <id>")
                    continue
                    
                try:
                    todo_id = int(parts[1])
                    if manager.delete_todo(todo_id):
                        print(f"Deleted todo {todo_id}.")
                    else:
                        print(f"Todo with ID {todo_id} not found.")
                except ValueError:
                    print("Error: Todo ID must be a number.")
                    
            else:
                print(f"Unknown command: {cmd}")
                print('Type "help" for a list of commands.')
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

def main():
    """Main entry point for the todo app."""
    manager = TodoManager()
    
    # If no arguments are provided, run in interactive mode
    if len(sys.argv) == 1:
        interactive_mode()
        return
        
    # Process command-line arguments
    command = sys.argv[1].lower()
    
    if command == "help":
        print_help()
        
    elif command == "add":
        if len(sys.argv) < 3:
            print("Error: Missing todo title. Usage: python todo.py add <title>")
            return
            
        title = " ".join(sys.argv[2:])
        todo = manager.add_todo(title)
        print(f"Added todo: {todo}")
        
    elif command == "list":
        todos = manager.list_todos()
        if not todos:
            print("No todos found.")
        else:
            print("Todo List:")
            for todo in todos:
                print(f"  {todo}")
                
    elif command == "complete":
        if len(sys.argv) < 3:
            print("Error: Missing todo ID. Usage: python todo.py complete <id>")
            return
            
        try:
            todo_id = int(sys.argv[2])
            if manager.complete_todo(todo_id):
                print(f"Marked todo {todo_id} as completed.")
            else:
                print(f"Todo with ID {todo_id} not found.")
        except ValueError:
            print("Error: Todo ID must be a number.")
            
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Missing todo ID. Usage: python todo.py delete <id>")
            return
            
        try:
            todo_id = int(sys.argv[2])
            if manager.delete_todo(todo_id):
                print(f"Deleted todo {todo_id}.")
            else:
                print(f"Todo with ID {todo_id} not found.")
        except ValueError:
            print("Error: Todo ID must be a number.")
            
    else:
        print(f"Unknown command: {command}")
        print('Type "python todo.py help" for a list of commands.')

if __name__ == "__main__":
    main()