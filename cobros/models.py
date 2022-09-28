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


class Propietarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    avatar = models.TextField()
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


class Inmuebles(models.Model):
    id = models.BigAutoField(primary_key=True)
    propietario = models.ForeignKey(Propietarios, on_delete=models.CASCADE)
    inmueble_numero = models.IntegerField()
    inmueble_nombre = models.CharField(max_length=200)
    lote_superficie = models.DecimalField(decimal_places=2, max_digits=10)
    tipo_inmueble = models.CharField(max_length=1, choices=TipoInmueble.choices, default=TipoInmueble.lote)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)
    fecha_ingreso = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.inmueble_nombre


class Reuniones(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_reunion = models.DateTimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)
    user_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fecha_reunion

class Asistencias(models.Model):
    id = models.BigAutoField(primary_key=True)
    inmueble = models.ForeignKey(Inmuebles, on_delete=models.CASCADE)
    reunion = models.ForeignKey(Reuniones, on_delete=models.CASCADE)
    tipo_asistencia = models.CharField(max_length=1, choices=TipoAsistencia.choices, default=TipoAsistencia.presente)
    motivo_permiso = models.TextField()
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)
    user_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class Gestiones(models.Model):
    id = models.BigAutoField(primary_key=True)
    gestion = models.IntegerField()
    descripcion = models.TextField()
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.activo)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.gestion
