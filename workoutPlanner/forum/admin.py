from django.contrib import admin

from workoutPlanner.forum.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
