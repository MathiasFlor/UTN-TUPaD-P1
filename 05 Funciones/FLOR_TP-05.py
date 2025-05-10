#Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.

lista_elementos = [True, 10, 80.2, "UTN", ["Hola mundo"]]
lista_elementos_pen = (lista_elementos[-2])
print (lista_elementos_pen)

#Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.

lista_vacia = []
lista_vacia.append ("Mathias")
lista_vacia.append ("Jesus")
lista_vacia.append ("Flor")
print (lista_vacia)
       
#Remplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = ("loro")
animales[3] = ("oso")
print (animales)

#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros)) #Lo que hace la funcion remove max es que elimina el numero mas grande que esta dentro de la lista
print (numeros)

#Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

lista_30 = list(range(10,31,5))
print (lista_30[0:2])

#Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["toyota", 9]
print (autos)

#Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

compras[2].append ("jugo")
compras[1][1]= ("tallarines")
compras[0].remove("pan")
print (compras)

#Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]

print(lista_anidada)
