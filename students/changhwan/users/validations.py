import re

from django.core.exceptions import ValidationError

class Validation:
    def validate_email(self, email):
        regex_email = '^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'

        if not re.match(regex_email, email):
            raise ValidationError('message : Incorrect Email format')

    def validate_password(self, password):
        regex_password = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$'

        if not re.match(regex_password, password):
            raise ValidationError('message : Incorrect Password format')