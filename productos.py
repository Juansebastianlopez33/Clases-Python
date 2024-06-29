"""
Centro de Biotecnologia Agropecuaria
Ficha: 2877795
aprendiz: Juan Sebastian Lopez
Version: 3.0
Fecha 20/05/2024
"""
import random
from os import system as osystem
from msvcrt import getch as get 
from datetime import datetime
from dateutil.relativedelta import relativedelta

def main():
    # Clase que representa un producto
    class Producto:
        def __init__(self, codigo, titulo, autor):
            self.__codigo = codigo
            self.__titulo = titulo
            self.__autor = autor

        # Método para establecer el código del producto
        def set_codigo(self, value):
            self.__codigo = value

        # Método para obtener el código del producto
        def get_codigo(self):
            return self.__codigo

        # Método para establecer el título del producto
        def set_titulo(self, value):
            self.__titulo = value

        # Método para obtener el título del producto
        def get_titulo(self):
            return self.__titulo

        # Método para establecer el autor del producto
        def set_autor(self, value):
            self.__autor = value

        # Método para obtener el autor del producto
        def get_autor(self):
            return self.__autor

        # Método para ingresar y mostrar información del producto
        def informacion(self, value):
            print("CLASE PRODUCTO GRABADO" + "\n")
            producto1 = Producto("", "", "")
            codigos = random.randint(101, 1000)
            producto1.set_codigo(codigos)

            while True:
                autor = str(input("Digite el autor del producto: "))
                if autor.replace("", "").isalpha():
                    producto1.set_autor(autor)
                    break
                else:
                    print("Solo puede usar caracteres alfabéticos.")

            while True:
                titulo = str(input("Digite el título del producto: "))
                if titulo.replace("", "").isalpha():
                    producto1.set_titulo(titulo)
                    break
                else:
                    print("Solo puede usar caracteres alfabéticos.")

            if value == 0:
                print("""
                    Título del producto: {0}
                    Autor del producto: {1}
                    Código del producto: {2}
                    """.format(producto1.get_titulo(), producto1.get_autor(), producto1.get_codigo()))

    # Clase que representa un producto grabado
    class ProductoGrabado(Producto):
        def __init__(self, codigo, titulo, autor, tiemp_dura, medi_tec):
            super().__init__(codigo, titulo, autor)
            self.__tiempo_de_duracion = tiemp_dura
            self.__medio_tecnologico = medi_tec

        # Método para establecer el tiempo de duración del producto grabado
        def set_tiem_dura(self, value):
            self.__tiempo_de_duracion = value

        # Método para obtener el tiempo de duración del producto grabado
        def get_tiemp_dura(self):
            return self.__tiempo_de_duracion

        # Método para establecer el medio tecnológico del producto grabado
        def set_medio_tec(self, value):
            self.__medio_tecnologico = value

        # Método para obtener el medio tecnológico del producto grabado
        def get_medio_tec(self):
            return self.__medio_tecnologico

        # Método para ingresar y mostrar información del producto grabado
        def informacion(self):
            print("CLASE PRODUCTO GRABADO" + "\n")
            pructo_grab = ProductoGrabado("", "", "", "", "")

            codigo = random.randint(101, 1000)
            while True:
                autor = str(input("Digite el autor: "))
                if autor.replace("", "").isalpha():
                    pructo_grab.set_autor(autor)
                    break
                else:
                    print("Solo puede usar caracteres alfabéticos.")
            while True:
                titulo = str(input("Digite el Título: "))
                if titulo.replace("", "").isalpha():
                    pructo_grab.set_titulo(titulo)
                    break
                else:
                    print("Solo puede usar caracteres alfabéticos.")

            pructo_grab.set_codigo(codigo)

            while True:
                try:
                    Tiempo_duracion = float(input('Digite el tiempo de duración en minutos: '))
                    pructo_grab.set_tiem_dura(Tiempo_duracion)
                    break
                except ValueError:
                    print("Solo puede digitar caracteres válidos numéricos, números")

            while True:
                Medio_tecnologico = str(input("Digite el medio tecnológico: "))
                if Medio_tecnologico.replace("", "").isalpha():
                    pructo_grab.set_medio_tec(Medio_tecnologico)
                    break
                else:
                    print("Solo puede usar caracteres alfabéticos.")

            print("""
                 __________________________________
                |       PRODUCTO GRABADO           |
                |__________________________________|
                |Autor: {0}                       {5}
                |                                  |
                |Título: {1}                      {5}
                |                                  |  
                |Código: {2}                       |
                |                                  |
                |Tiempo de duración: {3} minutos  {5}
                |                                  |   
                |                                  |
                |Medio tecnológico: {4}           {5}
                |__________________________________|
                """.format(pructo_grab.get_autor(), pructo_grab.get_titulo(), pructo_grab.get_codigo(), pructo_grab.get_tiemp_dura(), pructo_grab.get_medio_tec(),'|'))

    # Clase que representa un producto de software
    class ProductoSoftware(Producto):
        def __init__(self, codigo, titulo, autor, version, sis_opera):
            super().__init__(codigo, titulo, autor)
            self.__version = version
            self.__sistema_operativo = sis_opera

        # Método para establecer la versión del producto de software
        def set_version(self, value):
            self.__version = value

        # Método para obtener la versión del producto de software
        def get_version(self):
            return self.__version

        # Método para establecer el sistema operativo del producto de software
        def set_sis_opera(self, value):
            self.__sistema_operativo = value

        # Método para obtener el sistema operativo del producto de software
        def get_sis_opera(self):
            return self.__sistema_operativo

        # Método para ingresar y mostrar información del producto de software
        def informacion(self):
            prod = Producto("", "", "")
            print("CLASE PRODUCTO SOFTWARE" + "\n")
            while True:
                autor = str(input("Ingrese el autor: "))
                if autor.replace("", "").isalpha():
                    prod.set_autor(autor)
                    break
                else:
                    print("Solo puede usar caracteres alfabéticos.")
            while True:
                titulo = str(input("Ingrese el título: "))
                if titulo.replace("", "").isalpha():
                    prod.set_titulo(titulo)
                    break
                else:
                    print("Solo puede usar caracteres alfabéticos.")

            prod_softw = ProductoSoftware("", "", "", "", "")
            while True:
                try:
                    version = float(input("Ingrese la versión del programa: "))
                    prod_softw.set_version(version)
                    break
                except ValueError:
                    print("Solo puede digitar caracteres válidos numéricos, números")

            while True:
                sistem_opera = str(input("Ingrese el sistema operativo: "))
                if sistem_opera.replace("", "").isalpha():
                    prod_softw.set_sis_opera(sistem_opera)
                    break
                else:
                    print("Solo puede usar caracteres alfabéticos.")

            codigo = random.randint(101, 1000)
            prod_softw.set_codigo(codigo)
           

            print("""
                 _____________________________ 
                |       💻 PRODUCTO 💻        |
                |_____________________________|     
                {5} Autor: {0:<8}             {5}                  
                |_____________________________|
                {5} Titulo: {1}              {5}
                |_____________________________|
                |Codigo: {2}                  |
                |_____________________________|
                {5} Version: {3:<3}               {5}   
                |_____________________________|
                {5} Sistema Operativo: {4}  {5} 
                |_____________________________|
                  """.format(prod.get_autor(), prod.get_titulo(),prod_softw.get_codigo(), prod_softw.get_version(), prod_softw.get_sis_opera(),'|'))
    class ProductoImpreso(Producto):
        def __init__(self, codigo, titulo, autor, editorial, año, presio):
            super().__init__(codigo, titulo, autor)
            self.__editorial = editorial
            self.__año = año
            self.__precio = presio

        def set_editorial(self, value):
            self.__editorial = value

        def get_editorial(self):
            return self.__editorial
        
        def set_año(self, value):
            self.__año = value

        def get_año(self):
            return self.__año
        
        def set_precio(self, value):
            self.__precio = value

        def get_precio(self):
            return self.__precio
    
        def informacion(self):
            prod = Producto("","","")
            while True:
                autor = str(input("Ingrese el autor: "))
                if autor.replace("", "").isalpha():
                    prod.set_autor(autor)
                    break
            while True:
                titulo = str(input("Ingrese el titulo: "))
                if titulo.replace("", "").isalpha():
                    prod.set_titulo(titulo)
                    break
                else:
                    print("Solo puede usar caracteres alfabéticos.")

            prod_impre = ProductoImpreso("","","","","","")
            codigo = random.randint(101, 1000)

            prod_impre.set_codigo(codigo)
            while True:
                try:
                    precio = float(input("Ingrese el presio del producto: "))
                    prod_impre.set_precio(precio)
                    break
                except ValueError:
                    print("Solo puede digitar caracteres validos numericos, numeros")
            while True:     
                editoria = str(input("ingrese la editorial del producto: "))
                if editoria.replace("", "").isalpha():
                    prod_impre.set_editorial(editoria)
                    break
                else:
                    print("Solo puede usar caracteres alfabéticos.")
            while True:
                try:        
                    fecha_año_str = input("Ingrese la fecha de creacion del producto (YYYY-MM-DD): ")
                    fecha_año = datetime.strptime(fecha_año_str, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Solo puede digitar una fecha valida")
            
           
            print("""
                    Autor: {0}
                    Titulo: {1}
                    Codigo: {2}
                    Precio: {3}
                    Año: {4}
                  """.format(prod.get_autor(),prod.get_titulo(),prod_impre.get_codigo(), prod_impre.get_precio(),fecha_año.strftime('%Y-%m-%d')))
        

    class revista(ProductoImpreso):
        def __init__(self, codigo, titulo, autor, editorial, año, presio,volumen,estado):
            super().__init__(codigo, titulo, autor, editorial, año, presio)
            self.__volumen = volumen
            self.__estado = estado

        def set_volumen(self, value):
            self.__volumen = value

        def get_volumen(self):
            return self.__volumen
        
        def set_estado(self, value):
            self.__estado = value

        def get_estado(self):
            return self.__estado
            

        def  informacion(self):
            prod = Producto("","","")
            while True:
                autor = str(input("Ingrese el autor: "))
                if (autor.replace(" ","").isalpha()):
                    prod.set_autor(autor)
                    break
                else:
                    print("Ingrese solo letras")
            while True:
                try:
                    titulo = str(input("Ingrese el titulo: "))
                    prod.set_titulo(titulo)
                    break
                except ValueError:
                    print("Ingrese solo letras")

            prod_revis = revista("","","","","","","","")
            codigo = random.randint(101, 1000)
            prod_revis.set_codigo(codigo)
            estados = ["agotado", "promocion", "encargado", "2 x 1"]
            estado = random.choice(estados)
            prod_revis.set_estado(estado)
            while True:
                try:
                    volumen = int(input("Ingrese el volumen de la revista "))
                    prod_revis.set_volumen(volumen)
                    break
                except ValueError:
                    print("Ingrese un numero entero")
            while True:
                try:
                    precio = float(input("Ingrese el precio del producto: "))
                    prod_revis.set_precio(precio)
                    break
                except ValueError:
                    print("Ingrese un numero")
            while True:
                try:
                    editoria = str(input("ingrese la editorial del producto: "))
                    prod_revis.set_editorial(editoria)
                    break
                except ValueError:
                    print("Ingrese un numero entero")
            while True:
                try:
                    fecha_año_str = input("Ingrese la fecha de creacion del producto (YYYY-MM-DD): ")
                    fecha_año = datetime.strptime(fecha_año_str, "%Y-%m-%d")
                    prod_revis.set_año(fecha_año.strftime('%Y-%m-%d'))
                    break
                except ValueError:
                    print("Ingrese una fecha valida")

            osystem('cls')
            print("""
                    📖 PRODUCTO 📖       
                    
                     Autor: {0}                
                
                     Titulo: {1}                
                   
                     Codigo: {2}               
                    
                     Precio: {3}$            
                    
                     Año: {4}                   
                  
                     volumen: {5}               
                  
                     EDITORIAL: {7}
                    
                    METODO:
                     estado: {6}               
                    

                  """.format(prod.get_autor(),prod.get_titulo(),prod_revis.get_codigo(), prod_revis.get_precio(),fecha_año.strftime('%Y-%m-%d'), prod_revis.get_volumen(), prod_revis.get_estado(),prod_revis.get_editorial()))
    class libro(ProductoImpreso):
        def __init__(self, codigo, titulo, autor, editorial, año, presio, idioma, estado):
            super().__init__(codigo, titulo, autor, editorial, año, presio)
            self.__idioma = idioma
            self.__estado = estado

        def set_estado(self, value):
            self.__estado = value

        def get_estado(self):
            return self.__estado
        def set_idioma(self, value):
            self.__idioma = value
        def get_idioma(self):
            return self.__idioma
        def  informacion(self):
            prod = Producto("","","")
            while True:
                autor = str(input("Ingrese el autor: "))
                if (autor.replace(" ","").isalpha()):
                    prod.set_autor(autor)
                    break
                else:
                    print("Ingrese solo letras")
            while True:
                try:
                    titulo = str(input("Ingrese el titulo: "))
                    if titulo.replace(" ", "").isalpha():
                        prod.set_titulo(titulo)
                        break
                    else:
                        print("Ingrese solo letras")
                except ValueError:
                    print("Ingrese solo letras")
            
            prod_libro = libro("","","","","","","","")
            codigo = random.randint(101, 1000)
            prod.set_codigo(codigo)
            estados = ["agotado", "promocion", "encargado", "2 x 1"]
            estado = random.choice(estados)
            prod_libro.set_estado(estado)
            while True:
                idioma = str(input("Ingrese el idioma del libro: "))
                if idioma.replace(" ", "").isalpha():
                    prod_libro.set_idioma(idioma)
                    break
                else:
                    print("Ingrese solo letras")
            while True:
                try:
                    precio = float(input("Ingrese el precio del producto: "))
                    prod_libro.set_precio(precio)
                    break
                except ValueError:
                    print("Ingrese un numero")
            while True:
                try:
                    fecha_año_str = input("Ingrese la fecha de creacion del producto YYYY-MM-DD: ")
                    fecha_año = datetime.strptime(fecha_año_str, "%Y-%m-%d")
                    prod_libro.set_año(fecha_año.strftime('%Y-%m-%d'))
                    break
                except ValueError:
                    print("Ingrese una fecha valida")
            while True:
                try:
                    editoria = str(input("ingrese la editorial del producto: "))
                    if editoria.replace(" ","").isalpha():
                        prod_libro.set_editorial(editoria)
                        break
                    else:
                        print("Ingrese solo letras")
                except ValueError:
                    print("Ingrese texto no numeros")
            print("""
                           📕 PRODUCTO LIBRO 📕        
                     Autor: {0}                         
                    ____________________________________
                     Titulo: {1}                         
                    ____________________________________
                     Codigo: {2}                        
                    ____________________________________
                     idioma: {3}                        
                    ____________________________________
                     Editorial: {4}                     
                    ____________________________________
                     Año de publicacion : {6}           
                    ____________________________________
                     Precio: {5}$                       
                    ____________________________________
                     Estado: {7}
                  """.format(prod.get_autor(),prod.get_titulo(),prod.get_codigo(), prod_libro.get_idioma(),prod_libro.get_editorial(),prod_libro.get_precio(),fecha_año.strftime('%Y-%m-%d'),prod_libro.get_estado()))
                    

    # osystem('cls')
    # pructo_grab = ProductoGrabado("","","","","")
    # pructo_grab.informacion()
    # print("presione cualquier tecla para continuar")
    # get()

    # osystem('cls')
    # prod_soft = ProductoSoftware("","","","","")
    # prod_soft.informacion()
    # get()

    osystem("cls")
    prod_resvist = revista("","","","","","","","")
    prod_resvist.informacion()
    get()

    osystem("cls")
    prof_libro = libro("","","","","","","","")
    prof_libro.informacion()
    get()
if __name__ == '__main__':
    main()