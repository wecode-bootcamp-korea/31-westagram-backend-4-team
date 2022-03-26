import json
from django.forms import ValidationError

from django.http import JsonResponse
from django.views import View

from .decorators import login_decorator
from .models import Post, Image, Comment, Like
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
            
            return JsonResponse({"created": post.id}, status = 201)
        
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
            "3. text"      : post.text,
            "4. liked"     : len([like for like in post.likes.filter(post = post)]),
            "5. created_at": post.created_at
        } for post in posts]

        return JsonResponse({"result": result}, status=200)

class CommentView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        user = request.user
        post = data["postID"]
        text = data["text"]

        comment = Comment.objects.create(
            user = user,
            text = text,
            post = Post.objects.get(id = post)
        )

        return JsonResponse({"created": comment.id}, status=201)
    
    @login_decorator
    def get(self, request):
        data =  json.loads(request.body)
        post = Post.objects.get(id = data["postID"])

        result = [{
            "1. 작성자" :  comment.user.name,
            "2. 내용"  : comment.text
        } for comment in post.comments.all()]

        return JsonResponse({"comment": result}, status=200)

class LikesView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        post = Post.objects.get(id = data["postID"])
        user = request.user
        like = Like.objects.filter(user = user, post = post)


        if not like.exists(): 
            Like.objects.create(
                user = user,
                post = post
            )
            return JsonResponse({"message" : "liked"}, status = 201)
        
        else: like.delete()
        return JsonResponse({"message" : "unliked"}, status = 201)


        
        
        




        
    



        


