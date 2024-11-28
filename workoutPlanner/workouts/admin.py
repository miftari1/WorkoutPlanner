from django.contrib import admin

from workoutPlanner.workouts.models import PredefinedWorkoutModel


@admin.register(PredefinedWorkoutModel)
class WorkoutAdmin(admin.ModelAdmin):
    exclude = ['slug']
    search_fields = ['name', 'overview', 'content', 'effects', 'level', 'training_type']
    list_display = ['name', 'training_type', 'level']
    list_filter = ['name', 'training_type', 'level']
    show_facets = admin.ShowFacets.ALWAYS
    fieldsets = [
        (
            'Workout name',
            {'fields': ['name']}
        ),
        (
            'Constitutive exercises',
            {'fields': ['exercises']}
        ),
        (
            'Essential information',
            {'fields': ['level', 'training_type', 'overview', 'content', 'workout_manual', 'effects']}
        ),
        (
            'Additional information',
            {'fields': ['extra_info']}
        )
    ]
