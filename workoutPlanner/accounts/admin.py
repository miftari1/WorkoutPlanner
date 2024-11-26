from django.contrib import admin

from workoutPlanner.accounts.models import CustomUser, Profile


@admin.register(CustomUser, Profile)
class CustomUserAdmin(admin.ModelAdmin):
    pass
