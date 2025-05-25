from lib2to3.fixes.fix_input import context

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView

from workoutPlanner.exercises.forms import AddExerciseForm
from workoutPlanner.exercises.models import ExerciseModel



class ExerciseDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('accounts:login')
    model = ExerciseModel
    template_name = 'exercises/exercise_details.html'
    context_object_name = 'exercise'

class ExerciseListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('accounts:login')
    template_name = 'exercises/exercises_list.html'
    context_object_name = 'exercises'

    def get_queryset(self):
        category = self.kwargs.get('category')
        return ExerciseModel.objects.filter(muscle_groups__exact=category)



class AddExerciseView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    form_class = AddExerciseForm
    template_name = 'exercises/add_exercise.html'

    def form_valid(self, form):
        exercise = form.save()
        return redirect('exercises:exercise_details', kwargs={'slug': exercise.slug})

    

