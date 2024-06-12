from django.db import models

# Create your models here.
class Usuario (models.Model):
    nombre=models.CharField(max_length=50,null=False)
    apellido=models.CharField(max_length=50,null=False)
    correo=models.EmailField(unique=True,null=False)
    contraseña=models.CharField(max_length=50,null=False)
    