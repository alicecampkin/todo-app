from django.test import TestCase
from .models import Todo

# Create your tests here.

todo_title = "Book Dentist Appointment"

class TestTodoModel(TestCase):

    def setUp(self):
        self.todo = Todo.objects.create(
            title=todo_title
        )
    
    def test_todo_created(self):
        self.assertEqual(self.todo.title, todo_title)
    
    def test_date_automatically_assigned(self):
        self.assertTrue(self.todo.created_on)

    def test_status_assigned(self):
        self.assertEqual(self.todo.status, "todo")
    
    def test_str(self):
        self.assertEqual(str(self.todo), todo_title)