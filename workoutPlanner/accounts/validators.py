from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class OnlyLettersValidator:
    def __init__(self, msg=None):
        self.msg = msg

        if self.msg is None:
            self.msg = 'This field must contain only letters.'

    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError(self.msg)