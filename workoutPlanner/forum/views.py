from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView

from workoutPlanner.forum.forms import CreatePostForm, CommentForm
from workoutPlanner.forum.models import Post, Comment


class PostListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('accounts:login')
    model = Post
    template_name = 'forum/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('accounts:login')
    model = Post
    context_object_name = 'post'
    template_name = 'forum/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(active=True)
        context['form'] = CommentForm()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
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


class AddCommentView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    model = Comment
    form_class = CommentForm
    template_name = 'forum/add_comment.html'

    def form_valid(self, form):
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=self.kwargs['pk'])
            comment.name = self.request.user.username
            comment.email = self.request.user.email
            comment.save()

            return redirect('forum:post_detail', pk=self.kwargs['pk'])