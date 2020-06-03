from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .genero import Generos


# Create your models here.
#crear estrucuta base de datos

class Roles(models.Model):

    RoleName = models.CharField(max_length = 50, verbose_name="Nombre del rol")
 
    class Meta:
        verbose_name ="Perfil de Usuario"
        verbose_name = "Perfiles"

    def __str__(self):
        return self.RoleName
    
class DatosUser(models.Model):
    userDNI = models.CharField(max_length = 25,verbose_name='Identificación')
    nombUser = models.CharField(max_length = 236,verbose_name='Nombres', null = True)
    apelUser = models.CharField(max_length = 236,verbose_name='Apellido', null = True)
    
    fotoUser = models.ImageField(default='user.png',verbose_name='Foto de perfil', upload_to="perfiles/img")
    teleUser = models.CharField(max_length = 255,verbose_name='Teléfono')
    geneUser =models.CharField(max_length = 20, choices = Generos, default = "Otro",verbose_name='Genero')
    adddata = models.DateTimeField(auto_now_add = True, auto_now = False, null = True,  verbose_name ='Fue creado el')
    modifiat = models.DateTimeField(auto_now = True,null = True, verbose_name = 'Genero modificado')

    class Meta:
        verbose_name = "Datos de Usuario"
        verbose_name_plural = "Información"


    def __str__(self):
        return self.userDNI

class habilidades(models.Model):
    nombHabil = models.CharField(max_length = 22)
    DescHabil = models.TextField(max_length = 2000, verbose_name="Descripción de la habilidad")
    
    class Meta:
        verbose_name = "Habilidades del Usuario"
        verbose_name_plural = "Competencias"

    

    def __str__(self):
        return self.nombHabil

class DetaRoles(models.Model):
    idRoles = models.ForeignKey(Roles, on_delete = models.CASCADE, verbose_name = "Identificador de rol")
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name ="Identificación del usuario")
    addUser = models.DateTimeField(auto_now_add = True, auto_now = False)
    udtuser = models.DateTimeField(auto_now = True)
    estadoRol = models.CharField(max_length = 19,verbose_name="Estado del rol")

    class Meta:
        verbose_name = "Roles de Usuario"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.idUser



class rates(models.Model):
    idHabil = models.ForeignKey(habilidades, on_delete = models.CASCADE, verbose_name="Identificador de habilidad")
    iduser = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name="Identificador de usuario")
    Porcentaje = models.DecimalField(max_digits = 2, decimal_places =1)
    udtHabil = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "Calaficacion del usuario"
        verbose_name_plural = "Calificaciones"

    def __str__(self):
        return self.Porcentaje
'''
class documents(models.Model):
    nombDocu = models.CharField(max_length = 255)
    pathDocu = models.CharField(max_length = 255)

    def __str__(self):
        return self.nombDocu
        return self.pathDocu

class proyects(models.Model):
    nombProyec = models.CharField(max_length = 255)
    descProyec = models.CharField(max_length = 255)
    imgProyec = models.CharField(max_length = 255)
    #faltan las de fecha
    urlRepo = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombProyec
        return self.descProyec
        return self.imgProyec
        return self.urlRepo

class tipoDocu(models.Model):
    nombTipoDoc = models.CharField(max_length = 255)

    def __str__(self):
        return self.nombTipoDoc

class categProye(models.Model):
    lenguaje = models.CharField(max_length = 255)
    motorDB = models.CharField(max_length = 255)
    arquitectura = models.CharField(max_length = 255)

    def __str__(self):
        return self.lenguaje
        return self.motorDB
        return self.arquitectura
        
'''




