from django.forms import ModelForm
from tracker.models import *


class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = [
            "name",
            "description",
        ]
