from django.db import models

# Create your models here.

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    
    def __str__(self):
        return f"(< name_class object: {self.name}\n {self.city}\n {self.state} >)"
    
class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojos, related_name="Ninjas", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"(< name_class object: {self.first_name} \n{self.last_name}\n {self.dojo}  >)"
    
