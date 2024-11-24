from django import forms
from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import request

from workoutPlanner.accounts.models import Profile

UserModel = get_user_model()

class AccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email',)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

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