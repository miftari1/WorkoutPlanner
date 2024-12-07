from django.contrib import admin

from workoutPlanner.accounts.models import CustomUser, Profile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_superuser', 'is_staff', 'is_active']
    list_filter = ['is_active', 'is_superuser', 'is_staff', 'groups']
    search_fields = ('username', 'email')
    ordering = ('is_superuser', 'is_staff', 'is_active')
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
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'gender', 'goal', 'activity']
    search_fields = ['user__username', 'user__email']
    list_filter = ['activity', 'goal', 'gender', 'age']
    ordering = ['goal', 'activity']
    exclude = ['calories_needed']
    fieldsets = [
        (
            None,
            {'fields': ['user']}
        ),
        (
            'Personal Info',
            {
                'fields':
             [
                 'first_name',
              'last_name',
              'gender',
              'age',
              'height',
              'weight',
              'activity',
              'goal'
              ]
             },
        )
    ]