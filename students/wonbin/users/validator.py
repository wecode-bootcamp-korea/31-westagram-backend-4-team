import re

from django.forms import ValidationError


REGEX_EMAIL        = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
REGEX_PASSWORD     = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
REGEX_PHONE_NUMBER = '\d{3}-\d{3,4}-\d{4}'

def email_validate(email):
    if not re.match(REGEX_EMAIL, email):
                raise ValidationError("Email format error.")

def password_validate(password):
    if not re.match(REGEX_PASSWORD, password):
                raise ValidationError("Password format error.")

def phone_number_validate(phone_number):
    if not re.match(REGEX_PHONE_NUMBER, phone_number):
                raise ValidationError("Phone number format error.")
