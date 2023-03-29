#Germán Pablos León
#199137

print("Alquiler de peliculas")

def mostrar_categorias():
    print("Tipos de películas:")
    print("1. Acción")
    print("2. Comedia")
    print("3. Drama")
    print("4. Ciencia Ficción")
    print("5. Terror")
    print("6. Infantil")
    print("7. Animación")
    print("8. Documental")
    print("9. Romance")
    print("10. Aventura")


def mostrar_peliculas_accion():
    print("Películas:")
    print("#11. John Wick 4 - $25 por día")
    print("#12. Top Fun Maverick - $31 por día")

def mostrar_peliculas_comedia():
    print("Películas:")
    print("#21. 21 Jump Street - $23 por día")
    print("#22. Super Bad - $27 por día")

def mostrar_peliculas_drama():
    print("Películas:")
    print("#31. Creed III - $19 por día")
    print("#32. Joker - $17 por día")

def mostrar_peliculas_ciencia_ficcion():
    print("Películas:")
    print("#41. Dune - $29 por día")
    print("#42. Arrival - $26 por día")

def mostrar_peliculas_terror():
    print("Películas:")
    print("#51. It - $32 por día")
    print("#52. The vvitch - $29 por día")

def mostrar_peliculas_infantil():
    print("Películas:")
    print("#61. Encanto - $18 por día")
    print("#62. Klaus - $35 por día")

def mostrar_peliculas_animacion():
    print("Películas:")
    print("#71. Spiderman: Into de Spiderverse - $28 por día")
    print("#72. Walle - $25 por día")

def mostrar_peliculas_documental():
    print("Películas:")
    print("#81. The Thin Blue Line - $28 por día")
    print("#82. Searching For Sugar Man - $34 por día")

def mostrar_peliculas_romance():
    print("Películas:")
    print("#91. La La Land - $26 por día")
    print("#92. In The Shape Of Water - $35 por día")

def mostrar_peliculas_aventura():
    print("Películas:")
    print("#101. Avatar 2 - $27 por día")
    print("#102. Puss In Boots: The Last Wish - $36 por día")

def seleccionar_categoria():
    codigo_categoria = int(input("Introduzca el código de la categoría de la película que desea alquilar: "))
    if codigo_categoria == 1:
        mostrar_peliculas_accion()
    elif codigo_categoria == 2:
        mostrar_peliculas_comedia()
    elif codigo_categoria == 3:
        mostrar_peliculas_drama()
    elif codigo_categoria == 4:
        mostrar_peliculas_ciencia_ficcion()
    elif codigo_categoria == 5:
        mostrar_peliculas_terror()
    elif codigo_categoria == 6:
        mostrar_peliculas_infantil()
    elif codigo_categoria == 7:
        mostrar_peliculas_animacion()
    elif codigo_categoria == 8:
        mostrar_peliculas_documental()
    elif codigo_categoria == 9:
        mostrar_peliculas_romance()
    elif codigo_categoria == 10:
       mostrar_peliculas_aventura()
    else:
        print("Código de categoría inválido")
        return 0

def seleccionar_pelicula():
    codigo = int(input("Introduzca el código de la película que desea alquilar: "))
    dias = int(input("Introduzca el número de días que desea alquilar la película: "))
    if codigo == 11:
        costo = 25
    elif codigo == 12:
        costo = 31
    elif codigo == 21:
        costo = 23
    elif codigo == 22:
        costo = 27
    elif codigo == 31:
        costo = 19
    elif codigo == 32:
        costo = 17
    elif codigo == 41:
        costo = 29
    elif codigo == 42:
        costo = 26
    elif codigo == 51:
        costo = 32
    elif codigo == 52:
        costo = 29
    elif codigo == 61:
        costo = 18
    elif codigo == 62:
        costo = 35
    elif codigo == 71:
        costo = 28
    elif codigo == 72:
        costo = 25
    elif codigo == 81:
        costo = 28
    elif codigo == 82:
        costo = 34
    elif codigo == 91:
        costo = 26
    elif codigo == 92:
        costo = 35
    elif codigo == 101:
        costo = 27
    elif codigo == 102:
        costo = 36
    else:
        print("Código de pelicula inválido")
        return 0
    total = costo * dias
    print("El total a pagar es de $" + str(total))

mostrar_categorias()
seleccionar_categoria()
seleccionar_pelicula()
