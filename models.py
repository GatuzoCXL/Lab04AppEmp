from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    
class Entrada(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    fecha_creacion = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
# Create your models here.
