from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AlphaNumericValidator:
    def __init__(self, msg=None):
        self.msg = msg
        if self.msg is None:
            self.msg = 'This field can contain only letters and numbers.'

    def __call__(self, value):
        if not value.isalnum():
            raise ValidationError(self.msg)