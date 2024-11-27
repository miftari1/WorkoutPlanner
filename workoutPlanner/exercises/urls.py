from django.urls import path

from workoutPlanner.exercises import views

app_name = 'exercises'

urlpatterns = [
    path('', views.ExerciseListView.as_view(), name='exercise_list'),
    path('add_exercise/', views.AddExerciseView.as_view(), name='add_exercise'),
    path('<slug:slug>/', views.ExerciseDetailView.as_view(), name='exercise_details'),
]