"""
Unit tests for the Todo App.
"""

import unittest
import os
import json
import sys
from todo_item import TodoItem
from todo_manager import TodoManager
import main

class TestTodoItem(unittest.TestCase):
    """Test cases for the TodoItem class."""
    
    def test_init(self):
        """Test TodoItem initialization."""
        todo = TodoItem(1, "Test Todo")
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, "Test Todo")
        self.assertFalse(todo.completed)
        
        todo = TodoItem(2, "Completed Todo", True)
        self.assertEqual(todo.id, 2)
        self.assertEqual(todo.title, "Completed Todo")
        self.assertTrue(todo.completed)
    
    def test_to_dict(self):
        """Test TodoItem.to_dict method."""
        todo = TodoItem(1, "Test Todo")
        todo_dict = todo.to_dict()
        self.assertEqual(todo_dict, {
            'id': 1,
            'title': 'Test Todo',
            'completed': False
        })
        
        todo.completed = True
        todo_dict = todo.to_dict()
        self.assertEqual(todo_dict, {
            'id': 1,
            'title': 'Test Todo',
            'completed': True
        })
    
    def test_from_dict(self):
        """Test TodoItem.from_dict method."""
        todo_dict = {
            'id': 1,
            'title': 'Test Todo',
            'completed': False
        }
        todo = TodoItem.from_dict(todo_dict)
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, 'Test Todo')
        self.assertFalse(todo.completed)
        
        todo_dict = {
            'id': 2,
            'title': 'Completed Todo',
            'completed': True
        }
        todo = TodoItem.from_dict(todo_dict)
        self.assertEqual(todo.id, 2)
        self.assertEqual(todo.title, 'Completed Todo')
        self.assertTrue(todo.completed)
    
    def test_str(self):
        """Test TodoItem.__str__ method."""
        todo = TodoItem(1, "Test Todo")
        self.assertEqual(str(todo), "1. [ ] Test Todo")
        
        todo.completed = True
        self.assertEqual(str(todo), "1. [X] Test Todo")

class TestTodoManager(unittest.TestCase):
    """Test cases for the TodoManager class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_file = "test_todos.json"
        # Ensure the test file doesn't exist
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.manager = TodoManager(self.test_file)
    
    def tearDown(self):
        """Tear down test fixtures."""
        # Clean up the test file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_todo(self):
        """Test TodoManager.add_todo method."""
        todo = self.manager.add_todo("Test Todo")
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, "Test Todo")
        self.assertFalse(todo.completed)
        self.assertEqual(len(self.manager.todos), 1)
        
        todo = self.manager.add_todo("Another Todo")
        self.assertEqual(todo.id, 2)
        self.assertEqual(todo.title, "Another Todo")
        self.assertFalse(todo.completed)
        self.assertEqual(len(self.manager.todos), 2)
    
    def test_list_todos(self):
        """Test TodoManager.list_todos method."""
        self.assertEqual(len(self.manager.list_todos()), 0)
        
        self.manager.add_todo("Test Todo")
        self.manager.add_todo("Another Todo")
        todos = self.manager.list_todos()
        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[0].title, "Test Todo")
        self.assertEqual(todos[1].title, "Another Todo")
    
    def test_get_todo(self):
        """Test TodoManager.get_todo method."""
        self.assertIsNone(self.manager.get_todo(1))
        
        self.manager.add_todo("Test Todo")
        todo = self.manager.get_todo(1)
        self.assertIsNotNone(todo)
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, "Test Todo")
        
        self.assertIsNone(self.manager.get_todo(2))
    
    def test_complete_todo(self):
        """Test TodoManager.complete_todo method."""
        self.assertFalse(self.manager.complete_todo(1))
        
        self.manager.add_todo("Test Todo")
        self.assertTrue(self.manager.complete_todo(1))
        todo = self.manager.get_todo(1)
        self.assertTrue(todo.completed)
    
    def test_delete_todo(self):
        """Test TodoManager.delete_todo method."""
        self.assertFalse(self.manager.delete_todo(1))
        
        self.manager.add_todo("Test Todo")
        self.assertTrue(self.manager.delete_todo(1))
        self.assertEqual(len(self.manager.todos), 0)
    
    def test_save_and_load_todos(self):
        """Test TodoManager.save_todos and TodoManager.load_todos methods."""
        self.manager.add_todo("Test Todo")
        self.manager.add_todo("Another Todo")
        self.manager.complete_todo(1)
        
        # Create a new manager to load the saved todos
        new_manager = TodoManager(self.test_file)
        todos = new_manager.list_todos()
        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[0].id, 1)
        self.assertEqual(todos[0].title, "Test Todo")
        self.assertTrue(todos[0].completed)
        self.assertEqual(todos[1].id, 2)
        self.assertEqual(todos[1].title, "Another Todo")
        self.assertFalse(todos[1].completed)

if __name__ == "__main__":
    # Check if command line arguments are provided
    if len(sys.argv) > 1:
        # If arguments are provided, redirect to main.py
        main.main()
    else:
        # Otherwise, run the tests
        unittest.main()