import json
import re

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from users.models           import User
from users.validations      import validate_email, validate_password

class SignUpView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']

            validate_email(email)
            validate_password(password)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message':'Your email is already exists'}, status=400)

            User.objects.create(
                name         = name,
                email        = email,
                password     = password,
                phone_number = phone_number
            )

            return JsonResponse({'message':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message':'KeyError'}, status=400)

        except ValidationError as e:
            return JsonResponse({'message':(e.message)}, status=400)

class SignInView(View):
    def post(self, request):
        try:
            data           = json.loads(request.body)
            email          = data['email']
            password       = data['password']

            email_exist    = User.objects.filter(email=email).exists()
            password_exist = User.objects.filter(password=password).exists()

            if not email_exist:
                return JsonResponse({"message":"INVALID_USER"}, status=401)

            if not password_exist:
                return JsonResponse({"message":"INVALID_PASSWORD"}, status=401)

            return JsonResponse({'message':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message':'KeyError'}, status=400) 