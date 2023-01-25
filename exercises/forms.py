from django.forms import ModelForm
from exercises.models import *


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = [
            "name",
            "goal",
            "sets",
            "reps",
            "weight",
            "met_goal",
            "workout",
        ]
