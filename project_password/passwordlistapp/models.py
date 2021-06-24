from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Password(models.Model):
    STATUS_CHOICES = (
        ('running', 'running'),
        ('deprovision', 'deprovision')
    )
    passw = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name='passws', on_delete=models.CASCADE)
    title = models.TextField()
    deleted = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=27, choices=STATUS_CHOICES, default='running')

class Meta:
    ordering = ('-updated',)

def __str__(self):
    return self.title