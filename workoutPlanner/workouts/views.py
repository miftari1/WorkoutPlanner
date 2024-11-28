from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from workoutPlanner.workouts.forms import PredefinedWorkoutCreationForm
from workoutPlanner.workouts.models import PredefinedWorkoutModel


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


