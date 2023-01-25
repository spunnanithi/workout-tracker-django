from django.urls import path
from exercises.views import *

urlpatterns = [
    path("mine/", show_my_exercises, name="show_my_exercises"),
    path("create/", create_exercise, name="create_exercise"),
]
