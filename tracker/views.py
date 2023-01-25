from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from tracker.models import *

# Create your views here.


@login_required
def list_workouts(request):
    workouts = Workout.objects.filter(user=request.user)
    context = {
        "workouts": workouts,
    }
    return render(request, "tracker/list_workouts.html", context)

@login_required
def show_my_workout(request, id):
    workout = get_object_or_404(Workout, id=id)
    context = {
        "workout": workout,
    }
    return render(request, "tracker/detail.html", context)
