from django.views.generic import TemplateView, FormView
from django.views.generic.edit import FormMixin

from common.forms import NavSearchForm


class HomeView(TemplateView, FormMixin):
    template_name = 'home-page.html'
    form_class = NavSearchForm
