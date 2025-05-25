from rest_framework import serializers

from workoutPlanner.forum.models import Post


# from workoutPlanner.forum.models import Comment
#
#
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'author',
            'body',
            'publish',
            'created',
            'updated',
            'status',
        ]
        read_only_fields = ['slug', 'author', 'created', 'updated', 'publish']
