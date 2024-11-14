

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import TextChoices
from django.forms import ChoiceField
from django.utils.translation import gettext_lazy as _

from accounts import choices


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    def get_short_name(self):
        return self.first_name


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
    )
    gender = models.CharField(
        max_length=2,
        choices=choices.GenderChoices,
    )
    age = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(10),
            MaxValueValidator(100),
        ],
        error_messages={
            'min_value': _('You must be at least 10 years old.'),
            'max_value': _('You must be at most 100 years old.'),
        },
    )
    height = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(250)
        ],
        error_messages='Please provide correct height.',
    )
    goal = models.CharField(
        max_length=2,
        choices=choices.GoalChoices,
    )
    activity = models.CharField(
        max_length=2,
        choices=choices.ActivityChoices,
    )
    daily_calories_need = models.PositiveSmallIntegerField()



