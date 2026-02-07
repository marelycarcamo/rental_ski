import django.db.models
import django.contrib.auth.models

class Usuario(django.db.models.Model):
    # Relación one-to-one con el modelo User de Django
    user = django.db.models.OneToOneField(django.contrib.auth.models.User, on_delete=django.db.models.DO_NOTHING)
    created = django.db.models.DateTimeField(auto_now_add=True)
    
    # Opciones para el campo 'tipo'
    TIPO_USUARIO = [
        ('operario', 'Operario'),
        ('cliente', 'Cliente'),
    ]
    tipo = django.db.models.CharField(max_length=12, choices=TIPO_USUARIO)
    
    def __str__(self):
        return f'{self.user} ({self.tipo})'

# Modelo de Categoría
class Categoria(django.db.models.Model):
    CATEGORIA = [
        ('ski', 'Ski'),
        ('botas', 'Botas'),
        ('trineo', 'Trineo'),
        ('snowboard', 'Snowboard'),
        ('otros', 'Otros'),
    ]
    nombre = django.db.models.CharField(max_length=255, choices=CATEGORIA)

    def __str__(self):
        return self.nombre

# Modelo de Equipo
class Equipo(django.db.models.Model):
    nombre = django.db.models.CharField(max_length=255)
    categoria = django.db.models.ForeignKey(Categoria, on_delete=django.db.models.DO_NOTHING)
    imagen = django.db.models.URLField(max_length=200)
    precio = django.db.models.IntegerField(default=0)
    # Opciones para el campo 'estado'
    ESTADO = [
        ('disponible', 'Disponible'),
        ('arrendado', 'Arrendado'),
        ('mantencion', 'Mantencion'),
    ]
    estado = django.db.models.CharField(max_length=45, choices=ESTADO)

    def __str__(self):
        return f'{self.nombre} ({self.estado})'

# Modelo de Arriendo
class Arriendo(django.db.models.Model):
    user = django.db.models.ForeignKey(Usuario, on_delete=django.db.models.DO_NOTHING)
    equipo = django.db.models.ForeignKey(Equipo, on_delete=django.db.models.DO_NOTHING)
    fecha = django.db.models.DateTimeField()
    observacion = django.db.models.TextField(blank=True, null=True, default='Sin observaciones')
    danado = django.db.models.BooleanField(default=False)
    

    def __str__(self):
        return f'Arriendo de {self.equipo.nombre} por {self.user.user.username} el {self.fecha}'
