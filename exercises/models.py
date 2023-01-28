from django.db import models
from django.conf import settings

# Create your models here.


class Exercise(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)
    goal = models.CharField(max_length=200, default=0)
    sets = models.PositiveSmallIntegerField(default=0)
    reps = models.PositiveSmallIntegerField(default=0)
    weight = models.PositiveSmallIntegerField(default=0)
    met_goal = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)
    workout = models.ForeignKey(
        "tracker.Workout",
        related_name="exercises",
        on_delete=models.CASCADE,
        null=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="exercises",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
