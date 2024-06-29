"""
Centro de Biotecnologia Agropecuaria
Ficha: 2877795
aprendiz: Juan Sebastian Lopez
Version: 3.0
Fecha 20/05/2024
"""   
import random
from msvcrt import getwch
from os import system as osystem
from colorama import Fore, Back
from random import randint
from datetime import datetime
from dateutil.relativedelta import relativedelta
class persona():
    """
    Clase que representa una persona con documento y nombre completo.
    """
    def __init__(self, documento, nombre_completo):
        self.__documento = documento
        self.__nombre_completo = nombre_completo

    def set_documento(self, documento):
        """
        Establece el documento de la persona.
        """
        self.__documento = documento

    def get_documento(self):
        """
        Obtiene el documento de la persona.
        """
        return self.__documento

    def set_nombre(self, nombre):
        """
        Establece el nombre completo de la persona.
        """
        self.__nombre_completo = nombre

    def get_nombre(self):
        """
        Obtiene el nombre completo de la persona.
        """
        return self.__nombre_completo

    def infomacion(self, value, val):
        """
        Recoge y valida el nombre y el documento de la persona.
        """
        while True:
            nombre = str(input(f"Ingrese el nombre de {val}: "))
            if nombre.replace("", "").isalpha():
                self.set_nombre(nombre)
                correcto_nombre = True
                break
            else:
                correcto_nombre = False
                print("Solo puede usar caracteres alfabéticos.")

        while True:
            documento = str(input(f"Ingrese el documento de {val}: "))
            if documento.isnumeric() and len(documento) > 6:
                self.set_documento(documento)
                correcto_doc = True
                break
            else:
                correcto_doc = False
                print("No puede ingresar caracteres alfabéticos ni especiales en el documento y debe tener una longitud mayor a 6.")

        if value == 1:
            if correcto_nombre and correcto_doc:
                print("Mi nombre es: {0} y tengo el documento: {1}".format(self.get_nombre(), self.get_documento()))


class aprendiz(persona):
    """
    Clase que representa a un aprendiz, hereda de la clase persona.
    """
    def __init__(self, documento, nombre_completo, ficha, programa):
        super().__init__(documento, nombre_completo)
        self.__ficha = ficha
        self.__programa = programa

    def set_ficha(self, ficha):
        """
        Establece la ficha del aprendiz.
        """
        self.__ficha = ficha

    def get_ficha(self):
        """
        Obtiene la ficha del aprendiz.
        """
        return self.__ficha

    def set_programa(self, programa):
        """
        Establece el programa del aprendiz.
        """
        self.__programa = programa

    def get_programa(self):
        """
        Obtiene el programa del aprendiz.
        """
        return self.__programa


class EtapaLectiva(aprendiz):
    """
    Clase que representa la etapa lectiva de un aprendiz, hereda de la clase aprendiz.
    """
    def __init__(self, documento, nombre_completo, ficha, programa, NumeroTrimestre, FechaIni, FechaTer, estado):
        super().__init__(documento, nombre_completo, ficha, programa)
        self.__NumeroTrimestre = NumeroTrimestre
        self.__FechaInicio = FechaIni
        self.__FechaTerminacion = FechaTer
        self.__estado = estado

    def set_FechaIni(self, Fechaini):
        """
        Establece la fecha de inicio de la etapa lectiva.
        """
        self.__FechaInicio = Fechaini

    def get_FechaIni(self):
        """
        Obtiene la fecha de inicio de la etapa lectiva.
        """
        return self.__FechaInicio

    def set_NumeroTrimestre(self, NumeroTrimestre):
        """
        Establece el número de trimestre de la etapa lectiva.
        """
        self.__NumeroTrimestre = NumeroTrimestre

    def get_NumeroTrimestre(self):
        """
        Obtiene el número de trimestre de la etapa lectiva.
        """
        return self.__NumeroTrimestre

    def set_FechaTerminacion(self, FechaTer):
        """
        Establece la fecha de terminación de la etapa lectiva.
        """
        self.__FechaTerminacion = FechaTer

    def get_FechaTerminacion(self):
        """
        Obtiene la fecha de terminación de la etapa lectiva.
        """
        return self.__FechaTerminacion

    def set_estado(self, estados):
        """
        Establece el estado del aprendiz durante la etapa lectiva.
        """
        self.__estado = estados

    def get_estado(self):
        """
        Obtiene el estado del aprendiz durante la etapa lectiva.
        """
        return self.__estado

        
    def informacion(self):
                tabla = ("""
☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼   
☼                                                                                                                                                                                      ☼
☼                                                           INFORME ETAPA ELECTIVA APRENDIZ 2024 SENA CBA                                                                              ☼    
☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼
☼                                                                                                                                                                                      ☼
☼ NOMBRE                          DOCUMENTO               FICHA                PROGRAMA         TRIMESTRE              FECHA_INICIO           FECHA_FINAL           ESTADO             ☼    
☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼
""")
                tabla = tabla + "{8} {0:<32}{1:<24}{2:<21}{3:<17}{4:<23}{5:<23}{6:<21} {7:<18} {8}".format(self.get_nombre(), 
                self.get_documento(), self.get_ficha(), self.get_programa(),self.get_NumeroTrimestre(),self.get_FechaIni(),self.get_FechaTerminacion(),self.get_estado(),'☼')
                tabla = tabla + """    
☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼
                """
                print(tabla)
    
    
class EtapaPratica(aprendiz):
    """
    Clase que representa la etapa práctica de un aprendiz, hereda de la clase aprendiz.
    """
    def __init__(self, documento, nombre_completo, ficha, programa, Modalidad, FechaIni, FechaTer, estado):
        super().__init__(documento, nombre_completo, ficha, programa)
        self.__Modalidad = Modalidad
        self.__FechaInicio = FechaIni
        self.__FechaTerminacion = FechaTer
        self.__estado = estado

    def set_FechaIni(self, Fechaini):
        """
        Establece la fecha de inicio de la etapa práctica.
        """
        self.__FechaInicio = Fechaini

    def get_FechaIni(self):
        """
        Obtiene la fecha de inicio de la etapa práctica.
        """
        return self.__FechaInicio

    def set_Modaliad(self, Modalidad):
        """
        Establece la modalidad de la etapa práctica.
        """
        self.__Modalidad = Modalidad

    def get_Modalidad(self):
        """
        Obtiene la modalidad de la etapa práctica.
        """
        return self.__Modalidad

    def set_FechaTerminacion(self, FechaTer):
        """
        Establece la fecha de terminación de la etapa práctica.
        """
        self.__FechaTerminacion = FechaTer

    def get_FechaTerminacion(self):
        """
        Obtiene la fecha de terminación de la etapa práctica.
        """
        return self.__FechaTerminacion

    def set_estado(self, estados):
        """
        Establece el estado del aprendiz durante la etapa práctica.
        """
        self.__estado = estados

    def get_estado(self):
        """
        Obtiene el estado del aprendiz durante la etapa práctica.
        """
        return self.__estado

    def informacion(self):
            print("" + Fore.BLACK + Back.WHITE)
            tabla = ("""
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░                                                                                                                                                                                                     ░
    ░                                                                    INFORME ETAPA PRACTICA APRENDIZ 2024 SENA CBA                                                                                    ░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░                                                                                                                                                                                                     ░
    ░ NOMBRE                          DOCUMENTO               FICHA                PROGRAMA                           MODALIDAD                   FECHA_INICIO           FECHA_FINAL         ESTADO       ░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    """)
            tabla = tabla +"{8} {0:<32}{1:<24}{2:<21}{3:<35}{4:<28}{5:<23}{6:<19} {7:<13}{8}".format(self.get_nombre(), 
            self.get_documento(), self.get_ficha(), self.get_programa(),self.get_Modalidad(),self.get_FechaIni(),self.get_FechaTerminacion(),self.get_estado(),'░')
            tabla = tabla+"""
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                """
            print(tabla)


class instructor(persona):
    """
    Clase que representa a un instructor, hereda de la clase persona.
    """
    def __init__(self, documento, nombre_completo, profesion, salario_bas):
        super().__init__(documento, nombre_completo)
        self.__profesion = profesion
        self.__salario_basico = salario_bas

    def set_profesion(self, value):
        """
        Establece la profesión del instructor.
        """
        self.__profesion = value

    def get_profesion(self):
        """
        Obtiene la profesión del instructor.
        """
        return self.__profesion

    def set_salario_bas(self, value):
        """
        Establece el salario básico del instructor.
        """
        self.__salario_basico = value

    def get_salario_bas(self):
        """
        Obtiene el salario básico del instructor.
        """
        return self.__salario_basico

    def leer_Datos(self, value):
        """
        Lee los datos del instructor y los imprime.
        """
        instructor1 = instructor("", "", 0, "")
        val = 'el instructor'
        instructor1.infomacion(value, val)
        while True:
            try:
                profesion = str(input("Digite la profesión del instructor: "))
                break
            except ValueError:
                print("No puede usar caracteres numéricos.")
        salario_basico = 12000000
        instructor1.set_profesion(profesion)
        instructor1.set_salario_bas(salario_basico)
        print(f"El instructor: {instructor1.get_nombre()} se postuló a: {instructor1.get_profesion()} y tiene un salario básico de: {instructor1.get_salario_bas()}$")
        print("Presione enter para continuar")
        print("" + Fore.RESET + Back.RESET)

        press = None
        while press not in ["\r"]:
            press = getwch()

    def contrato():
        """
        Método vacío para contrato.
        """
        print("void")

class InstructorPlanta(instructor):
    """
    Clase que representa a un instructor de planta, hereda de la clase instructor.
    """
    def __init__(self, documento, nombre_completo, profesion, salario_bas, grad, fech_vincu):
        super().__init__(documento, nombre_completo, profesion, salario_bas)
        self.__grado = grad
        self.__fecha_vincula = fech_vincu

    def set_grad(self, value):
        """
        Establece el grado del instructor.
        """
        self.__grado = value

    def get_grad(self):
        """
        Obtiene el grado del instructor.
        """
        return self.__grado

    def set_fecha_vincu(self, value):
        """
        Establece la fecha de vinculación del instructor.
        """
        self.__fecha_vincula = value

    def get_fecha_vincu(self):
        """
        Obtiene la fecha de vinculación del instructor.
        """
        return self.__fecha_vincula

    def leer_Datos(self, value):
        """
        Lee los datos del instructor de planta y los imprime.
        """
        estados = ("retirado", "licencia", "activo", "inactivo", "vacaciones")
        estado_1 = random.choice(estados)
        instructor_plant = InstructorPlanta("", "", "", "", "", "")
        print("Clase Instructor de planta")
        while True:
            try:
                nombre = str(input("Ingrese el nombre del instructor: "))
                if nombre.replace(" ", "").isalpha():    
                    break
            except ValueError:
                print("Solo puede digitar caracteres válidos en texto alfabéticos y en numéricos números.")
        while True:
            try:
                documento = int(input("Ingrese el documento del instructor: "))
                documento_revi = str(documento)
                if len(documento_revi) < 7:
                    print("No puede digitar un documento menor a 7 dígitos.")
                else:
                    break
            except ValueError:
                print("Solo puede digitar caracteres válidos en texto alfabéticos y en numéricos números.")
        while True:
            try:
                profesion = str(input("Ingrese la profesión del instructor: "))
                if profesion.replace(" ","").isalpha():
                    break
            except ValueError:
                print("Solo puede digitar caracteres válidos en texto alfabéticos y en numéricos números.")

        instructor_plant.set_profesion(profesion)
        instructor_plant.set_documento(documento)
        instructor_plant.set_nombre(nombre)
        while True:
            try:
                fecha_vinculacion = str(input("Ingrese la fecha de vinculación: "))
                break
            except ValueError:
                print("No puede dejar el campo vacío o usar caracteres especiales.")
        while True:
            try:
                grado = int(input("Ingrese el grado del instructor: "))
                break
            except ValueError:
                print("Solo caracteres numéricos, no use alfabéticos ni especiales.")
        instructor_plant.set_fecha_vincu(fecha_vinculacion)
        instructor_plant.set_grad(grado)
        salario = 1200000

        grad_multi = grado * 100000
        salario += grad_multi
        print("Mi nombre es: {0}, trabajo en: {5}, tengo el documento: {1}, fui vinculado el: {4}, mi salario es: {2}, tengo el grado número: {3} y mi estado es: {6}".format(instructor_plant.get_nombre(), instructor_plant.get_documento(), salario, grado, instructor_plant.get_fecha_vincu(), instructor_plant.get_profesion(), estado_1))
        press = None
        print("Presione enter para continuar")
        print("" + Fore.RESET + Back.RESET)
        while press not in ["\r"]:
            press = getwch()

class InstructorContrato(instructor):
    """
    Clase que representa a un instructor por contrato, hereda de la clase instructor.
    """
    def __init__(self, documento, nombre_completo, profesion, salario_bas):
        super().__init__(documento, nombre_completo, profesion, salario_bas)

    def leer_datos_1(self):
        """
        Lee los datos del instructor por contrato y los imprime.
        """
        print("Clase Instructor de contrato")
        Instructor_contra = instructor("", "", "", "")
        while True:
            try:
                nombre = str(input("Ingrese el nombre del instructor: "))
                break
            except ValueError:
                print("Digite caracteres válidos, texto o numéricos.")
        while True:
            try:
                documento = str(input("Ingrese el documento del instructor: "))
                if len(documento) < 7:
                    print("No puede tener una longitud menor a 7 dígitos.")
                else:
                    break
            except ValueError:
                print("Digite caracteres válidos, texto o numéricos.")
        while True:
            try:
                profesion = str(input("Ingrese la profesión del instructor: "))
                break
            except ValueError:
                print("Digite caracteres válidos, texto o numéricos.")
        Instructor_contra.set_profesion(profesion)
        Instructor_contra.set_documento(documento)
        Instructor_contra.set_nombre(nombre)

        # Solicitar la fecha de inicio del contrato al usuario
        while True:
            try:
                fecha_inicio_str = input("Ingrese la fecha de inicio del contrato (YYYY-MM-DD): ")
                break
            except ValueError:
                print("Introduzca una fecha válida usando el formato 2005-06-25.")

        fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")

        # Solicitar la duración del contrato en meses al usuario
        while True:
            try:
                duracion_meses = int(input("Ingrese la duración del contrato en meses: "))
                break
            except ValueError:
                print("No use caracteres especiales ni alfabéticos.")

        # Calcular la fecha de finalización del contrato sumando los meses
        fecha_fin = fecha_inicio + relativedelta(months=duracion_meses)

        # Calcular la duración total en días
        duracion_total = fecha_fin - fecha_inicio
        print("Mi nombre es: {0}, tengo el documento: {1}, trabajo en: {2}".format(Instructor_contra.get_nombre(), Instructor_contra.get_documento(), Instructor_contra.get_profesion()))
        print(f"Fecha de inicio del contrato: {fecha_inicio.strftime('%Y-%m-%d')}")
        print(f"Fecha de finalización del contrato: {fecha_fin.strftime('%Y-%m-%d')}")
        print(f"Duración total del contrato en días: {duracion_total.days}")




            
                            

         
