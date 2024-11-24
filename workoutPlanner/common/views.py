

from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin

from workoutPlanner.common.forms import NavSearchForm


class HomeView(TemplateView, FormMixin):
    template_name = 'home-page.html'
    form_class = NavSearchForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form_class
        return context
