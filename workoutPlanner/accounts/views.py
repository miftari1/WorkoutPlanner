from django.contrib.auth import get_user_model, login, logout

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from django.views.generic import CreateView, DeleteView, DetailView
from django.views.generic.edit import FormMixin

from workoutPlanner.accounts.forms import AccountCreationForm, AccountDeleteForm, ProfileUpdateForm
from workoutPlanner.accounts.models import Profile

UserModel = get_user_model()

class MyLoginView(LoginView):
    pass

class MyLogoutView(LogoutView):
    pass


class UserRegistrationView(CreateView):
    form_class = AccountCreationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('common:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(request=self.request, user=self.object)
        return response

class UserDeleteView(DeleteView):
    model = UserModel
    template_name = 'registration/account_deletion.html'
    success_url = reverse_lazy('common:home')

    def get_initial(self):
        initial = {
            'username': self.object.username,
            'email': self.object.email,
        }
        return initial

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        logout(request)
        return super().delete(request, *args, **kwargs)

class ProfileDetailView(DetailView):
    model = UserModel
    template_name = 'profile_page.html'
    context_object_name = 'user'


class ProfileConfView(CreateView):
    model = Profile
    template_name = 'registration/profile_config.html'
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('accounts:profile-details')


    def form_valid(self, form):
        # Assign the currently logged-in user to the profile
        form.instance.user = self.request.user
        return super().form_valid(form)
