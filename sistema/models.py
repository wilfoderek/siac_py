
# coding=utf-8

from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class TipoIdentificacion(models.Model):
    """
    Representa tipos de identificación (CI - Pasaporte)
    """
    nombre_identificacion = models.CharField(max_length=100)


class Genero(models.Model):
    """
    Representa el género de una persona: Masculino, Femenino, etc
    """
    nombre = models.CharField(max_length=100)


class TipoSangre(models.Model):
    """
    Representa los diversos tipos de sangre existentes
    """
    nombre = models.CharField(max_length=100)


class EstadoCivil(models.Model):
    """
    Representa los diferentes estados civiles existentes
    """
    nombre = models.CharField(max_length=100)


class TipoEtnia(models.Model):
    """
    Representa las deniminaciones de etnias
    """
    nombre = models.CharField(max_length=100)


class Pais(models.Model):
    """
    Guarda los paises
    """
    nombre = models.CharField(max_length=100)


class Zonal(models.Model):
    """
    Representa la zonificación que tiene el país de acuerdo
    al ordenamietno territorial de la República del Ecuador
    """
    nombre = models.CharField(max_length=100)


class Provincia(models.Model):
    """
    Provincias principalmente de Ecuador y se relaciona con la zonal
    """
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais)
    zonal = models.ForeignKey(Zonal)


class Canton(models.Model):
    """
    Representa los cantones de las provincias del ecuador
    """
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia)


class Ciudad(models.Model):
    """
    Representa las ciudades del mundo
    """
    canton = models.ForeignKey(Canton)
    nombre = models.CharField(max_length=200)


class Parroquia(models.Model):
    """
    Parroquias pertenecientes a las ciudades del Ecuador
    """
    nombre = models.CharField(max_length=300)
    ciudad = models.ForeignKey(Ciudad)


class Parentesco(models.Model):
    """
    Representa los diferentes tipos de parentesco que un familiar
    o persona tiene con alguien registrado en el sistema
    """
    nombre = models.CharField(max_length=100)


class CategoriaInstitucion(models.Model):
    """
    Catergorías de institusiones y empresas
    Ejemplo: Banco, Universidad
    """
    nombre = models.CharField(max_length=100)


class TipoInstitucion(models.Model):
    """
    Tipos de empresas: Publicas, Privadas...
    """
    nombre = models.CharField(max_length=299)


class Institucion(models.Model):
    """
    Representa los datos de las institusiones o empresas registradas en el sistema
    @nombre guarda el nombre de una persona
    """
    nombre = models.CharField(max_length=200)
    representante = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telf1 = models.CharField(max_length=20)
    telf2 = models.CharField(max_length=20)
    direccion = models.CharField(max_length=300)
    ciudad = models.ForeignKey(Ciudad)
    categoria_empresa = models.ForeignKey(CategoriaInstitucion)
    tipo_institucion = models.ForeignKey(TipoInstitucion, null=True, blank=True)


class NivelInstruccion(models.Model):
    """
    Niveles de instruccion educativa que puede tener una persona
    Ejemplo:Primaria, Secundaria
    """
    nombre = models.CharField(max_length=200)


class TituloProfesional(models.Model):
    """
    Representa el listado de los títulos profesionales de una persona
    """
    nombre = models.CharField(max_length=300)


class Cargo(models.Model):
    """
    Cargos profesionales de personas
    """
    nombre = models.CharField(max_length=300)


class Persona(models.Model):
    """
    Representa los datos personales de una persona
    """
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.TextField(null=True, blank=True)
    telefono = models.CharField(max_length=20)
    telefono_domicilio = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_registro = models.DateField(auto_now=True)

    #número de la casa.
    numero_domicilio = models.CharField(max_length=50)

    #ruc , cedula lo que sea
    numero_identificacion = models.CharField(max_length=20)

    #Boolean
    discapacidad = models.BooleanField()

    carne_conadis = models.CharField(max_length=50)
    porcentaje_discapacidad = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    #nobre de la persona que se contactará
    contacto_emergencia = models.CharField(max_length=200)

    telefono_emergencia = models.CharField(max_length=20)
    celular_emergencia = models.CharField(max_length=20)
    email_emergencia = models.CharField(max_length=200)

    #código de acceso de la tarjeta de ingreso
    codigo_acceso = models.CharField(max_length=200)

    foto = models.CharField(max_length=300)

    #"estado de la persona: A:Activo , I:Inactivo ,etc "
    estado = models.CharField(max_length=2)

    usuario = models.ForeignKey(User, unique=True)

    #especifíca si es cédula , pasaporte...
    tipo_identidad = models.ForeignKey(TipoIdentificacion)

    #con la ciudad se tiene la provincia , país.
    ciudad_nacimiento = models.ForeignKey(Ciudad, related_name='ciudad_nacimiento')

    #ciudad de donde reside la persona actualmente
    ciudad_residencia = models.ForeignKey(Ciudad, related_name='ciudad_residencia')

    #nacionalidad de la personas
    pais_nacimiento = models.CharField(max_length=100)
    estado_civil = models.ForeignKey(EstadoCivil)
    tipo_sangre = models.ForeignKey(TipoSangre)

    #genero de las personas
    genero = models.ForeignKey(Genero)

    # etnia de la persona
    etnia = models.ForeignKey(TipoEtnia)


class Subgrupo(models.Model):
    """
    Representan los diferentes Grupos Funcionarios de la institución
    Ejemplo: Directores, Docentes, Contador ...
    """
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    #Activa o desactiva un Subgrupo
    estado = models.BooleanField()
    grupo = models.ForeignKey(Group)


class Menu(models.Model):
    """
    Modelo que contiene el listado gerárquico de menús
    Ejemplo: Archivo->
                Abrir
                Guardar
                Recientes->
                    uno.txt
                    dos.txt
            Salir
    """
    nombre = models.CharField(max_length=100)
    orden = models.SmallIntegerField()
    padre = models.SmallIntegerField()
    url = models.TextField()
    icono = models.TextField()

    #Valor para menu activo o inactivo
    estado = models.BooleanField()

    descripcion = models.TextField()


class SubgrupoMenu(models.Model):
    """
    Establece una relacion muchos a muchos entre los modelos
    Subgrupo y Menu, almacena el listado de opciones de menu para
    cada Subgrupo con los permisos (CRUD) pertinentes
    """
    crear = models.BooleanField()
    leer = models.BooleanField()
    actualizar = models.BooleanField()
    borrar = models.BooleanField()
    acceso_directo = models.BooleanField()

    #Valor para menu de un subgrupo activo o inactivo
    estado = models.BooleanField()

    menu = models.ForeignKey(Menu)
    subgrupo = models.ForeignKey(Subgrupo)
