from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_name
    
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    sender = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return str(self.message)