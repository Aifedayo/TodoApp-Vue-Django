from django.db import models

class Task(models.Model):
    TODO = 'todo'
    DONE = 'done'

    STATUS_CHOICES = (
        (TODO, 'Todo'),
        (DONE, 'Done')
    )

    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO)
    created_at = models.DateTimeField(auto_now_add=True)
    done_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title or ''
    
    @property
    def formatted_created_date(self):
        return self.created_at.strftime("%A %m %Y")
    
    @property
    def formatted_done_date(self):
        return self.done_at.strftime("%A %m %Y")
