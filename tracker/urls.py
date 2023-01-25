from django.urls import path
from tracker.views import *


urlpatterns = [
    path("workouts/", list_workouts, name="list_workouts"),
]
