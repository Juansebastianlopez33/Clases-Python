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
from modulos import Classes

def main():
    """
    Función principal para ejecutar el programa, demostrando el uso de las Clases.
    """
    osystem("cls")
    print("Clase EtapaLectiva")
    aprediz1 = Classes.EtapaLectiva(" ", " ", " ", " ", " ", " ", " ", " ")

    # Recopilación y validación de la entrada del usuario para EtapaLectiva
    while True:
        try:
            documento = int(input("Introduzca el documento del aprendiz: "))
            documento_revi = str(documento)
            if len(documento_revi) < 7:
                print("La longitud del documento debe ser mayor a 7")
            else:
                break
        except ValueError:
            print("Utilice los caracteres correctos: si es texto, alfabéticos; si es numérico, números")

    while True:
        try:
            nombre = str(input("Introduzca el nombre del aprendiz: "))
            if nombre.replace(" ", "").isalpha():
                break
        except ValueError:
            print("Utilice los caracteres correctos: si es texto, alfabéticos; si es numérico, números")

    while True:
        try:
            ficha = int(input("Introduzca la ficha del aprendiz: "))
            ficha_revicion = str(ficha)
            if len(ficha_revicion) < 6:
                print("Las fichas tienen que tener una longitud mayor o igual a 6 dígitos")
            else:
                break
        except ValueError:
            print("Utilice los caracteres correctos: si es texto, alfabéticos; si es numérico, números")

    while True:
            try:
                Trimestre = str(input("Ingrese el trimestre: "))
                if Trimestre.replace(" ", "").isalpha():    
                    break
            except ValueError:
                print("Solo puede digitar caracteres válidos en texto alfabéticos y en numéricos números.")

    while True:
        try:
            programa = str(input("Introduzca el programa del aprendiz: "))
            if programa.replace(" ", "").isalpha():
                break
        except ValueError:
            print("Utilice los caracteres correctos: si es texto, alfabéticos; si es numérico, números")

    while True:
        try:
            fechaini = str(input("Introduzca la fecha de inicio del programa: "))
            if fechaini.replace("-","").isnumeric():
                    break
        except ValueError:
            print("Utilice los caracteres correctos: si es texto, alfabéticos; si es numérico, números")
    while True:
        fecharter = str(input("Introduzca la fecha de terminación del programa: "))
        if fecharter.replace("-","").isnumeric():
                    break

    # Configuración de los atributos del aprendiz
    aprediz1.set_NumeroTrimestre(Trimestre)
    aprediz1.set_documento(documento)
    aprediz1.set_nombre(nombre)
    aprediz1.set_ficha(ficha)
    aprediz1.set_programa(programa)
    aprediz1.set_FechaIni(fechaini)
    aprediz1.set_FechaTerminacion(fecharter)

    # Selección aleatoria del estado del aprendiz
    estados = ("Inducción", "En formación", "Activo", "Retirado", "Condicionado")
    estado_selec = random.choice(estados)
    aprediz1.set_estado(estado_selec)
    aprediz1.informacion()

    press = None
    print("Presione enter para continuar")
    while press not in ["\r"]:
        press = getwch()

    def leer_datos_general():
        osystem("cls")
        print("Clase EtapaPractica")
        aprediz1 = Classes.EtapaPratica(" ", " ", " ", " ", " ", " ", " ", " ")

        while True:
            try:
                documento = int(input("Introduzca el documento del aprendiz: "))
                documento_revi = str(documento)
                if len(documento_revi) < 7:
                    print("El documento no puede tener una longitud menor a 7")
                else:
                    break
            except ValueError:
                print("NO PUEDE INGRESAR UN CARACTER DIFERENTE AL INDICADO: si es numérico, números; si es texto, alfabético")
        
        while True:
            try:
                nombre = str(input("Introduzca el nombre del aprendiz: "))
                if nombre.replace(" ","").isalpha():
                    break
            except ValueError:
                print("NO PUEDE INGRESAR UN CARACTER DIFERENTE AL INDICADO: si es numérico, números; si es texto, alfabético")
        
        while True:
            try:
                ficha = int(input("Introduzca la ficha del aprendiz: "))
                ficha_revicion = str(ficha)
                if len(ficha_revicion) < 7:
                    print("Las fichas tienen que tener una longitud mayor o igual a 7 dígitos")
                else:
                    break
            except ValueError:
                print("NO PUEDE INGRESAR UN CARACTER DIFERENTE AL INDICADO: si es numérico, números; si es texto, alfabético")

        while True:
            try:
                programa = str(input("Introduzca el programa del aprendiz: "))
                if programa.replace(" ", "").isalpha():
                    break
            except ValueError:
                print("NO PUEDE INGRESAR UN CARACTER DIFERENTE AL INDICADO: si es numérico, números; si es texto, alfabético")

        while True:
            try:
                fechaini = str(input("Introduzca la fecha de inicio del programa: "))
                if fechaini.replace("-","").isnumeric():
                    break
            except ValueError:
                print("NO PUEDE INGRESAR UN CARACTER DIFERENTE AL INDICADO: si es numérico, números; si es texto, alfabético")

        while True:
            try:
                fecharter = str(input("Introduzca la fecha de terminación del programa: "))
                if fecharter.replace("-","").isnumeric():
                    break
            except ValueError:
                print("NO PUEDE INGRESAR UN CARACTER DIFERENTE AL INDICADO: si es numérico, números; si es texto, alfabético")

        # Configuración de los atributos del aprendiz
        aprediz1.set_documento(documento)
        aprediz1.set_nombre(nombre)
        aprediz1.set_ficha(ficha)
        aprediz1.set_programa(programa)
        aprediz1.set_FechaIni(fechaini)
        aprediz1.set_FechaTerminacion(fecharter)

        # Selección aleatoria del estado y modalidad del aprendiz
        estados = ("Inducción", "Activo", "Retirado", "Condicionado")
        modalidades = ("Presencial", "Virtual")
        modalidad_selec = random.choice(modalidades)
        estado_selec = random.choice(estados)
        aprediz1.set_estado(estado_selec)
        aprediz1.set_Modaliad(modalidad_selec)
        aprediz1.informacion()

        press = None
        print("Presione enter para continuar")
        print("" + Fore.RESET + Back.RESET)
        while press not in ["\r"]:
            press = getwch()

        
        osystem('cls')
        instructor_planta = Classes.InstructorPlanta("", "", "", "", "", "")
        instructor_planta.leer_Datos(0)
        
        osystem("cls")
        instruc_con = Classes.InstructorContrato("", "", "", "")
        instruc_con.leer_datos_1()
    
    leer_datos_general()
if __name__ == '__main__':
    main()
