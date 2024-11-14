

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


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

