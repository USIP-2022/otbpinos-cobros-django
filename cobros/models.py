from django.db import models
from django.conf import settings


# Create your models here.

class Estado(models.TextChoices):
    activo = 'a', 'Activo'
    inactivo = 'i', 'Inactivo'

class TipoAsistencia(models.TextChoices):
    presente = 'p', 'Presente'
    falta = 'f', 'Falta'
    justificacion = 'j', 'Justificacion'


class Expedido(models.TextChoices):
    cochabamba = 'CB', 'Cochabamba'
    la_paz = 'LP', 'La paz'


class Genero(models.TextChoices):
    masculino = 'MASCULINO', 'Masculino'
    femenino = 'FEMENINO', 'Femenino'


class TipoInmueble(models.TextChoices):
    lote = 'LOTE', 'Lote'
    casa = 'CASA', 'Casa'


class Propietario(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    avatar = models.TextField(blank=True, null=True)
    nombres = models.CharField(max_length=200)
    paterno = models.CharField(max_length=200)
    materno = models.CharField(max_length=200)
    nro_documento = models.IntegerField()
    expedido = models.CharField(max_length=2, choices=Expedido.choices)
    genero = models.CharField(max_length=200, choices=Genero.choices)
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10)
    domicilio = models.TextField()
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.paterno + " " + self.materno + " " + self.nombres


class Inmueble(models.Model):
    id = models.BigAutoField(primary_key=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    inmueble_numero = models.IntegerField()
    inmueble_nombre = models.CharField(max_length=200)
    lote_superficie = models.DecimalField(decimal_places=2, max_digits=10)
    tipo_inmueble = models.CharField(max_length=20, choices=TipoInmueble.choices, default=TipoInmueble.lote)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)
    fecha_ingreso = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.inmueble_nombre


class Reunion(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_reunion = models.DateTimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)
    user_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.motivo)

class Asistencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    reunion = models.ForeignKey(Reunion, on_delete=models.CASCADE)
    tipo_asistencia = models.CharField(max_length=1, choices=TipoAsistencia.choices, default=TipoAsistencia.presente)
    motivo_permiso = models.TextField()
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)
    user_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.inmueble.inmueble_nombre


class Gestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    gestion = models.IntegerField()
    descripcion = models.TextField()
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.gestion
class Multa(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    inmueble_id = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300)
    monto = models.DecimalField(decimal_places=2, max_digits=10)
    tipo_multa = models.CharField(max_length=200)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)
    asistencia_id = models.ForeignKey(Asistencia, on_delete=models.CASCADE)
    estado_aporte = models.CharField(max_length=200)

    def __int__(self):
        return self.id

class PagoMulta(models.Model):
    id = models.BigAutoField(primary_key=True)
    multa_id = models.IntegerField()
    monto_pagado = models.DecimalField(decimal_places=2, max_digits=10)
    pago_id = models.ForeignKey(Multa, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)

    def __int__(self):
        return self.id

class Aporte(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    monto = models.DecimalField(decimal_places=2, max_digits=10)
    descripcion = models.CharField(max_length=300)
    fecha_inicio = models.DateField()
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)

    def __int__(self):
        return self.id

class InmuebleAporte(models.Model):
    id = models.BigAutoField(primary_key=True)
    inmueble_id = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    estado_aporte = models.CharField(max_length=100)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)

    def __int__(self):
        return self.id


class Pago(models.Model):
    id = models.BigAutoField(primary_key=True)
    inmueble_id = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    monto  = models.DecimalField(decimal_places=2, max_digits=10)
    reunion = models.ForeignKey(Reunion, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)

    def __int__(self):
        return self.id
class PagoInmuebleAporte(models.Model):
    id = models.BigAutoField(primary_key=True)
    inmueble_aporte_id = models.ForeignKey(InmuebleAporte, on_delete=models.CASCADE)
    monto_pagado = models.DecimalField(decimal_places=2, max_digits=10)
    pago_id =models.ForeignKey(Pago, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)

    def __int__(self):
        return self.id
class Desembolsos(models.Model):
    id = models.BigAutoField(primary_key=True)
    motivo = models.CharField(max_length=300)
    monto  = models.DecimalField(decimal_places=2, max_digits=10)
    numero_boleta  = models.IntegerField()
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)

    def __int__(self):
        return self.id

class Generico(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    propiedad = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    valor = models.IntegerField()
    data = models.CharField(max_length=300)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)

    def __int__(self):
        return self.id