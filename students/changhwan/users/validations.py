import re

from django.core.exceptions import ValidationError

class Validation:
    def validate_email(self, value):
        email_regex = re.compile('^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$')

        if not email_regex.match(value):
            raise ValidationError('message : Incorrect Email format')

    def validate_password(self, value):
        password_regex = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$')

        if not password_regex.match(value):
            raise ValidationError('message : Incorrect Password format')