from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from exercises.models import *

# Create your views here.


@login_required
def list_exercises(request):
    exercises = Exercise.objects.filter(user=request.user)
    context = {
        "exercises": exercises,
    }
    return render(request, "exercises/list_exercises.html", context)
