from django.db import models
from acceso.models import Usuario

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    
    uploaded_by = models.ForeignKey(Usuario, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(Usuario, related_name="liked_books")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)