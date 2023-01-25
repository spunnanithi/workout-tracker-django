from django.contrib import admin
from tracker.models import *

# Register your models here.


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_on",
        "updated_on",
        "user",
        "id",
    )
