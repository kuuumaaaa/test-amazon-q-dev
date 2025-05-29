"""
Todo Manager module for the Todo App.
This module defines the TodoManager class which manages todo items.
"""

import json
import os
from todo_item import TodoItem

class TodoManager:
    """
    A class for managing todo items.
    
    Attributes:
        todos (list): A list of TodoItem objects.
        next_id (int): The next available ID for a new todo item.
        filename (str): The name of the file to save todos to.
    """
    
    def __init__(self, filename="todos.json"):
        """
        Initialize a new TodoManager.
        
        Args:
            filename (str, optional): The name of the file to save todos to. Defaults to "todos.json".
        """
        self.todos = []
        self.next_id = 1
        self.filename = filename
        self.load_todos()
    
    def add_todo(self, title):
        """
        Add a new todo item.
        
        Args:
            title (str): The title or description of the todo item.
            
        Returns:
            TodoItem: The newly created TodoItem.
        """
        todo = TodoItem(self.next_id, title)
        self.todos.append(todo)
        self.next_id += 1
        self.save_todos()
        return todo
    
    def list_todos(self):
        """
        Get all todo items.
        
        Returns:
            list: A list of all TodoItem objects.
        """
        return self.todos
    
    def get_todo(self, todo_id):
        """
        Get a todo item by ID.
        
        Args:
            todo_id (int): The ID of the todo item to get.
            
        Returns:
            TodoItem or None: The TodoItem with the specified ID, or None if not found.
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None
    
    def complete_todo(self, todo_id):
        """
        Mark a todo item as completed.
        
        Args:
            todo_id (int): The ID of the todo item to mark as completed.
            
        Returns:
            bool: True if the todo item was found and marked as completed, False otherwise.
        """
        todo = self.get_todo(todo_id)
        if todo:
            todo.completed = True
            self.save_todos()
            return True
        return False
    
    def delete_todo(self, todo_id):
        """
        Delete a todo item.
        
        Args:
            todo_id (int): The ID of the todo item to delete.
            
        Returns:
            bool: True if the todo item was found and deleted, False otherwise.
        """
        todo = self.get_todo(todo_id)
        if todo:
            self.todos.remove(todo)
            self.save_todos()
            return True
        return False
    
    def save_todos(self):
        """
        Save all todo items to a file.
        """
        data = {
            'next_id': self.next_id,
            'todos': [todo.to_dict() for todo in self.todos]
        }
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_todos(self):
        """
        Load todo items from a file.
        """
        if not os.path.exists(self.filename):
            return
        
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.next_id = data.get('next_id', 1)
                self.todos = [TodoItem.from_dict(todo_data) for todo_data in data.get('todos', [])]
        except (json.JSONDecodeError, KeyError):
            # If the file is corrupted or has an invalid format, start with an empty list
            self.todos = []
            self.next_id = 1