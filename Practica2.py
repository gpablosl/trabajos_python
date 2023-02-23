#Funciones
#Crear una rutina, que mediante una función nos indique cual es el número mayor

def comparar(n1, n2):
    if n1 < n2:
        print (n2)
    elif n2 < n1:
        print (n1)
    else:
        print("son iguales")

comparar(8,9)

def compararTres(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    elif n3 > n1 and n3 > n2:
        print(n3)
    else:
        print("Son iguales")

compararTres(6,5,8)

#Funcion que calcule la longitud de una lista o una cadena
def largo(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont
print(largo("murcielago"))
print(largo([1,2,3,4,9,9]))

#Función que nos indique True si encuentra una vocal
def es_vocal(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    elif x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
    else:
        return False

print(es_vocal("o"))