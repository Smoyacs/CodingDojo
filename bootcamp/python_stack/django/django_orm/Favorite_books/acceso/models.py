from django.db import models

# Create your models here.
class Usuario(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=72)
    confirmar_password = models.CharField(max_length=72)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # books_uploaded = a list of books uploaded by a given user
    # liked_books = a list of books that a given user likes 

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"