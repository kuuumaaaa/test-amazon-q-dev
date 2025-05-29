"""
Unit tests for the main module.
"""

import unittest
import os
import sys
import io
from unittest.mock import patch
from todo_manager import TodoManager
import main

class TestMain(unittest.TestCase):
    """Test cases for the main module."""
    
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
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add(self, mock_stdout):
        """Test main.add function."""
        main.add("Test Todo")
        output = mock_stdout.getvalue()
        self.assertIn("Added todo: 1. [ ] Test Todo", output)
        
        # Verify the todo was actually added
        todos = self.manager.list_todos()
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0].title, "Test Todo")
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_list_todos(self, mock_stdout):
        """Test main.list_todos function."""
        # Test with no todos
        main.list_todos()
        output = mock_stdout.getvalue()
        self.assertIn("No todos found.", output)
        
        # Add a todo and test again
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        self.manager.add_todo("Test Todo")
        main.list_todos()
        output = mock_stdout.getvalue()
        self.assertIn("Todo List:", output)
        self.assertIn("1. [ ] Test Todo", output)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_complete(self, mock_stdout):
        """Test main.complete function."""
        # Test with non-existent todo
        main.complete("1")
        output = mock_stdout.getvalue()
        self.assertIn("Todo with ID 1 not found.", output)
        
        # Add a todo and test again
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        self.manager.add_todo("Test Todo")
        main.complete("1")
        output = mock_stdout.getvalue()
        self.assertIn("Marked todo 1 as completed.", output)
        
        # Verify the todo was actually marked as completed
        todo = self.manager.get_todo(1)
        self.assertTrue(todo.completed)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_delete(self, mock_stdout):
        """Test main.delete function."""
        # Test with non-existent todo
        main.delete("1")
        output = mock_stdout.getvalue()
        self.assertIn("Todo with ID 1 not found.", output)
        
        # Add a todo and test again
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        self.manager.add_todo("Test Todo")
        main.delete("1")
        output = mock_stdout.getvalue()
        self.assertIn("Deleted todo 1.", output)
        
        # Verify the todo was actually deleted
        todos = self.manager.list_todos()
        self.assertEqual(len(todos), 0)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_help(self, mock_stdout):
        """Test main.print_help function."""
        main.print_help()
        output = mock_stdout.getvalue()
        self.assertIn("Todo App - A simple command-line todo application", output)
        self.assertIn("Usage:", output)
        self.assertIn("Commands:", output)
        self.assertIn("Examples:", output)

if __name__ == "__main__":
    unittest.main()