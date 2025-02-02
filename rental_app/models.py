from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    # Relación one-to-one con el modelo User de Django
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    
    # Opciones para el campo 'tipo'
    TIPO_USUARIO = [
        ('operario', 'Operario'),
        ('cliente', 'Cliente'),
    ]
    tipo = models.CharField(max_length=12, choices=TIPO_USUARIO)
    
    def __str__(self):
        return f'{self.user} ({self.tipo})'

    

# Modelo de Categoría
class Categoria(models.Model):
    CATEGORIA = [
        ('ski', 'Ski'),
        ('botas', 'Botas'),
        ('trineo', 'Trineo'),
        ('snowboard', 'Snowboard'),
        ('otros', 'Otros'),
    ]
    nombre = models.CharField(max_length=255, choices=CATEGORIA)

    def __str__(self):
        return self.nombre

# Modelo de Equipo
class Equipo(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    imagen = models.URLField(max_length=200)
    precio = models.IntegerField(default=0)
    # Opciones para el campo 'estado'
    ESTADO = [
        ('disponible', 'Disponible'),
        ('arrendado', 'Arrendado'),
        ('mantencion', 'Mantencion'),
    ]
    estado = models.CharField(max_length=45, choices=ESTADO)

    def __str__(self):
        return f'{self.nombre} ({self.estado})'

# Modelo de Arriendo
class Arriendo(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    equipo = models.ForeignKey(Equipo, on_delete=models.DO_NOTHING)
    fecha = models.DateTimeField()
    observacion = models.TextField(blank=True, null=True)
    danado = models.BooleanField(default=False)

    def __str__(self):
        return f'Arriendo de {self.equipo.nombre} por {self.user.user.username} el {self.fecha}'
