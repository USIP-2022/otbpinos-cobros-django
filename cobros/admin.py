from django.contrib import admin
from .models import Propietario
from .models import Inmueble
from .models import Reunion
from .models import Asistencia
from .models import Gestion


class inmuebleAdmin(admin.ModelAdmin):
    list_display = ("inmueble_nombre", "inmueble_numero", "propietario", "tipo_inmueble")


class propietarioAdmin(admin.ModelAdmin):
    list_display = ("nro_documento", "paterno", "materno", "nombres", "celular")


class gestionAdmin(admin.ModelAdmin):
    list_display = ("gestion", "estado")


class reunionAdmin(admin.ModelAdmin):
    list_display = ("fecha_reunion", "motivo", "estado")

class asistenciaAdmin(admin.ModelAdmin):
    list_display = ("inmueble", "reunion", "tipo_asistencia")


admin.site.register(Propietario, propietarioAdmin)
admin.site.register(Inmueble, inmuebleAdmin)
admin.site.register(Gestion, gestionAdmin)
admin.site.register(Reunion, reunionAdmin)
admin.site.register(Asistencia,asistenciaAdmin)
