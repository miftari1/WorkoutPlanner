from django.urls import path

from workoutPlanner.workouts import views

app_name = 'workouts'

urlpatterns = [
    path('', views.PredefinedWorkoutListView.as_view(), name='predefined_workout_list'),
    path('create_workout/', views.CreatePredefinedWorkoutView.as_view(), name='create_predefined_workout'),
    path('<slug:slug>/', views.PredefinedWorkoutDetailView.as_view(), name='predefined_workout_detail'),
]