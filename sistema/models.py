# coding=utf-8
from django.db import models
from django.contrib.auth.models import User

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
    nombre_genero = models.CharField(max_length=100)


class TipoSangre(models.Model):
    """
    Representa los diversos tipos de sangre existentes
    """
    nombre_tipo_sangre = models.CharField(max_length=100)


class EstadoCivil(models.Model):
    """
    Representa los diferentes estados civiles existentes
    """
    nombre_estado_civil = models.CharField(max_length=100)


class TipoEtnia(models.Model):
    """
    Representa las deniminaciones de etnias
    """
    nombre_etnia = models.CharField(max_length=100)


class Pais(models.Model):
    """
    Guarda los paises
    """
    nombre_pais = models.CharField(max_length=100)


class Zonal(models.Model):
    """
    Representa la zonificación que tiene el país de acuerdo
    al ordenamietno territorial de la República del Ecuador
    """
    nombre_zonal = models.CharField(max_length=100)


class Provincia(models.Model):
    """
    Provincias principalmente de Ecuador y se relaciona con la zonal
    """
    nombre_provincia = models.CharField(max_length=100)
    id_pais = models.ForeignKey(Pais)
    id_zonal = models.ForeignKey(Zonal)


class Canton(models.Model):
    """
    Representa los cantones de las provincias del ecuador
    """
    nombre_canton = models.CharField(max_length=100)
    id_provincia = models.ForeignKey(Provincia)


class Ciudad(models.Model):
    """
    Representa las ciudades del mundo
    """
    id_canton = models.ForeignKey(Canton)
    nombre_ciudad = models.CharField(max_length=200)


class Parroquia(models.Model):
    """
    Parroquias pertenecientes a las ciudades del Ecuador
    """
    nombre_parroquia = models.CharField(max_length=300)
    id_ciudad = models.ForeignKey(Ciudad)


class Parentesco(models.Model):
    """
    Representa los diferentes tipos de parentesco que un familiar
    o persona tiene con alguien registrado en el sistema
    """
    nombre_parentesco = models.CharField(max_length=100)


class CategoriaInstitucion(models.Model):
    """
    Catergorías de institusiones y empresas
    Ejemplo: Banco, Universidad
    """
    nombre_categoria = models.CharField(max_length=100)


class TipoInstitucion(models.Model):
    """
    Tipos de empresas: Publicas, Privadas...
    """
    nombre_tipo = models.CharField(max_length=299)


class Institucion(models.Model):
    """
    Representa los datos de las institusiones o empresas registradas en el sistema
    @nombre guarda el nombre de una persona
    """
    nombre_institusion = models.CharField(max_length=200)
    representante = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telf1 = models.CharField(max_length=20)
    telf2 = models.CharField(max_length=20)
    direccion = models.CharField(max_length=300)
    id_ciudad = models.ForeignKey(Ciudad)
    categoria_empresa = models.ForeignKey(CategoriaInstitucion)
    tipo_institucion = models.ForeignKey(TipoInstitucion, null=True, blank=True)


class NivelInstruccion(models.Model):
    """
    Niveles de instruccion educativa que puede tener una persona
    Ejemplo:Primaria, Secundaria
    """
    nombre_nivel_instruccion = models.CharField(max_length=200)


class TituloProfesional(models.Model):
    """
    Representa el listado de los títulos profesionales de una persona
    """
    nombre_titulo = models.CharField(max_length=300)


class Cargo(models.Model):
    """
    Cargos profesionales de personas
    """
    nombre_cargo = models.CharField(max_length=300)


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
