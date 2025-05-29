"""
Todo Item module for the Todo App.
This module defines the TodoItem class which represents a single todo item.
"""

class TodoItem:
    """
    A class representing a single todo item.
    
    Attributes:
        id (int): The unique identifier for the todo item.
        title (str): The title or description of the todo item.
        completed (bool): The completion status of the todo item.
    """
    
    def __init__(self, id, title, completed=False):
        """
        Initialize a new TodoItem.
        
        Args:
            id (int): The unique identifier for the todo item.
            title (str): The title or description of the todo item.
            completed (bool, optional): The completion status of the todo item. Defaults to False.
        """
        self.id = id
        self.title = title
        self.completed = completed
    
    def to_dict(self):
        """
        Convert the TodoItem to a dictionary.
        
        Returns:
            dict: A dictionary representation of the TodoItem.
        """
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a TodoItem from a dictionary.
        
        Args:
            data (dict): A dictionary containing the TodoItem data.
            
        Returns:
            TodoItem: A new TodoItem instance.
        """
        return cls(
            id=data['id'],
            title=data['title'],
            completed=data.get('completed', False)
        )
    
    def __str__(self):
        """
        Return a string representation of the TodoItem.
        
        Returns:
            str: A string representation of the TodoItem.
        """
        status = "[X]" if self.completed else "[ ]"
        return f"{self.id}. {status} {self.title}"