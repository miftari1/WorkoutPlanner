from django.contrib.auth import get_user_model
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from workoutPlanner.exercises.models import ExerciseModel
from workoutPlanner.workouts.forms import PredefinedWorkoutCreationForm, CustomWorkoutCreationForm
from workoutPlanner.workouts.formsets import CustomWorkoutExerciseFormSet
from workoutPlanner.workouts.models import PredefinedWorkoutModel, CustomWorkoutModel, CustomWorkoutExerciseModel


class PredefinedWorkoutBaseView:
    model = PredefinedWorkoutModel
    context_object_name = 'workout'


class PredefinedWorkoutDetailView(PredefinedWorkoutBaseView, DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exercises = context['workout'].exercises.all()
        context['exercises'] = exercises
        return context


class PredefinedWorkoutListView(PredefinedWorkoutBaseView, ListView):
    template_name = 'workouts/workouts_list.html'
    context_object_name = 'workouts'


class CreatePredefinedWorkoutView(CreateView):
    # model = PredefinedWorkoutModel
    form_class = PredefinedWorkoutCreationForm
    template_name = 'workouts/create_predefined_workout.html'
    success_url = reverse_lazy('workouts:predefined_workout_list')


class CreateCustomWorkoutView(CreateView):
    model = CustomWorkoutExerciseModel
    form_class = CustomWorkoutCreationForm
    template_name = 'workouts/create_custom_workout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Prepopulate the formset if exercise_id is provided in the query params
        formset = CustomWorkoutExerciseFormSet
        exercise_slug = self.kwargs['slug']
        preselected_exercise = None

        if exercise_slug:
            preselected_exercise = get_object_or_404(ExerciseModel, slug=exercise_slug)
            initial_data = [{'exercise': preselected_exercise}]
        else:
            initial_data = []

        if self.request.POST:
            context['formset'] = formset(self.request.POST)
        else:
            context['formset'] = formset(initial=initial_data)

        return context

    def get_success_url(self):
        return reverse_lazy('accounts:profile-details', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        profile = self.request.user.profile
        form.instance.profile = profile
        response =  super().form_valid(form)

        formset = CustomWorkoutExerciseFormSet(self.request.POST, instance=self.object)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    exercise = form.cleaned_data['exercise']
                    self.object.exercises.add(exercise)  # Link exercise to the workout
            formset.save()
        return response


class CustomWorkoutDetailView(DetailView):
    template_name = 'workouts/custom_workout_details.html'
    context_object_name = 'workout'

    def get_queryset(self):
        # CustomWorkout objects for the logged-in user's profile
        profile = self.request.user.profile
        return CustomWorkoutModel.objects.filter(profile=profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_exercises'] = CustomWorkoutExerciseModel.objects.filter(workout=self.object)
        return context


class CustomWorkoutUpdateView(UpdateView):
    model = CustomWorkoutExerciseModel
    template_name = 'workouts/update_workout.html'
    form_class = CustomWorkoutCreationForm

    def get_initial(self):
        initial_data = {'name': self.object.workout.name}
        return initial_data

    def get_context_data(self, **kwargs): #TODO: Need to implement correctly
        context = super().get_context_data(**kwargs)

        # Prepopulate the formset if exercise_id is provided in the query params
        formset = CustomWorkoutExerciseFormSet
        exercise_slug = kwargs['exercise']
        preselected_exercise = None

        if exercise_slug:
            preselected_exercise = get_object_or_404(ExerciseModel, slug=exercise_slug)
            initial_data = [{'exercise': preselected_exercise}]
        else:
            initial_data = []

        if self.request.POST:
            context['formset'] = formset(self.request.POST)
        else:
            context['formset'] = formset(initial=initial_data)

        return context

    def get_success_url(self):
        return reverse_lazy('accounts:profile-details', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        profile = self.request.user.profile
        form.instance.profile = profile
        response = super().form_valid(form)

        formset = CustomWorkoutExerciseFormSet(self.request.POST, instance=self.object)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    exercise = form.cleaned_data['exercise']
                    self.object.exercises.add(exercise)  # Link exercise to the workout
            formset.save()
        return response