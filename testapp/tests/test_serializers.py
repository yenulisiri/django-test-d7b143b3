from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from testapp.models import Todo
from testapp.serializers import TodoSerializer

class SerializerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.todo = Todo.objects.create(title="Test Todo", is_completed=False)
            
    def test_serializer_valid_data(self):
        data = {'title': 'Valid Todo', 'is_completed': True}
        serializer = TodoSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Todo.objects.count(), 2) # 1 from setUp, 1 created here
        
    def test_serializer_invalid_data(self):
        data = {'title': '', 'is_completed': False}
        serializer = TodoSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)