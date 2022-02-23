from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"(< Users object: {self.first_name} {self.last_name} {self.email_address} {self.age} {self.created_at} {self.updated_at} >)"