from django import forms

from workoutPlanner.forum.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']