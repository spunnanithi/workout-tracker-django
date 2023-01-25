from django.contrib import admin
from exercises.models import Exercise

# Register your models here.


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        "created_on",
        "name",
        "goal",
        "sets",
        "reps",
        "weight",
        "met_goal",
        "updated_on",
        "user",
        "id",
    )
