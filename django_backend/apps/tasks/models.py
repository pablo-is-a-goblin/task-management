from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

STATUS_CHOICES = [
    ("N", "Not Started"),
    ("W", "Work In Progress"),
    ("F", "Finished"),
]

PRIORITY_CHOICES = [
    ("L", "Low"),
    ("M", "Medium"),
    ("H", "High"),
]

class User(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES)
    priority = models.CharField(choices=PRIORITY_CHOICES)
    due_date = models.DateTimeField()
    estimated_hours = models.DecimalField(decimal_places=2, max_digits=5)
    actual_hours = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    # Relationships
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks_created")
    assigned_to = models.ManyToManyField(User, related_name="assignments")
    tags = models.ManyToManyField(Tag)
    parent_task = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    # Metadata
    metadata = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # Check if a tag is overdue
    def is_overdue(self):
        if timezone.now() > self.due_date:
            return True
        else:
            return False

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


