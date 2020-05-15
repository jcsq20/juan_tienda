from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    def get_full_name(self):
        return "%s %s" %(self.first_name, self.last_name)


#proxy model: es un modelo que hereda de otro
#obligatorioa
class Cliente(User):
    class Meta:
        proxy = True
    
    def get_productos(self):
        return []

#class Profile(models.Model):
 #   user = models.OneToOneField(User, on_delete=models.CASCADE)
  #  bio = models.TextField()
