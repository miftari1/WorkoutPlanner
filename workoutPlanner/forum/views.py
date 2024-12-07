from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView

from workoutPlanner.forum.forms import CreatePostForm
from workoutPlanner.forum.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'forum/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'forum/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    context_object_name = 'post'
    form_class = CreatePostForm
    template_name = 'forum/add_post.html'

    def form_valid(self, form):
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.slug = slugify(post.title)
            post.save()

        return redirect('forum:post_list')
