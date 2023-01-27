from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from exercises.models import Exercise
from tracker.models import Workout
from exercises.forms import ExerciseForm

# Create your views here.


@login_required
def show_my_exercises(request, id):
    workout = get_object_or_404(Workout, id=id)
    exercises = Exercise.objects.filter(user=request.user).filter(id=id)
    context = {
        "exercises": exercises,
        "workout": workout,
    }
    return render(request, "exercises/show_my_exercises.html", context)

@login_required
def individual_exercise(request, id):
    exercise = get_object_or_404(Exercise, id=id)
    context = {
        "exercise": exercise,
    }
    return render(request, "exercises/individual_exercise.html", context)

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

@login_required
def delete_exercise(request, id):
    exercise = get_object_or_404(Exercise, id=id)
    if request.method == "POST":
        exercise.delete()
        return redirect("list_workouts")
    context = {
        "exercise": exercise,
    }
    return render(request, "exercises/delete_exercise.html", context)

@login_required
def edit_exercise(request, id):
    exercise = get_object_or_404(Exercise, id=id)
    if request.method == "POST":
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid:
            form.save()
            return redirect("list_workouts")
    else:
        form = ExerciseForm(instance=exercise)
    context = {
        "form": form,
    }
    return render(request, "exercises/edit_exercise.html", context)
