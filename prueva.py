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

def main():
    class persona():
        def __init__(self, documento, nombre_completo):
            self.__documento = documento
            self.__nombre_completo = nombre_completo

        def set_documento(self, documento):
            self.__documento = documento

        def get_documento(self):
            return self.__documento

        def set_nombre(self, nombre):
            self.__nombre_completo = nombre

        def get_nombre(self):
            return self.__nombre_completo
        
        def infomacion(self, value):
            while True:
                nombre = str(input("Ingrese el nombre de la persona: "))
                if nombre.replace("", "").isalpha():
                    self.set_nombre(nombre)
                    correcto_nombre = True
                    break
                else:
                    correcto_nombre = False
                    print("Solo puede usar caracteres alfabéticos.")

            while True:
                documento = str(input("Ingrese el documento de la persona: "))
                if documento.isnumeric():
                    self.set_documento(documento)
                    correcto_doc = True
                    break
                else:
                    correcto_doc = False
                    print("No puede ingresar caracteres alfabéticos ni especiales en el documento.")

            if value == 1:
                if correcto_nombre and correcto_doc:
                    print("Mi nombre es: {0} y tengo el documento: {1}".format(self.get_nombre(), self.get_documento()))
    class aprendiz(persona):
            def __init__(self, documento, nombre_completo,ficha, programa):
                super().__init__(documento, nombre_completo)
                self.__ficha = ficha
                self.__programa = programa
                

            def set_ficha(self,ficha):
                self.__ficha = ficha


            def get_ficha(self):
                return self.__ficha
            

            def set_programa(self, programa):
                self.__programa = programa
            

            def get_programa(self):
                return self.__programa
            
            
    class EtapaLectiva(aprendiz):
        def __init__(self, documento, nombre_completo, ficha, programa, NumeroTrimestre, FechaIni, FechaTer, estado):
              super().__init__(documento, nombre_completo, ficha, programa)
              self.__NumeroTrimestre = NumeroTrimestre
              self.__FechaInicio = FechaIni
              self.__FechaTerminacion = FechaTer
              self.__estado = estado


        def set_FechaIni(self, Fechaini):
             self.__FechaInicio = Fechaini


        def get_FechaIni(self):
            return self.__FechaInicio
        
        
        def set_NumeroTrimestre(self, NumeroTrimestre):
            self.__NumeroTrimestre = NumeroTrimestre


        def get_NumeroTrimestre(self):
            return self.__NumeroTrimestre

        
        def set_FechaTerminacion(self,FechaTer):
            self.__FechaTerminacion = FechaTer


        def get_FechaTerminacion(self):
            return self.__FechaTerminacion

        def set_estado(self,estados):
            self.__estado = estados
            
        def get_estado(self):
            return self.__estado
        
        def informacion(self):
                tabla = ("""
☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼   
☼                                                                                                                                                                                      ☼
☼                                                           INFORME ETAPA ELECTIVA APRENDIZ 2024 SENA CBA                                                                              ☼    
☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼
☼                                                                                                                                                                                      ☼
☼ NOMBRE                          DOCUMENTO               FICHA                PROGRAMA                                FECHA_INICIO           FECHA_FINAL           ESTADO             ☼    
☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼
""")
                tabla = tabla + "{7} {0:<32}{1:<24}{2:<21}{3:<40}{4:<23}{5:<22}{6:<18} {7}".format(self.get_nombre(), 
                self.get_documento(), self.get_ficha(), self.get_programa(),self.get_FechaIni(),self.get_FechaTerminacion(),self.get_estado(),'☼')
                tabla = tabla + """    
☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼
                """
                print(tabla)
    
    
    class EtapaPratica(aprendiz):
        def __init__(self, documento, nombre_completo, ficha, programa, Modalidad, FechaIni, FechaTer, estado):
              super().__init__(documento, nombre_completo, ficha, programa)
              self.__Modalidad = Modalidad
              self.__FechaInicio = FechaIni
              self.__FechaTerminacion = FechaTer
              self.__estado = estado


        def set_FechaIni(self, Fechaini):
                self.__FechaInicio = Fechaini


        def get_FechaIni(self):
            return self.__FechaInicio
        
        
        def set_Modaliad(self, Modalidad):
            self.__Modalidad = Modalidad


        def get_Modalidad(self):
            return self.__Modalidad

        
        def set_FechaTerminacion(self,FechaTer):
            self.__FechaTerminacion = FechaTer


        def get_FechaTerminacion(self):
            return self.__FechaTerminacion

        def set_estado(self,estados):
            self.__estado = estados
            
        def get_estado(self):
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
        def __init__(self, documento, nombre_completo, profecion, salario_bas):
             super().__init__(documento, nombre_completo)
             self.__profesion = profecion
             self.__salario_basico = salario_bas

        def set_profesion(self, value):
             self.__profesion = value


        def get_profesion(self):
             return self.__profesion
        

        def set_salario_bas(self, value):
             self.__salario_basico = value


        def get_salario_bas(self):
             return self.__salario_basico
        

        def leer_Datos(self,value):
            instructor1 = instructor("","",0,"")
            instructor1.infomacion(value)
            profecion = str(input("digite la profecion del instructor: "))
            salario_basico = 12000000
            instructor1.set_profesion(profecion)
            instructor1.set_salario_bas(salario_basico)
            print(f"el instructor: {instructor1.get_nombre()} se postulo a: {instructor1.get_profesion()} y tiene un salario basico de: {instructor1.get_salario_bas()}$")
            print("Presione enter para continuar")
            print("" + Fore.RESET + Back.RESET)
           
            press = None
            while press not in ["\r"]:
                press = getwch()
        def contrato():
             print("void")
    
    class InstructorPlanta(instructor):
        def __init__(self, documento, nombre_completo, profecion, salario_bas,grad,fech_vincu):
              super().__init__(documento, nombre_completo, profecion, salario_bas)
              self.__grado = grad
              self.__fecha_vincula = fech_vincu

        def set_grad(self,value):
             self.__grado = value
        
        def get_grad(self):
             return self.__grado

        def set_fecha_vincu(self,value):
             self.__fecha_vincula = value
        
        def get_fecha_vincu(self):
             return self.__fecha_vincula    
        def leer_Datos(self, value):
            estados = ("retirado", "licencia" "activo", "inactivo", "vacaciones")
            estado_1 = random.choice(estados)
            instructor_plant = InstructorPlanta("","","","","","")
            print("Clase Instructor de planta")
            while True:
                 try:
                    nombre = str(input("ingrese el nombre del instructor: "))
                    break
                 except ValueError:
                      print("no puede introducir caracteres numericos")
            while True:
                 try:
                    documento = int(input("ingrese el documento del instructor: "))
                    documento_revi = str(documento)
                    if len(documento_revi) < 7:
                         print("los documentos no pueden tener una logitud menor a 7")
                    else:
                        break
                 except ValueError:
                      print("Introdusca solo caracteres numericos")
            while True:
                 try:
                    profecion = str(input("ingrese la profecion del instructor: "))
                    break
                 except ValueError:
                      print("solo use caracteres alfabeticos")
            instructor_plant.set_profesion(profecion)
            instructor_plant.set_documento(documento)
            instructor_plant.set_nombre(nombre)
            while True:
                try:
                    fecha_vinculacion = str(input("ingrese la fecha de vinculacion: "))
                    break
                except:
                     print("No utilise caracteres numericos")
            grado = int(input("ingrese el grado del instructor: "))
            instructor_plant.set_fecha_vincu(fecha_vinculacion)
            instructor_plant.set_grad(grado)
            salario = 1200000

            grad_multi = grado * 100000
            salario += grad_multi
            print("mi nombre es: {0} trabajo en: {4} tengo el documento: {1} fui vinculado el: {4} mi salario es:{2} tengo el grado numero: {3} y mi estado es: {5}".format(instructor_plant.get_nombre(),instructor_plant.get_documento(), salario, grado, instructor_plant.get_profesion(),estado_1))
            press = None
        print("Presione enter para continuar")
        print("" + Fore.RESET + Back.RESET)
        while press not in ["\r"]:
            press = getwch()

    class InstructorContrato(instructor):
        def __init__(self, documento, nombre_completo, profecion, salario_bas):
            super().__init__(documento, nombre_completo, profecion, salario_bas)

        def leer_datos_1(self):
            print("Clase Instructor de contrato")
            Instructor_contra = instructor("","","","")
            nombre = str(input("ingrese el nombre del instructor: "))
            documento = int(input("ingrese el documento del instructor: "))
            profecion = str(input("ingrese la profecion del instructor: "))
            Instructor_contra.set_profesion(profecion)
            Instructor_contra.set_documento(documento)
            Instructor_contra.set_nombre(nombre)
            
            # Solicitar la fecha de inicio del contrato al usuario
            fecha_inicio_str = input("Ingrese la fecha de inicio del contrato (YYYY-MM-DD): ")

            fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")

            # Solicitar la duración del contrato en meses al usuario
            duracion_meses = int(input("Ingrese la duración del contrato en meses: "))

            # Calcular la fecha de finalización del contrato sumando los meses
            fecha_fin = fecha_inicio + relativedelta(months=duracion_meses)

            # Calcular la duración total en días
            duracion_total = fecha_fin - fecha_inicio
            print("Mi nombre es: {0} tengo el documento: {1} trabajo en: {2}".format(Instructor_contra.get_nombre(), Instructor_contra.get_documento(), Instructor_contra.get_profesion()))
            print(f"Fecha de inicio del contrato: {fecha_inicio.strftime('%Y-%m-%d')}")
            print(f"Fecha de finalización del contrato: {fecha_fin.strftime('%Y-%m-%d')}")
            print(f"Duración total del contrato en días: {duracion_total.days}")
            
                            

         

    osystem('cls')
    elecion = None
    persona1 = persona("","")
    print("Clase persona")
    persona1.infomacion(1)
    print("Presione enter para continuar")
    print("" + Fore.RESET + Back.RESET)
    press = None
    while press not in ["\r"]:
            press = getwch()


    osystem("cls")
    print("Clase EtapaLectiva")
    aprediz1 = EtapaLectiva(" ", " ", " "," "," "," "," "," ")
    documento = str(input("introduzca el documento de el aprendiz: "))
    nombre = str(input("introduzca el nombre de el aprendiz: "))
    ficha = str(input("introduzca la ficha del aprendiz: "))
    programa = str(input("introduzca el programa del aprendiz: "))
    fechaini = str(input("introduzca la fecha de inicio del programa: "))
    fecharter = str(input("Introdusca la fecha de terminacion del programa: "))
    aprediz1.set_documento(documento)
    aprediz1.set_nombre(nombre)
    aprediz1.set_ficha(ficha)
    aprediz1.set_programa(programa)
    aprediz1.set_FechaIni(fechaini)
    aprediz1.set_FechaTerminacion(fecharter)
    estados = ("Induccion","En formacion","activo","retirado","condicionado")
    estado_selec = random.choice(estados)
    # aprediz1.set_documento("1073426335")
    # aprediz1.set_nombre("Juan Sebastian Lopez Morales")
    # aprediz1.set_ficha("287795")
    # aprediz1.set_programa("Analizis y desarrollo de sofware")
    # aprediz1.set_FechaIni("28/06/2025")
    # aprediz1.set_FechaTerminacion("28/07/2027")
    aprediz1.set_estado(estado_selec)
    aprediz1.informacion()
    press = None
    print("Presione enter para continuar")
    while press not in ["\r"]:
            press = getwch()

    def leer_datos_general():
        osystem("cls")
        print("Clase EtapaLectiva")
        aprediz1 = EtapaPratica(" ", " ", " "," "," "," "," "," ")
        documento = str(input("introduzca el documento de el aprendiz: "))
        nombre = str(input("introduzca el nombre de el aprendiz: "))
        ficha = str(input("introduzca la ficha del aprendiz: "))
        programa = str(input("introduzca el programa del aprendiz: "))
        fechaini = str(input("introduzca la fecha de inicio del programa: "))
        fecharter = str(input("Introdusca la fecha de terminacion del programa: "))
        aprediz1.set_documento(documento)
        aprediz1.set_nombre(nombre)
        aprediz1.set_ficha(ficha)
        aprediz1.set_programa(programa)
        aprediz1.set_FechaIni(fechaini)
        aprediz1.set_FechaTerminacion(fecharter)
        estados = ("Induccion","activo","retirado","condicionado")
        modalidades = ("Precensial", "virtual")
        modalidad_selec = random.choice(modalidades)
        estado_selec = random.choice(estados)
        # aprediz1.set_documento("1073426335")
        # aprediz1.set_nombre("Juan Sebastian Lopez Morales")
        # aprediz1.set_ficha("287795")
        # aprediz1.set_programa("Analizis y desarrollo de sofware")
        # aprediz1.set_FechaIni("28/06/2025")
        # aprediz1.set_FechaTerminacion("28/07/2027")
        aprediz1.set_estado(estado_selec)
        aprediz1.set_Modaliad(modalidad_selec)
        aprediz1.informacion()
        press = None
        print("Presione enter para continuar")
        print("" + Fore.RESET + Back.RESET)
        while press not in ["\r"]:
            press = getwch()


        osystem('cls')
        instructor1 = instructor("","",0,"")
        instructor1.leer_Datos(0)
        
        osystem('cls')
        instructor_planta = InstructorPlanta("","","","","","")
        instructor_planta.leer_Datos(0)
        
        
        instruc_con = InstructorContrato("","","","")
        instruc_con.leer_datos_1()
    leer_datos_general()
if __name__ == '__main__':
    main()