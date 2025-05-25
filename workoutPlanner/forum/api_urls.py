from django.urls import path

from workoutPlanner.forum.views import PostListCreateAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='api-post-list-create')
]