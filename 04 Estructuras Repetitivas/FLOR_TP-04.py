#Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for num in range (101):
    print (num)
    
#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de digitos que contiene.

numero = int(input("Ingresa un numero entero: "))
cont = 0
if numero == 0:
    cont = 1
else:
    while numero > 0:
        numero = (numero//10)
        cont += 1

print ("El numero tiene", cont , "digitos")

#Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

# Solicita los dos valores al usuario
inicio = int(input("Introduce el primer número: "))
fin = int(input("Introduce el segundo número: "))

# Asegura que inicio sea menor que fin
if inicio > fin:
    inicio, fin = fin, inicio

# Suma los números entre inicio y fin, excluyendo ambos
suma = 0
for numero in range(inicio + 1, fin):
    suma += numero

# Muestra el resultado
print(f"La suma de los números entre {inicio} y {fin} (excluyéndolos) es: {suma}")

#Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

total_acumulado = 0

# Usamos un bucle infinito controlado internamente sin break
inicio = fin = 1  # valores iniciales no cero

while inicio != 0 and fin != 0:
    print("Introduce dos números (0 para salir):")
    inicio = int(input("Primer número: "))
    if inicio == 0:
        continue  # salta la iteración, evita pedir el segundo número innecesariamente

    fin = int(input("Segundo número: "))
    if fin == 0:
        continue  # lo mismo aquí, se verifica antes de hacer la suma

    # Asegurar el orden
    if inicio > fin:
        temp = inicio
        inicio = fin
        fin = temp

    # Suma de los números entre inicio y fin (excluyéndolos)
    suma = 0
    numero = inicio + 1
    while numero < fin:
        suma += numero
        numero += 1

    print(f"Suma parcial entre {inicio} y {fin} (excluidos): {suma}")
    total_acumulado += suma

# Muestra el resultado final
print(f"\nTotal acumulado de todas las sumas: {total_acumulado}")

#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

# Generar número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)
intentos = 0
acertado = False

print("Adivina el número entre 0 y 9.")

# Bucle que sigue pidiendo intentos hasta que el usuario acierte
while acertado == False:
    intento = input("Introduce tu intento: ")

    # Verificar que el intento sea un número válido
    if intento.isdigit():  # Solo se acepta entrada numérica
        intento = int(intento)
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Correcto! Adivinaste el número en {intentos} intento(s).")
            acertado = True  # Salir del bucle porque se adivinó el número
        else:
            print("Incorrecto, intenta de nuevo.")  # Aquí debería imprimir cuando el intento es incorrecto
    else:
        print("Por favor, introduce un número válido.")
        
#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

# Imprimir los números pares entre 0 y 100 en orden decreciente
for i in range(100, -1, -2):
    print(i)

#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

# Solicitar al usuario un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Comprobar que el número es positivo
if n > 0:
    suma = 0
    # Usar un bucle para sumar los números del 0 hasta n
    for i in range(n + 1):
        suma += i
    print(f"La suma de los números entre 0 y {n} es: {suma}")
else:
    print("Por favor, introduce un número entero positivo.")

#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos.

# Inicializar contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Pedir 100 números al usuario
for i in range(1, 101):
    num = int(input(f"Introduce el número {i}: "))
    
    # Contar pares e impares
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Contar positivos y negativos
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    # El 0 no cuenta como positivo ni negativo

# Mostrar resultados
print("\nResumen:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores

# Inicializar la suma
suma = 0

# Pedir 100 números al usuario
for i in range(1, 101):
    num = int(input(f"Introduce el número {i}: "))
    suma += num  # Acumular la suma

# Calcular la media
media = suma / 100

# Mostrar el resultado
print(f"\nLa media de los 100 números ingresados es: {media}")

#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Solicitar un número al usuario
numero = input("Introduce un número: ")

# Invertir el número usando slicing
numero_invertido = numero[::-1]

# Mostrar el número invertido
print(f"El número invertido es: {numero_invertido}")


    

