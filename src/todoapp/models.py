from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Todo(models.Model):
    task = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    expiry = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.task
    