from django.db import models

# Create your models here.
class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Inscrito(models.Model):
    ESTADO_CHOICES = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No asisten'),
    ]
    id_persona = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    fecha_inscripcion = models.DateField()
    institucion = models.CharField(max_length=100)
    hora_inscripcion = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    observacion = models.TextField(max_length=100)