from django.urls import path, include

from workoutPlanner.forum import views

app_name = 'forum'
urlpatterns = [
    path('', include([
        path('', views.PostListView.as_view(), name='post_list'),
        path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    ])),

]