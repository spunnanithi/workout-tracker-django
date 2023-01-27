from django.urls import path
from exercises.views import *

urlpatterns = [
    path("exercise/<int:id>/", show_my_exercises, name="show_my_exercises"),
    path("create/", create_exercise, name="create_exercise"),
    path("<int:id>/", individual_exercise, name="individual_exercise"),
    path("<int:id>/delete/", delete_exercise, name="delete_exercise"),
    path("<int:id>/edit/", edit_exercise, name="edit_exercise"),
]
