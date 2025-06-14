def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def ejecutar_factoriales():
    limite = int(input("Ingrese un número entero positivo: "))
    for i in range(1, limite + 1):
        print(f"Factorial de {i} es {factorial(i)}")

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def ejecutar_fibonacci():
    posicion = int(input("Ingrese hasta qué posición quiere ver la serie de Fibonacci: "))
    print("Serie de Fibonacci:")
    for i in range(posicion + 1):
        print(fibonacci(i), end=" ")
    print()

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def ejecutar_potencia():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    print(f"{base}^{exponente} = {potencia(base, exponente)}")

def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

def ejecutar_binario():
    numero = int(input("Ingrese un número decimal positivo: "))
    resultado = decimal_a_binario(numero)
    print(f"Binario: {resultado if resultado else '0'}")

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def ejecutar_palindromo():
    texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
    print("¿Es palíndromo?", es_palindromo(texto))

def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

def ejecutar_suma_digitos():
    numero = int(input("Ingrese un número para sumar sus dígitos: "))
    print(f"La suma de los dígitos es: {suma_digitos(numero)}")

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

def ejecutar_piramide():
    nivel = int(input("Ingrese el número de bloques en el nivel más bajo: "))
    print(f"Total de bloques necesarios: {contar_bloques(nivel)}")

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)

def ejecutar_contar_digito():
    numero = int(input("Ingrese un número: "))
    digito = int(input("Ingrese el dígito que desea contar (0-9): "))
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")

# Menú de selección
def menu():
    while True:
        print("\n--- MENÚ DE FUNCIONES RECURSIVAS ---")
        print("1. Factorial de 1 a N")
        print("2. Serie Fibonacci hasta N")
        print("3. Potencia (n^m)")
        print("4. Convertir decimal a binario")
        print("5. Verificar si palabra es palíndromo")
        print("6. Sumar dígitos de un número")
        print("7. Contar bloques de una pirámide")
        print("8. Contar cuántas veces aparece un dígito")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_factoriales()
        elif opcion == "2":
            ejecutar_fibonacci()
        elif opcion == "3":
            ejecutar_potencia()
        elif opcion == "4":
            ejecutar_binario()
        elif opcion == "5":
            ejecutar_palindromo()
        elif opcion == "6":
            ejecutar_suma_digitos()
        elif opcion == "7":
            ejecutar_piramide()
        elif opcion == "8":
            ejecutar_contar_digito()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar menú
menu()
