from django.urls import path
from tracker.views import *


urlpatterns = [
    path("workouts/", list_workouts, name="list_workouts"),
    path("<int:id>/", show_my_workout, name="show_my_workout"),
    path("create/", create_workout, name="create_workout"),
]
