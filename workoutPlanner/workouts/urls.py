from django.urls import path, include

from workoutPlanner.workouts import views

app_name = 'workouts'

urlpatterns = [
    path('', views.PredefinedWorkoutListView.as_view(), name='predefined_workout_list'),
    path('create_workout/', views.CreatePredefinedWorkoutView.as_view(), name='create_predefined_workout'),
    path('create_custom_workout/<slug:slug>/', views.CreateCustomWorkoutView.as_view(), name='create_custom_workout'),
    path('update_workout/', include([
        path('<slug:slug>/', views.CustomWorkoutUpdateView.as_view(), name='update_workout'),
    ])
    ),
    path('custom/', include([
        path('', views.CustomWorkoutListView.as_view(), name='custom_workouts_list'),
        path('remove_exercise/<int:pk>/', views.DeleteCustomWorkoutExerciseView.as_view(), name='remove_exercise'),
        path('<slug:slug>/', include([
            path('', views.CustomWorkoutDetailView.as_view(), name='custom_workout_detail'),
            path('delete/', views.CustomWorkoutDeleteView.as_view(), name='custom_workout_delete'),
        ])),
    ])),
    path('<slug:slug>/', views.PredefinedWorkoutDetailView.as_view(), name='predefined_workout_detail'),
]