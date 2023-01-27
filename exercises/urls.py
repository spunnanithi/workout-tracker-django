from django.urls import path
from exercises.views import *

urlpatterns = [
    path("<int:id>", show_my_exercises, name="show_my_exercises"),
    path("create/", create_exercise, name="create_exercise"),
]
