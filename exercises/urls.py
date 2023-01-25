from django.urls import path
from exercises.views import *

urlpatterns = [
    path("exercise/", list_exercises, name="list_exercises"),
    path("create/", create_exercise, name="create_exercise"),
]
