from django.db import models

# Create your models here.

SATTUS = (
    ('todo', 'To Do'),
    ('inprogress', 'In Progress'),
    ('done', 'Done'),
)
class Task(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=SATTUS, default='todo') 
    def __str__(self):
        return self.name