from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=100)
    email        = models.EmailField(max_length=245, unique=True)
    password     = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now_add=True)

    class Meta: 
        db_table = "users"