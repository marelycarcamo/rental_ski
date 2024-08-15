from django.contrib import admin

# Register your models here.
from .models import Usuario
admin.site.register(Usuario)

from .models import Equipo
admin.site.register(Equipo)

from .models import Categoria
admin.site.register(Categoria)

from .models import Arriendo
admin.site.register(Arriendo)


