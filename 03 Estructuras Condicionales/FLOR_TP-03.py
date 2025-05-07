#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
MayorEdad= 18
edad= int(input("Ingrese su edad: "))

if edad >= MayorEdad:
    print ("Es mayor de edad")
    
#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
notaaprob = 6
nota = float(input ("Ingrese su nota: "))

if nota >= notaaprob:
    print ("Aprobado")
else:
    print ("Desaprobado")
    
#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
num= int(input("Ingrese un numero: "))

if num % 2 == 0:
    print ("Ha ingresado un número par")
else:
    print ("Por favor, ingrese un numero par")
    
#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.
edad1 = int(input("Ingrese su edad: "))

if edad1 < 12:
    print ("Usted es un niño/a")
elif edad1 >= 12 and edad1 < 18:
    print ("Usted es un adolescente")
elif edad1 >= 18 and edad1 < 30:
    print ("Usted es un adulto/a joven")
else:
    print ("Usted es un adulto/a")
    
#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
contraseña= input("Ingrese una contraseña ")

if 8<= len(contraseña) <=14:
    print ("Ah ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
#escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random
from statistics import mean, median, mode, StatisticsError

# Generar la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular media y mediana
media_valor = mean(numeros_aleatorios)
mediana_valor = median(numeros_aleatorios)

# Intentar calcular la moda
try:
    moda_valor = mode(numeros_aleatorios)
except StatisticsError:
    moda_valor = None

# Imprimir valores
print("Lista de números aleatorios:")
print(numeros_aleatorios)
print(f"\nMedia: {media_valor:.2f}")
print(f"Mediana: {mediana_valor:.2f}")
print(f"Moda: {moda_valor if moda_valor is not None else 'No hay una única moda'}")

# Determinar el tipo de sesgo
if moda_valor is not None:
    if media_valor > mediana_valor > moda_valor:
        print("\nSesgo positivo (asimetría a la derecha).")
    elif media_valor < mediana_valor < moda_valor:
        print("\nSesgo negativo (asimetría a la izquierda).")
    elif media_valor == mediana_valor == moda_valor:
        print("\nDistribución simétrica (sin sesgo).")
    else:
        print("\nNo se puede determinar un sesgo claro con los valores actuales.")
else:
    print("\nNo se puede determinar el sesgo porque no hay una única moda.")

#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
# Solicitar una frase o palabra al usuario
texto = input("Ingrese una frase o palabra: ")

# Verificar si termina en vocal (mayúscula o minúscula)
if texto and texto[-1].lower() in "aeiou":
    texto += "!"

# Imprimir el resultado
print("Resultado:", texto)

#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.
# Solicitar nombre al usuario
nombre = input("Ingrese su nombre: ")

# Mostrar opciones
print("\nSeleccione una opción:")
print("1. Mostrar el nombre en MAYÚSCULAS.")
print("2. Mostrar el nombre en minúsculas.")
print("3. Mostrar el nombre con la primera letra en mayúscula.")

# Solicitar opción
opcion = input("Ingrese el número de la opción (1, 2 o 3): ")

# Transformar e imprimir el nombre según la opción elegida
if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print ("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print ("Leve")
elif magnitud >= 4 and magnitud < 5:
    print ("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print ("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print ("Muy fuerte")
else:
    print ("Extremo")

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano
# Función para determinar la estación según el mes y día
def obtener_estacion(dia, mes, hemisferio):
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion_norte = "Otoño"
    else:
        return "Fecha inválida"

    if hemisferio.upper() == "N":
        return estacion_norte
    elif hemisferio.upper() == "S":
        # En el hemisferio sur las estaciones son opuestas
        estaciones_opuestas = {
            "Invierno": "Verano",
            "Primavera": "Otoño",
            "Verano": "Invierno",
            "Otoño": "Primavera"
        }
        return estaciones_opuestas[estacion_norte]
    else:
        return "Hemisferio inválido"

# Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ")
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Obtener estación
estacion = obtener_estacion(dia, mes, hemisferio)

# Mostrar resultado
print(f"La estación del año es: {estacion}")
