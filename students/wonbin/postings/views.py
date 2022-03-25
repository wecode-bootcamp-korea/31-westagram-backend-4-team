import json
from django.forms import ValidationError

from django.http import JsonResponse
from django.views import View

from .decorators import login_decorator
from .models import Post, Image, Comment
from .validator import url_validate

class PostingView(View):
    @login_decorator
    def post(self, request):
        try:
            data   = json.loads(request.body)
            text   = data["text"]
            images = data["images"].split(",")
            user   = request.user

            for image in images:
                url_validate(image)
            
            if len(images) > 10:
                return JsonResponse({"message": "images can't exceed 10."}, status = 400)

            post = Post.objects.create(
                user = user,
                text = text,
            )

            for image in images:
                Image.objects.create(
                    image_url = image,
                    post      = post
                )
            
            return JsonResponse({"message": "created"}, status = 201)
        
        except KeyError:
            return JsonResponse({"message": "None image"}, status = 400)
        except ValidationError:
            return JsonResponse({"message": "URL format error."}, status = 400)
    
    @login_decorator
    def get(self, request):
        user = request.user
        posts = Post.objects.filter(user = user)

        result = [{
            "1. user"  : user.name,
            "2. images": [{
                "이미지 주소": image.image_url
            } for image in post.images.all()],
            '3. text'      : post.text,
            "4. created_at": post.created_at
        } for post in posts]

        return JsonResponse({"result": result}, status=200)

class CommentView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        user = request.user
        post = data["postId"]
        text = data["text"]

        comment = Comment.objects.create(
            user = user,
            text = text,
            post = Post.objects.get(id = post)
        )
        
        return JsonResponse({"message": comment.id}, status=201)


