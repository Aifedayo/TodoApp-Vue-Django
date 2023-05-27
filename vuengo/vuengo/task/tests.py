from django.test import TestCase
from datetime import datetime
from .models import Task

class TaskModelTestCase(TestCase):
    """ Create a testcase for Task Model """
    def setUp(self):
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task',
            status=Task.TODO,
            created_at=datetime(2023, 5, 1),
            done_at=datetime(2023, 5, 27)
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'This is a test task')
        self.assertEqual(self.task.status, Task.TODO)
        self.assertEqual(self.task.created_at, datetime(2023, 5, 1))
        self.assertEqual(self.task.done_at, datetime(2023, 5, 27))

    def test_formatted_created_date(self):
        expected_date = 'Sunday 05 2023'
        self.assertEqual(self.task.formatted_created_date, expected_date)

    def test_formatted_done_date(self):
        expected_date = 'Thursday 05 2023'
        self.assertEqual(self.task.formatted_done_date, expected_date)
