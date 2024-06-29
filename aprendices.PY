"""
Centro de Biotecnologia Agropecuaria
Ficha: 2877795
aprendiz: Juan Sebastian Lopez
Version: 3.0
Fecha 20/05/2024
"""
from modulos.funciones import mostrar_menu
import modulos
import modulos.funciones
import msvcrt

def main():
    while True:
        mostrar_menu()
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            modulos.funciones.limpiar_lista()
            
        elif opcion == '2':
            modulos.funciones.ingresar_aprendiz()
        elif opcion == '3':
            modulos.funciones.listar_aprendices()
            print("presione una tecla para continuar")
            msvcrt.getch()
        elif opcion == '4':
            modulos.funciones.lista_ficha()
            print("presione una tecla para continuar")
            msvcrt.getch()
        elif opcion == '5':
            modulos.funciones.buscar_por_evaluacion()
            print("presione una tecla para continuar")
            msvcrt.getch()
        elif opcion == '6':
            modulos.funciones.borrar_aprendiz()
        elif opcion == '7':
            modulos.funciones.actualizar_aprendiz()
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
if __name__ == '__main__':
    main()