from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from workoutPlanner.accounts.forms import AccountCreationForm, ProfileUpdateForm, LoginForm
from workoutPlanner.accounts.models import Profile
from workoutPlanner.workouts.models import CustomWorkoutModel

UserModel = get_user_model()

class MyLoginView(LoginView):
    form_class = LoginForm
    # def get_context_data(self, **kwargs):
    #     form = LoginForm(self.request.POST or None)
    #     return {'form': form}

    # def form_valid(self, form):
    #     if form.is_valid():
    #         print("Form is valid")
    #     else:
    #         print("Form errors:", form.errors)

class MyLogoutView(LoginRequiredMixin, LogoutView):
    login_url = reverse_lazy('accounts:login')


class UserRegistrationView(CreateView):
    form_class = AccountCreationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('common:home')

    def form_valid(self, form):
        if form.is_valid():
            response = super().form_valid(form)
            login(request=self.request, user=self.object)
            return response

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    login_url = reverse_lazy('accounts:login')
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

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserModel
    login_url = reverse_lazy('accounts:login')
    template_name = 'profile_page.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workouts'] = CustomWorkoutModel.objects.filter(profile_id=self.request.user.id)
        return context


class ProfileConfView(LoginRequiredMixin, CreateView):
    model = Profile
    login_url = reverse_lazy('accounts:login')
    template_name = 'registration/profile_config.html'
    form_class = ProfileUpdateForm


    def form_valid(self, form):
        # Assign the currently logged-in user to the profile
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('accounts:profile-details', kwargs={'pk': self.object.pk})


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    login_url = reverse_lazy('accounts:login')
    template_name = 'registration/profile_update.html'
    form_class = ProfileUpdateForm

    def get_initial(self):
        initial_data = {
            'first_name': self.object.first_name,
            'last_name': self.object.last_name,
            'image': self.object.image.url,
            'gender': self.object.gender,
            'age': self.object.age,
            'height': self.object.height,
            'weight': self.object.weight,
            'goal': self.object.goal,
            'activity': self.object.activity,
            'calories_needed': self.object.calories_needed,
        }
        return initial_data



    def get_success_url(self):
        return reverse_lazy('accounts:profile-details', kwargs={'pk': self.object.pk})
