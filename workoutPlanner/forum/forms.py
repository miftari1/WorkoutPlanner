from workoutPlanner.forum.models import Post, Comment

from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search...',
                'class': 'search-bar',
            }
        ),
        required=False,
        label='',
    )

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        labels = {
            'title': '',
            'body': ''
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title...',}),
            'body': forms.Textarea(attrs={'placeholder': 'Share your thoughts...'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': ''
        }
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Write a comment...'})
        }