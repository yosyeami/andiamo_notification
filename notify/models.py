from django.db import models

# Create your models here.
class Notification(models.Model):
    cases=[
        ("sickness","sickness"),
        ("illness","illness"),
        ("personal case","personal case"),
    ]
    # assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notification_sender_driver")
    case= models.CharField(max_length=100, choices=cases)
    reason= models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_Accepted=models.BooleanField(default=False)

    def __str__(self):
        return self.case