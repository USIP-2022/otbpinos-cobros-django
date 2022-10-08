from django.contrib import admin
from .models import Propietario
from .models import Inmueble
from .models import Reunion
from .models import Asistencia
from .models import Gestion

from .models import Multa
from .models import PagoMulta
from .models import Aporte
from .models import InmuebleAporte
from .models import PagoInmuebleAporte
from .models import Pago
from .models import Desembolsos
from .models import Generico


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

class multaAdmin(admin.ModelAdmin):
    list_display = ("inmueble_id", "descripcion", "monto", "estado")

class pagoMultaAdmin(admin.ModelAdmin):
    list_display = ("multa_id", "monto_pagado", "estado")
class aporteAdmin(admin.ModelAdmin):
    list_display = ("monto", "descripcion", "fecha_inicio")
class inmuebleAporteAdmin(admin.ModelAdmin):
    list_display = ("inmueble_id", "estado")
class pagoInmuebleAporteAdmin(admin.ModelAdmin):
    list_display = ("inmueble_aporte_id", "monto_pagado", "estado")
class pagoAdmin(admin.ModelAdmin):
    list_display = ("inmueble_id", "monto", "reunion_id", "estado")
class desembolsoAdmin(admin.ModelAdmin):
    list_display = ("motivo", "monto", "numero_boleta", "estado")
class genericoAdmin(admin.ModelAdmin):
    list_display = ("propiedad", "descripcion", "valor", "data", "estado")


admin.site.register(Propietario, propietarioAdmin)
admin.site.register(Inmueble, inmuebleAdmin)
admin.site.register(Gestion, gestionAdmin)
admin.site.register(Reunion, reunionAdmin)
admin.site.register(Asistencia,asistenciaAdmin)

admin.site.register(Multa,multaAdmin)
admin.site.register(PagoMulta,pagoMultaAdmin)
admin.site.register(Aporte,aporteAdmin)
admin.site.register(InmuebleAporte,inmuebleAporteAdmin)
admin.site.register(PagoInmuebleAporte,pagoInmuebleAporteAdmin)
admin.site.register(Pago,pagoAdmin)
admin.site.register(Desembolsos,desembolsoAdmin)
admin.site.register(Generico,genericoAdmin)
