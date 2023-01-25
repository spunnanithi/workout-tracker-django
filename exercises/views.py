from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from exercises.models import Exercise
from exercises.forms import ExerciseForm

# Create your views here.


@login_required
def show_my_exercises(request):
    exercises = Exercise.objects.filter(user=request.user)
    context = {
        "exercises": exercises,
    }
    return render(request, "exercises/show_my_exercises.html", context)

@login_required
def create_exercise(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(False)
            exercise.user = request.user
            exercise.save()
            return redirect("list_workouts")
    else:
        form = ExerciseForm()
    context = {
        "form": form,
    }
    return render(request, "exercises/create_exercise.html", context)
