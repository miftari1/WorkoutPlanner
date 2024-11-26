from django.contrib import admin

from workoutPlanner.accounts.models import CustomUser, Profile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Credentials',
            {'fields': ['username','email', 'password']},
        ),
        (
            'Groups and Permissions',
            {'fields': ['groups', 'user_permissions']}
        ),
        (
            'Status',
            {'fields': ['is_superuser', 'is_staff', 'is_active']}
        )
    ]
