from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from workoutPlanner.exercises.models import ExerciseModel
from workoutPlanner.workouts.forms import PredefinedWorkoutCreationForm, CustomWorkoutCreationForm
from workoutPlanner.workouts.formsets import CustomWorkoutExerciseFormSet, UpdateCustomWorkoutExerciseFormSet
from workoutPlanner.workouts.models import PredefinedWorkoutModel, CustomWorkoutModel, CustomWorkoutExerciseModel


class PredefinedWorkoutBaseView:
    model = PredefinedWorkoutModel
    context_object_name = 'workout'


class PredefinedWorkoutDetailView(LoginRequiredMixin, PredefinedWorkoutBaseView, DetailView):
    login_url = reverse_lazy('accounts:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exercises = context['workout'].exercises.all()
        context['exercises'] = exercises
        return context


class PredefinedWorkoutListView(LoginRequiredMixin, PredefinedWorkoutBaseView, ListView):
    login_url = reverse_lazy('accounts:login')
    template_name = 'workouts/workouts_list.html'
    context_object_name = 'workouts'


class CreatePredefinedWorkoutView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    form_class = PredefinedWorkoutCreationForm
    template_name = 'workouts/create_predefined_workout.html'
    success_url = reverse_lazy('workouts:predefined_workout_list')


class CreateCustomWorkoutView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    model = CustomWorkoutModel
    form_class = CustomWorkoutCreationForm
    template_name = 'workouts/create_custom_workout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Prepopulate formset exercise field
        formset = CustomWorkoutExerciseFormSet
        exercise_slug = self.kwargs['slug']

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
        return reverse_lazy('workouts:custom_workouts_list')

    def form_valid(self, form):
        # Associate the workout with the user's profile
        profile = self.request.user.profile
        form.instance.profile_id = profile.user_id

        # Save the main form (the workout instance)
        response = super().form_valid(form)

        formset = CustomWorkoutExerciseFormSet(
            self.request.POST,
            instance=self.object,
            )

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    custom_exercise = form.save(commit=False)
                    custom_exercise.exercise = form.cleaned_data['exercise']
                    custom_exercise.save()

        return response


class CustomWorkoutDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('accounts:login')
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


class CustomWorkoutListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('accounts:login')
    template_name = 'workouts/custom_workouts_list.html'
    context_object_name = 'workouts'

    def get_queryset(self):
        return CustomWorkoutModel.objects.filter(profile_id=self.request.user.id)



class CustomWorkoutUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('accounts:login')
    model = CustomWorkoutModel
    template_name = 'workouts/update_workout.html'
    form_class = CustomWorkoutCreationForm

    def get_initial(self):
        initial_data = {'name': self.object}
        return initial_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        formset = UpdateCustomWorkoutExerciseFormSet
        context['formset'] = formset(self.request.POST or None)

        return context


    def get_success_url(self):
        return reverse_lazy('workouts:custom_workouts_list')

    def form_valid(self, form):
        profile = self.request.user.profile
        form.instance.profile = profile
        response = super().form_valid(form)

        formset = UpdateCustomWorkoutExerciseFormSet(self.request.POST)

        if formset.is_valid():
            for form in formset:
                custom_exercise = form.save(commit=False)
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    exercise = form.cleaned_data['exercise']
                    custom_exercise.exercise = exercise
                    custom_exercise.workout = self.object
                    form.save()
        return response


class CustomWorkoutDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('accounts:login')
    form_class = CustomWorkoutCreationForm
    success_url = reverse_lazy('workouts:custom_workouts_list')
    context_object_name = 'workout'
    template_name = 'workouts/delete_custom_workout.html'

    def get_initial(self):
        initial_data = {'name': self.object.name}
        return initial_data

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].disabled = True
        return form

    def get_queryset(self):
        return CustomWorkoutModel.objects.filter(profile_id=self.request.user.id)