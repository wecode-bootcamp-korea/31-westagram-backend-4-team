import re
import json
from django.db import IntegrityError
from django.http import JsonResponse
from django.views import View
from .models import User

class SignupView(View):
    def post(self, request):
        try:
            data                 = json.loads(request.body)
            email_compile        = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            password_compile     = re.compile('^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$')
            phone_number_compile = re.compile('\d{3}-\d{3,4}-\d{4}')
    
            if email_compile.match(data["email"]) != None:
                email = data["email"]
            else: 
                return JsonResponse({"message": "이메일 형식이 아닙니다."}, status=401)
            
            if password_compile.match(data["password"]) != None:
                password = data["password"]
            else:
                return JsonResponse({"message": "비밀번호 양식을 지켜주세요."}, status=401)

            if phone_number_compile.match(data["phone_number"]) != None:
                phone_number = data["phone_number"]
            else:
                return JsonResponse({"message": "전화번호 양식을 지켜주세요."}, status=401)
        
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