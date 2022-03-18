import json
import re
# from django.shortcuts import render

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from users.models           import User
from users.validations      import Validation

# Create your views here.
class SignUpView(View, Validation):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']

            validation = Validation()

            validation.validate_email(email)
            validation.validate_password(password)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message':'Your email already exists'}, status=400)

            user = User.objects.create(
                name         = name,
                email        = email,
                password     = password,
                phone_number = phone_number
            )

            return JsonResponse({'message':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'error':'KeyError'}, status=400)

        except ValidationError as e:
            return JsonResponse({'message':(e.message)}, status=400)