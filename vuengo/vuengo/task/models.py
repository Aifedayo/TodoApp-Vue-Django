from django.db import models

class Task(models.Model):
    TODO = 'todo'
    DONE = 'done'

    STATUS_CHOICES = (
        (TODO, 'Todo'),
        (DONE, 'Done')
    )

    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO)

    def __str__(self):
        return self.title or ''
