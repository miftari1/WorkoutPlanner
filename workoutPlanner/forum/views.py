from webbrowser import Error

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from workoutPlanner.forum.forms import CreatePostForm, CommentForm, SearchForm
from workoutPlanner.forum.models import Post, Comment


class PostListView(LoginRequiredMixin, ListView, FormMixin):
    login_url = reverse_lazy('accounts:login')
    form_class = SearchForm
    template_name = 'forum/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.all()
        form = self.form_class(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            if query:
                queryset = queryset.filter(body__icontains=query)

        return queryset


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

# class PostCreateView(LoginRequiredMixin, CreateView):
#     login_url = reverse_lazy('accounts:login')
#     model = Post
#     context_object_name = 'post'
#     form_class = CreatePostForm
#     template_name = 'forum/add_post.html'
#
#     def form_valid(self, form):
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = self.request.user
#             post.slug = slugify(post.title)
#             post.save()
#
#         return redirect('forum:post_list')

from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from django.utils.text import slugify
from django.utils import timezone

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            slug=slugify(self.request.data.get('title')),
            publish=timezone.now()
        )

class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save(
                author=self.request.user,
                slug=slugify(self.request.data.get('title')),
                publish=timezone.now()
            )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'forum/post-update.html'
    form_class = CreatePostForm

    def get_success_url(self):
        return reverse_lazy('forum:post_detail', kwargs={'pk': self.object.pk})

    def get_initial(self):
        initial = super().get_initial()
        initial['title'] = self.object.title
        initial['body'] = self.object.body

        return initial


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('forum:post_list')
    template_name = 'forum/delete-post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CreatePostForm(instance=self.object)
        for field in form.fields.values():
            field.widget.attrs['disabled'] = True
        context['form'] = form

        return context

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

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#     def get(self):
#         pass
