import json, bcrypt, jwt

from django.db    import IntegrityError
from django.http  import JsonResponse
from django.views import View
from django.conf  import settings

from .models    import User
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

            hashed_password =  bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

            User.objects.create(
                name         = data["name"],
                email        = email,
                password     = hashed_password,
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

            user = User.objects.get(email = email)

            if not bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
                return JsonResponse({"message": "INVALID_USER"}, status = 401)
            
            access_token = jwt.encode({"id": user.id}, settings.SECRET_KEY, algorithm = settings.ALGORITHM)
            return JsonResponse({"token": access_token}, status = 200)
                
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status = 401)
