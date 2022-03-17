from django.db import models

# Create your models here.
class User(models.Model):
    name        = models.CharField(max_length=30)
    email       = models.EmailField(max_length=50)
    password    = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=20)

    class Meta:
        db_table = 'users'