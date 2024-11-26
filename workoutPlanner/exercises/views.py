from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView

from workoutPlanner.exercises.forms import AddExerciseForm
from workoutPlanner.exercises.models import ExerciseModel


class ExerciseDetailView(DetailView):
    model = ExerciseModel
    template_name = 'exercises/exercise_details.html'
    context_object_name = 'exercise'

class AddExerciseView(CreateView):
    form_class = AddExerciseForm
    template_name = 'exercises/add_exercise.html'

    def form_valid(self, form):
        exercise = form.save()
        return HttpResponseRedirect(reverse('exercises:exercise_details', kwargs={'slug': exercise.slug}))

