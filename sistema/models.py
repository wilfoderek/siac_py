# coding=utf-8
import django.db
from django.contrib.auth.models import User

# Create your models here.


class TipoIdentificacion(django.db.models.Model):
    """
    Representa tipos de identificación (CI - Pasaporte)
    """
    nombre_identificacion = django.db.models.CharField(max_length=100)


class Genero(django.db.models.Model):
    """
    Representa el género de una persona: Masculino, Femenino, etc
    """
    nombre = django.db.models.CharField(max_length=100)


class TipoSangre(django.db.models.Model):
    """
    Representa los diversos tipos de sangre existentes
    """
    nombre = django.db.models.CharField(max_length=100)


class EstadoCivil(django.db.models.Model):
    """
    Representa los diferentes estados civiles existentes
    """
    nombre = django.db.models.CharField(max_length=100)


class TipoEtnia(django.db.models.Model):
    """
    Representa las deniminaciones de etnias
    """
    nombre = django.db.models.CharField(max_length=100)


class Pais(django.db.models.Model):
    """
    Guarda los paises
    """
    nombre = django.db.models.CharField(max_length=100)


class Zonal(django.db.models.Model):
    """
    Representa la zonificación que tiene el país de acuerdo
    al ordenamietno territorial de la República del Ecuador
    """
    nombre = django.db.models.CharField(max_length=100)


class Provincia(django.db.models.Model):
    """
    Provincias principalmente de Ecuador y se relaciona con la zonal
    """
    nombre = django.db.models.CharField(max_length=100)
    pais = django.db.models.ForeignKey(Pais)
    zonal = django.db.models.ForeignKey(Zonal)


class Canton(django.db.models.Model):
    """
    Representa los cantones de las provincias del ecuador
    """
    nombre = django.db.models.CharField(max_length=100)
    provincia = django.db.models.ForeignKey(Provincia)


class Ciudad(django.db.models.Model):
    """
    Representa las ciudades del mundo
    """
    canton = django.db.models.ForeignKey(Canton)
    nombre = django.db.models.CharField(max_length=200)


class Parroquia(django.db.models.Model):
    """
    Parroquias pertenecientes a las ciudades del Ecuador
    """
    nombre = django.db.models.CharField(max_length=300)
    ciudad = django.db.models.ForeignKey(Ciudad)


class Parentesco(django.db.models.Model):
    """
    Representa los diferentes tipos de parentesco que un familiar
    o persona tiene con alguien registrado en el sistema
    """
    nombre = django.db.models.CharField(max_length=100)


class CategoriaInstitucion(django.db.models.Model):
    """
    Catergorías de institusiones y empresas
    Ejemplo: Banco, Universidad
    """
    nombre = django.db.models.CharField(max_length=100)


class TipoInstitucion(django.db.models.Model):
    """
    Tipos de empresas: Publicas, Privadas...
    """
    nombre = django.db.models.CharField(max_length=299)


class Institucion(django.db.models.Model):
    """
    Representa los datos de las institusiones o empresas registradas en el sistema
    @nombre guarda el nombre de una persona
    """
    nombre = django.db.models.CharField(max_length=200)
    representante = django.db.models.CharField(max_length=200)
    descripcion = django.db.models.CharField(max_length=200)
    email = django.db.models.CharField(max_length=200)
    telf1 = django.db.models.CharField(max_length=20)
    telf2 = django.db.models.CharField(max_length=20)
    direccion = django.db.models.CharField(max_length=300)
    ciudad = django.db.models.ForeignKey(Ciudad)
    categoria_empresa = django.db.models.ForeignKey(CategoriaInstitucion)
    tipo_institucion = django.db.models.ForeignKey(TipoInstitucion, null=True, blank=True)


class NivelInstruccion(django.db.models.Model):
    """
    Niveles de instruccion educativa que puede tener una persona
    Ejemplo:Primaria, Secundaria
    """
    nombre = django.db.models.CharField(max_length=200)


class TituloProfesional(django.db.models.Model):
    """
    Representa el listado de los títulos profesionales de una persona
    """
    nombre = django.db.models.CharField(max_length=300)


class Cargo(django.db.models.Model):
    """
    Cargos profesionales de personas
    """
    nombre = django.db.models.CharField(max_length=300)


class Persona(django.db.models.Model):
    """
    Representa los datos personales de una persona
    """
    nombre = django.db.models.CharField(max_length=200)
    apellido = django.db.models.CharField(max_length=200)
    direccion = django.db.models.TextField(null=True, blank=True)
    telefono = django.db.models.CharField(max_length=20)
    telefono_domicilio = django.db.models.CharField(max_length=20)
    celular = django.db.models.CharField(max_length=20)
    fecha_nacimiento = django.db.models.DateField(null=True, blank=True)
    fecha_registro = django.db.models.DateField(auto_now=True)

    #número de la casa.
    numero_domicilio = django.db.models.CharField(max_length=50)

    #ruc , cedula lo que sea
    numero_identificacion = django.db.models.CharField(max_length=20)

    #Boolean
    discapacidad = django.db.models.BooleanField()

    carne_conadis = django.db.models.CharField(max_length=50)
    porcentaje_discapacidad = django.db.models.DecimalField(max_digits=8, decimal_places=2, default=0)

    #nobre de la persona que se contactará
    contacto_emergencia = django.db.models.CharField(max_length=200)

    telefono_emergencia = django.db.models.CharField(max_length=20)
    celular_emergencia = django.db.models.CharField(max_length=20)
    email_emergencia = django.db.models.CharField(max_length=200)

    #código de acceso de la tarjeta de ingreso
    codigo_acceso = django.db.models.CharField(max_length=200)

    foto = django.db.models.CharField(max_length=300)

    #"estado de la persona: A:Activo , I:Inactivo ,etc "
    estado = django.db.models.CharField(max_length=2)

    usuario = django.db.models.ForeignKey(User, unique=True)

    #especifíca si es cédula , pasaporte...
    tipo_identidad = django.db.models.ForeignKey(TipoIdentificacion)

    #con la ciudad se tiene la provincia , país.
    ciudad_nacimiento = django.db.models.ForeignKey(Ciudad, related_name='ciudad_nacimiento')

    #ciudad de donde reside la persona actualmente
    ciudad_residencia = django.db.models.ForeignKey(Ciudad, related_name='ciudad_residencia')

    #nacionalidad de la personas
    pais_nacimiento = django.db.models.CharField(max_length=100)
    estado_civil = django.db.models.ForeignKey(EstadoCivil)
    tipo_sangre = django.db.models.ForeignKey(TipoSangre)

    #genero de las personas
    genero = django.db.models.ForeignKey(Genero)

    # etnia de la persona
    etnia = django.db.models.ForeignKey(TipoEtnia)
