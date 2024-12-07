from django.shortcuts import render
from django.views.generic import ListView, DetailView

from workoutPlanner.forum.models import Post


class PostListView(ListView):
    template_name = 'forum/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.published.all()


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'forum/post_detail.html'
