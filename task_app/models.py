from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    STATUS_CHOISES = [
        ('todo', 'Треба зробити'),
        ('in_progress', 'Виконується'),
        ('done', 'Виконано'),
    ]

    PRIORITY_CHOISES = [
        ('low', 'Низбкий'),
        ('middle', 'Середній'),
        ('high', 'Високий'),
    ]

    

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOISES, default='todo')
    proirity = models.CharField(max_length=15, choices=PRIORITY_CHOISES, default='middle')
    deadline = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    




