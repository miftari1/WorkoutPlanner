from django.urls import path

from workoutPlanner.forum.views import PostListCreateAPIView, PostDetail

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='api-post-list-create'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='api-post-detail'),
]