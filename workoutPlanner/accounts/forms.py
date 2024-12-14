from cProfile import label

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, BaseUserCreationForm
from django.utils.translation import gettext_lazy as _


from workoutPlanner.accounts.models import Profile

UserModel = get_user_model()

class LoginForm(AuthenticationForm):
    username = UsernameField(
        label='',
        widget=forms.TextInput(attrs={
            "autofocus": True,
            'placeholder': 'Username',
        }),
    )
    password = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'placeholder': 'Password',
        }),
    )
    error_messages = {
        "invalid_login": _(
            'Incorrect username or password!'
        ),
        "inactive": _("This account is inactive."),
                    }



class AccountCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Password',
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Confirm Password',
            }),
        }
        labels = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Password',
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
        })

        for field_name, field in self.fields.items():
            field.help_text = ''
            field.label = ''

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        labels = {
            'image': 'Profile picture',
            'goal': 'Your goal',
            'activity': 'Activity',
            'calories_needed': 'Daily calorie need'
        }
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'profile-conf-image-input'
            }),
            'age': forms.NumberInput(attrs={
                'class': "profile-conf-age-field",
            }),
            'goal': forms.Select(attrs={
                'class': 'profile-conf-goal-input',
            },),
            'activity': forms.Select(attrs={
                'class': 'profile-conf-activity-input'
            }),
            'calories_needed': forms.NumberInput(attrs={
                'disabled': 'True'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.weight and self.instance.height:
            # Prepopulate the field if instance data exists
            self.fields['calories_needed'].initial = (
                    10 * self.instance.weight + 6.25 * self.instance.height - 5 * 25
            )
            self.fields['calories_needed'].widget.attrs['disabled'] = True

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.calories_needed = 10 * instance.weight + 6.25 * instance.height - 5 * 25

        if commit:
            instance.save()
        return instance