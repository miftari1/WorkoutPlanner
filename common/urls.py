from django.urls import path

from common import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
]