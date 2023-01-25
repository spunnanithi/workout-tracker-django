from django.db import models
from django.conf import settings


# Create your models here.


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="workouts",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name
