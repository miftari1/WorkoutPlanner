from django.urls import path

from workoutPlanner.common import views

app_name = 'common'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
