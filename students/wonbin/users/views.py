import json

from django.db import IntegrityError
from django.http import JsonResponse
from django.views import View

from .models import User
from .validator import email_validate, password_validate, phone_number_validate

class SignupView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            email        = data["email"]
            password     = data["password"]
            phone_number = data["phone_number"]
    
            email_validate(email)
            password_validate(password)
            phone_number_validate(phone_number)

            User.objects.create(
                name         = data["name"],
                email        = email,
                password     = password,
                phone_number = phone_number
            )
            
            return JsonResponse({"message":"SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        except IntegrityError:
            return JsonResponse({"message":"중복된 이메일입니다."}, status=400)