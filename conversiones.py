valor = float(input("Ingresa la cantidad de metros a convertir: "))

print("""
 \nSelecciona una de las siguientes opciones
 -------------------------------------------
 1) Convertir a pies
 2) Convertir a pulgadas
 3) Convertir a yardas
--------------------------------------------
      """)

selec = int(input("Selecciona una opción: "))
if selec == 1:
    valor2 = valor * 3.28084
    print("En ", valor ," metros, hay ",  valor2," pies")
elif selec == 2:
    valor2 = valor * 39.3701
    print("En ", valor ," metros, hay ",  valor2," pulgadas")
elif selec == 3:
    valor2 = valor * 1.09361
    print("En ", valor ," metros, hay ", valor2," yardas")
else:
    print("Opción inexistente")
