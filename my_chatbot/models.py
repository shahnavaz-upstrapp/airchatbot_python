from django.db import models
from users.models import User

class ChatHistory(models.Model):
    question = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "ChatHistory"
        verbose_name_plural = "ChatHistories"
        ordering = ["created_at"]
        
    def __str__(self):
        return self.question