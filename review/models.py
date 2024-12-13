# review/models.py

from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_REVIEW', 'In Review'),
        ('COMPLETED', 'Completed'),
    )

    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PENDING')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CodeSnippet(models.Model):
    session = models.OneToOneField(Session, on_delete=models.CASCADE, related_name='code_snippet')
    file = models.FileField(upload_to='code_snippets/')
    language = models.CharField(max_length=1200)

    def __str__(self):
        return f"{self.session.name} Code Snippet"

class Comment(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    line_number = models.PositiveIntegerField()
    content = models.TextField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.user.username} on line {self.line_number}"

class Reviewer(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='reviewers')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} for {self.session.name}"
