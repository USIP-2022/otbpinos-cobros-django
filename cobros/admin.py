from django.contrib import admin
from .models import Propietario
from .models import Inmueble
from .models import Reunion
from .models import Asistencia
from .models import Gestion

class inmuebleAdmin(admin.ModelAdmin):
    list_display = ( "inmueble_nombre","inmueble_numero","propietario","tipo_inmueble")
class propietarioAdmin(admin.ModelAdmin):
    list_display = ( "nro_documento","paterno","materno","nombres","celular")


admin.site.register(Propietario,propietarioAdmin)
admin.site.register(Inmueble, inmuebleAdmin)
admin.site.register(Reunion)
admin.site.register(Asistencia)
admin.site.register(Gestion)