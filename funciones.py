"""
Centro de Biotecnologia Agropecuaria
Ficha: 2877795
aprendiz: Juan Sebastian Lopez
Version: 3.0
Fecha 20/05/2024
"""

#*************


import msvcrt
#Importamos el colorama
from colorama import Back, Fore, Style, Cursor, init
#Aca iniciamos el colorama
init()
#Impostamos la libreria os para acceder al sistema
import os


#Funcion para digitar solo numeros
def solo_numeros(prompt):
    while True:
        entrada=input(prompt)
        if entrada.isdigit():
            return entrada
        else:
            print ("Solo se pueden digitar numeros")
            


#Funcion para poder digitar numeros y tenga un minimo de 6 y maximo de 10
def solo_numeros_seis(prompt):
    while True:
        entrada = input(prompt)
        if entrada.isdigit() and 6 <= len(entrada) <= 10:
            return entrada
        else:
            print('\n'"La entrada debe contener solo numeros y un minimo entre 6 y 10 caracteres.")


#Funcion para digitar solo numeros con un limite de 7
def solo_numeros_siete(prompt):
    while True:
        entrada = input(prompt)
        if entrada.isdigit() and len(entrada) == 7:
            return entrada
        else:
            print('\n'"La entrada debe ser solo numeros y debe contener exactamente 7 caracteres")

#Funcion para digitar solo letras
def solo_letras(prompt):
    while True:
        entrada=input(prompt)
        if entrada.replace(" ","").isalpha():
            return entrada
        else:
            print ('\n'"Solo se pueden digitar letras")

#Definimos la funcion de el menu principal
def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "╔════════════════════════════╗")
    print("║     BIENVENIDO AL PROGRAMA ║")
    print("╠════════════════════════════╣")
    print("║                            ║")
    print(Fore.GREEN + Back.BLACK + '║  1. Iniciar lista          ║')
    print("║                            ║")
    print(Fore.GREEN + Back.BLACK + '║  2. Ingreso Aprendiz       ║')
    print("║                            ║")
    print(Fore.GREEN + Back.BLACK + '║  3. Lista aprendices       ║')
    print("║                            ║")
    print(Fore.GREEN + Back.BLACK + '║  4. Lista por fichas       ║')
    print("║                            ║")
    print(Fore.GREEN + Back.BLACK + '║  5. Resultado Aprendices   ║')
    print("║     por ficha              ║")
    print(Fore.GREEN + Back.BLACK + '║                            ║')
    print("║                            ║")
    print(Fore.GREEN + Back.BLACK + '║  6. Borrar aprendices      ║')
    print("║                            ║")
    print(Fore.GREEN + Back.BLACK + '║  7. Actualizar información ║')
    print("║                            ║")
    print(Fore.RED + Back.BLACK + '║  0. Salir                  ║')
    print("║                            ║")
    print(Fore.CYAN + "╚════════════════════════════╝")
    print(" ")


init(autoreset=True)

# Creamos una lista vacía para almacenar los diccionarios
lista_aprendices = []


# Función para limpiar la lista de aprendices
def limpiar_lista():
    lista_aprendices.clear()


# Función para ingresar un nuevo aprendiz
def ingresar_aprendiz():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiamos la pantalla
    print(Fore.LIGHTYELLOW_EX + "*******   BIENVENIDO AL REGISTRO DE APRENDICES   ********")
    print(" ")  # Dejamos un espacio

    # Solicitamos los datos al usuario
    Nombre = input(Fore.CYAN + "Ingrese su nombre y apellido: " + Style.RESET_ALL)
    Documento = input(Fore.CYAN + "Ingrese su documento: " + Style.RESET_ALL)
    Ficha = input(Fore.CYAN + "Ingrese el número de ficha de su programa: " + Style.RESET_ALL)

    while True:
        Evaluacion = input(Fore.CYAN + "Ingrese su evaluación (A o D): " + Style.RESET_ALL).upper()
        if Evaluacion in ['A', 'D']:
            break
        else:
            print(Fore.CYAN + "Ingrese una opción válida (A o D)." + Style.RESET_ALL)

    # Creamos un diccionario con los datos del aprendiz
    aprendiz = {'Nombre': Nombre, 'Documento': Documento, 'Ficha': Ficha, 'Evaluacion': Evaluacion}

    # Agregamos el diccionario a la lista
    lista_aprendices.append(aprendiz)


# Función para listar todos los aprendices ingresados
def listar_aprendices():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiamos la pantalla
    print(Fore.LIGHTYELLOW_EX + "*******   LISTA DE APRENDICES REGISTRADOS   ********")
    print(" ")  # Dejamos un espacio

    # Iteramos sobre la lista de aprendices y mostramos sus datos
    for aprendiz in lista_aprendices:
        print(f"Nombre: {aprendiz['Nombre']}, Documento: {aprendiz['Documento']}, Ficha: {aprendiz['Ficha']}, Evaluación: {aprendiz['Evaluacion']}")
        print(" ")  # Dejamos un espacio


# Función para listar los aprendices agrupados por ficha
def lista_ficha():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiamos la pantalla
    print(Fore.LIGHTYELLOW_EX + "*******   LISTA DE APRENDICES POR FICHA   ********")
    print(" ")  # Dejamos un espacio

    # Obtenemos todas las fichas únicas
    fichas_unicas = list(set([aprendiz['Ficha'] for aprendiz in lista_aprendices]))

    # Iteramos sobre las fichas únicas y mostramos los aprendices para cada una
    for ficha in fichas_unicas:
        print(Fore.BLUE + f"Ficha: {ficha}" + Style.RESET_ALL)
        for aprendiz in lista_aprendices:
            if aprendiz['Ficha'] == ficha:
                print(f"Nombre: {aprendiz['Nombre']}, Documento: {aprendiz['Documento']}, Evaluación: {aprendiz['Evaluacion']}")
        print(" ")  # Dejamos un espacio


# Función para buscar aprendices por evaluación (A o D)
def buscar_por_evaluacion():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiamos la pantalla
    print(Fore.LIGHTYELLOW_EX + "*******   LISTA DE APRENDICES POR FICHA   ********")
    print(" ")  # Dejamos un espacio

    # Obtenemos todas las fichas únicas
    fichas_unicas = list(set([aprendiz['Ficha'] for aprendiz in lista_aprendices]))

    # Iteramos sobre las fichas únicas y mostramos los aprendices para cada una
    for ficha in fichas_unicas:
        print(Fore.BLUE + f"Ficha: {ficha}" + Style.RESET_ALL)
        for aprendiz in lista_aprendices:
            if aprendiz['Ficha'] == ficha:
                # Coloreamos el nombre según la evaluación
                if aprendiz['Evaluacion'] == 'A':
                    print(f"Nombre: {Fore.GREEN}{aprendiz['Nombre']}{Style.RESET_ALL}, Documento: {aprendiz['Documento']}, Evaluación: {aprendiz['Evaluacion']}")
                elif aprendiz['Evaluacion'] == 'D':
                    print(f"Nombre: {Fore.RED}{aprendiz['Nombre']}{Style.RESET_ALL}, Documento: {aprendiz['Documento']}, Evaluación: {aprendiz['Evaluacion']}")
    print(" ")  # Dejamos un espacio



# Función para eliminar un aprendiz por número de documento
def borrar_aprendiz():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiamos la pantalla
    print(Fore.LIGHTYELLOW_EX + "*******   ELIMINAR APRENDIZ POR DOCUMENTO   ********")
    print(" ")  # Dejamos un espacio

    # Mostramos todos los aprendices registrados
    for i, aprendiz in enumerate(lista_aprendices):
        print(f"Índice: {i}, Nombre: {aprendiz['Nombre']}, Documento: {aprendiz['Documento']}, Ficha: {aprendiz['Ficha']}, Evaluación: {aprendiz['Evaluacion']}")
        print(" ")  # Dejamos un espacio

    # Solicitamos al usuario ingresar el número de documento del aprendiz a eliminar
    documento_buscar = input("Ingrese el número de documento del aprendiz a eliminar: ")

    # Buscamos el aprendiz por documento y lo eliminamos si se encuentra
    for i, aprendiz in enumerate(lista_aprendices):
        if aprendiz['Documento'] == documento_buscar:
            del lista_aprendices[i]
            print("Aprendiz eliminado correctamente.")
            return

    # Si no se encontró ningún aprendiz con el documento ingresado
    print("No se encontró ningún aprendiz con el documento especificado.")


# Función para actualizar la información de un aprendiz por número de documento
def actualizar_aprendiz():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiamos la pantalla
    print(Fore.LIGHTYELLOW_EX + "*******   ACTUALIZAR APRENDIZ POR DOCUMENTO   ********")
    print(" ")  # Dejamos un espacio

    # Mostramos todos los aprendices registrados
    for i, aprendiz in enumerate(lista_aprendices):
        print(f"Índice: {i}, Nombre: {aprendiz['Nombre']}, Documento: {aprendiz['Documento']}, Ficha: {aprendiz['Ficha']}, Evaluación: {aprendiz['Evaluacion']}")
        print(" ")  # Dejamos un espacio

    # Solicitamos al usuario ingresar el número de documento del aprendiz a actualizar
    documento_buscar = input("Ingrese el número de documento del aprendiz a actualizar: ")

    # Buscamos el aprendiz por documento y mostramos sus datos si se encuentra
    for i, aprendiz in enumerate(lista_aprendices):
        if aprendiz['Documento'] == documento_buscar:
            print(f"Aprendiz encontrado:\n")
            print(f"Nombre: {aprendiz['Nombre']}, Documento: {aprendiz['Documento']}, Ficha: {aprendiz['Ficha']}, Evaluación: {aprendiz['Evaluacion']}\n")
            
            # Solicitamos al usuario ingresar los nuevos datos para el aprendiz
            nuevo_nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar): ")
            nueva_ficha = input("Ingrese el nuevo número de ficha (deje en blanco para no cambiar): ")
            nueva_evaluacion = input("Ingrese la nueva evaluación (A o D, deje en blanco para no cambiar): ").upper()

            # Actualizamos los datos del aprendiz si el usuario ingresó valores nuevos
            if nuevo_nombre:
                aprendiz['Nombre'] = nuevo_nombre
            if nueva_ficha:
                aprendiz['Ficha'] = nueva_ficha
            if nueva_evaluacion in ['A', 'D']:
                aprendiz['Evaluacion'] = nueva_evaluacion

            print("Datos del aprendiz actualizados correctamente.")
            return

    # Si no se encontró ningún aprendiz con el documento ingresado
    print("No se encontró ningún aprendiz con el documento especificado.")