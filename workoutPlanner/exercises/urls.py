

from django.urls import path, include

from workoutPlanner.exercises import views

app_name = 'exercises'

urlpatterns = [
    path('add_exercise/', views.AddExerciseView.as_view(), name='add_exercise'),
    path('details/', include([
        path('<slug:slug>/', views.ExerciseDetailView.as_view(), name='exercise_details'),
    ])),
    path('<str:category>/', views.ExerciseListView.as_view(), name='exercise_list'),
]