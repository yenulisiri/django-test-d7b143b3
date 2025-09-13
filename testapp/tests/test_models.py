from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from testapp.models import Todo

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_model_creation(self):
        todo = Todo.objects.create(title="Test Todo", is_completed=False)
        self.assertEqual(todo.title, "Test Todo")
        self.assertFalse(todo.is_completed)
        self.assertEqual(str(todo), "Test Todo") # Test __str__ method
        
    def test_model_validation(self):
        todo = Todo(title="A" * 201) # Title too long
        with self.assertRaises(ValidationError):
            todo.full_clean() # Trigger validation

    def test_model_methods(self):
        pass