from django.db import models

# Create your models here.


#TABLAS PARA NUESTRO PROYECTO

class registro(models.Model):
    idRegistro = models.AutoField(primary_key=True, verbose_name="id_registro")
    nombres = models.CharField(max_length=50, verbose_name="nombre_completo")
    apellidos = models.CharField(max_length=50, verbose_name="apellido_completo")
    usuario = models.CharField(max_length=60, verbose_name="nombre_usuario")
    correo = models.EmailField(max_length=100, verbose_name="correo")
    contraseña = models.CharField(max_length=50, verbose_name="contraseña")

    def __str__(self):
        return f'{self.idRegistro}, {self.nombres}'
        
class formulario(models.Model):
    rut = models.CharField(primary_key=True, verbose_name="run", max_length=12)
    nombreCompleto = models.CharField(max_length=100, verbose_name="name_completo")
    correo_electronico = models.EmailField(max_length=100, verbose_name="correo_e")
    numero = models.IntegerField(verbose_name="numero_telefonico")
    mensaje = models.TextField(verbose_name="mensaje_dejado", max_length=300)

    def __str__(self):
        return self.rut


class listadoTortas(models.Model):
    idtorta = models.AutoField(primary_key=True, verbose_name="id_torta")
    torta = models.CharField(max_length=50, verbose_name="nombre torta")
    tipotorta = models.CharField(max_length=50, verbose_name="tipo torta")
    tamanio = models.CharField(max_length=50, verbose_name="tamaño torta")
    stock = models.IntegerField( verbose_name="cantidad tortas")
    foto = models.ImageField(verbose_name="foto tortas", upload_to="core", default="static/core/img/sin_imagen.jpg")

    def __str__(self):
        return f'{self.idtorta}'



