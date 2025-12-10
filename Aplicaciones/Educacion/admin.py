from django.contrib import admin
from .models import Carrera  # Importar el modelo creado 

# Register your models here.
admin.site.register(Carrera)   #colocar esta linea para que aparezca las opciones de carrera en el panel de adm.