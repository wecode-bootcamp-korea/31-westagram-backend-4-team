import re

from django.core.exceptions import ValidationError

from users.models           import User

def validate_email(email):
    regex_email    = '^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'

    if not re.match(regex_email, email):
        raise ValidationError('INVALID_EMAIL')

def validate_password(password):
    regex_password = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$'

    if not re.match(regex_password, password):
        raise ValidationError('INVALID_PASSWORD')