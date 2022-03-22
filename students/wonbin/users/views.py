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
            return JsonResponse({"message":"This email already exists.."}, status=400)

class SigninView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data["email"]
            password = data["password"]

            email_validate(email)
            password_validate(password)
             
            if User.objects.get(email = email).password != password:
                return JsonResponse({"message": "INVALID_USER"}, status = 401)
                
            return JsonResponse({"message": "success"}, status = 200)
                
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status = 401)