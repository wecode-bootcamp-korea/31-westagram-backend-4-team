from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=20)
    email        = models.EmailField(max_length=245)
    password     = models.CharField(max_length=100)
    phone_number = models.IntegerField()

    class Meta: 
        db_table = "users"
  
    

