import math

# 1. Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Función que devuelve un saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Función que muestra información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4. Funciones que calculan área y perímetro de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Función que convierte segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Función que imprime la tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Función que devuelve una tupla con las operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Infinito"
    return (suma, resta, multiplicacion, division)

# 8. Función que calcula el índice de masa corporal (IMC)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Función que convierte Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# 10. Función que calcula el promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# ===============================
# PROGRAMA PRINCIPAL
# ===============================

# 1
imprimir_hola_mundo()

# 2
nombre = input("\nIngresá tu nombre: ")
print(saludar_usuario(nombre))

# 3
nombre = input("\nNombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4
radio = float(input("\nIngresá el radio de un círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")

# 5
segundos = int(input("\nIngresá la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"Equivale a {horas:.2f} horas")

# 6
numero = int(input("\nIngresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# 7
a = float(input("\nPrimer número: "))
b = float(input("Segundo número: "))
suma, resta, mult, div = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")

# 8
peso = float(input("\nIngresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

# 9
celsius = float(input("\nIngresá la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"Equivale a {fahrenheit:.2f}°F")

# 10
n1 = float(input("\nPrimer número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Tercer número: "))
promedio = calcular_promedio(n1, n2, n3)
print(f"El promedio es: {promedio:.2f}")
