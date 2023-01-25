from django.urls import path
from exercises.views import *

urlpatterns = [
    path("exercise/", list_exercises, name="list_exercises"),
]
