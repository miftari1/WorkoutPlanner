from workoutPlanner.common.forms import NavSearchForm


def search_form_processor(request):
    return {
        'search_form': NavSearchForm()
    }