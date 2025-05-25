from django.urls import path, include

from workoutPlanner.forum import views
from workoutPlanner.forum.views import PostListCreateAPIView

app_name = 'forum'
urlpatterns = [
    path('', include([
        path('', views.PostListView.as_view(), name='post_list'),
        path('<int:pk>/', include([
            path('', views.PostDetailView.as_view(), name='post_detail'),
            path('edit/', views.PostUpdateView.as_view(), name='post_update'),
            path('delete/', views.PostDeleteView.as_view(), name='post_delete'),
            path('comment/', views.AddCommentView.as_view(), name='add_comment'),
        ])),
    ])),

]