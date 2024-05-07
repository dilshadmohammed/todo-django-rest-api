from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Todo(models.Model):
    task = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    expiry = models.DateTimeField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.task
    
    def save(self, *args, **kwargs):
        if not self.expiry:
            self.expiry = timezone.now() + timedelta(days=1)
        super().save(*args, **kwargs)
    