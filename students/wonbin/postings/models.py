from django.db import models

from  users.models import User


class Post(models.Model):
    user =  models.ForeignKey(User, on_delete=(models.CASCADE), related_name= "posts")
    text =  models.TextField(null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table =  "posts"

class Image(models.Model):
    image_url = models.URLField(max_length=2000)
    post      = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")

    class Meta:
        db_table = "images"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comments"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "likes"