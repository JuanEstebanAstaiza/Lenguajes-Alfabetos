import itertools


# Función recursiva para generar todas las cadenas posibles de una longitud dada
def generar_cadenas(alfabeto, longitud, cadena_actual=""):
    if len(cadena_actual) == longitud:
        return [cadena_actual]
    cadenas = []
    for letra in alfabeto:
        cadenas += generar_cadenas(alfabeto, longitud, cadena_actual + letra)
    return cadenas


# Función para verificar si una cadena pertenece al lenguaje
def pertenece_lenguaje(cadena, alfabeto, regla_inicio=None):
    for letra in cadena:
        if letra not in alfabeto:
            return False
    if regla_inicio and not cadena.startswith(regla_inicio):
        return False
    return True


# Función para generar cadenas con prefijos y sufijos específicos
def generar_cadenas_con_prefijo_sufijo(alfabeto, longitud, prefijo="", sufijo=""):
    longitud_restante = longitud - len(prefijo) - len(sufijo)
    if longitud_restante < 0:
        return []
    cadenas_centrales = generar_cadenas(alfabeto, longitud_restante)
    cadenas_resultantes = [prefijo + central + sufijo for central in cadenas_centrales]
    return cadenas_resultantes


# Función para seleccionar o crear un alfabeto
def seleccionar_alfabeto():
    alfabetos_predefinidos = {
        1: ['a', 'b', 'c', 'd', 'e'],
        2: ['x', 'y', 'z', 'w', 'v'],
        3: ['1', '2', '3', '4', '5'],
        4: ['p', 'q', 'r', 's', 't'],
        5: ['u', 'v', 'w', 'x', 'y', 'z']
    }
    print("Selecciona un alfabeto predefinido o crea uno propio:")
    for key, value in alfabetos_predefinidos.items():
        print(f"{key}. {value}")
    print("6. Crear un alfabeto personalizado")
    seleccion = int(input("Ingresa el número de tu elección: "))
    if seleccion in alfabetos_predefinidos:
        alfabeto = alfabetos_predefinidos[seleccion]
    elif seleccion == 6:
        alfabeto = list(input("Introduce tu alfabeto personalizado (separando los caracteres con espacios): ").split())
    else:
        print("Opción inválida. Se utilizará el alfabeto predefinido 1 por defecto.")
        alfabeto = alfabetos_predefinidos[1]
    return alfabeto


# Función para crear tres lenguajes a partir de un alfabeto
def crear_lenguajes(alfabeto):
    print("\nGenerando tres lenguajes diferentes con el alfabeto.")
    L1 = generar_cadenas(alfabeto, 2)
    L2 = generar_cadenas(alfabeto, 3)
    L3 = generar_cadenas(alfabeto, 1)
    print(f"Lenguaje 1 (L1): {L1}")
    print(f"Lenguaje 2 (L2): {L2}")
    print(f"Lenguaje 3 (L3): {L3}")
    return L1, L2, L3


# Funciones para operaciones sobre lenguajes
def union(L1, L2):
    return list(set(L1) | set(L2))


def concatenacion(L1, L2):
    return [a + b for a in L1 for b in L2]


def estrella(L1, max_repeticiones=3):
    resultado = L1[:]
    for i in range(2, max_repeticiones + 1):
        combinaciones = list(itertools.product(L1, repeat=i))
        resultado += [''.join(comb) for comb in combinaciones]
    return resultado


# Función para verificar si una cadena es un palíndromo
def es_palindromo(cadena):
    return cadena == cadena[::-1]


# Función para generar palíndromos a partir de un alfabeto
def generar_palindromos(alfabeto, longitud):
    palindromos = []
    for cadena in generar_cadenas(alfabeto, longitud):
        if es_palindromo(cadena):
            palindromos.append(cadena)
    return palindromos


# Función para transformar una cadena según reglas específicas
def transformar_cadena(cadena, regla):
    if regla == 1:
        # Regla de reemplazo: cambiar todas las 'a' por 'x'
        return cadena.replace('a', 'x')
    elif regla == 2:
        # Regla de inversión
        return cadena[::-1]
    else:
        return cadena


# Menú principal que contiene todas las funcionalidades
def menu():
    print("\nLaboratorio de Simulación en Python")
    alfabeto = seleccionar_alfabeto()
    print(f"\nAlfabeto seleccionado: {alfabeto}")

    while True:
        print("\n--- Menú ---")
        print("1. Generar cadenas de una longitud dada")
        print("2. Verificar si una cadena pertenece al lenguaje")
        print("3. Generar cadenas con prefijo y sufijo")
        print("4. Crear tres lenguajes y aplicar operaciones (Unión, Concatenación, Estrella)")
        print("5. Generar y verificar palíndromos")
        print("6. Transformar cadena según reglas específicas")
        print("7. Salir")

        opcion = int(input("\nSelecciona una opción: "))

        if opcion == 1:
            longitud = int(input("Introduce la longitud de las palabras a generar: "))
            cadenas = generar_cadenas(alfabeto, longitud)
            print(f"Cadenas generadas: {cadenas}")

        elif opcion == 2:
            cadena = input("Introduce una cadena para verificar si pertenece al lenguaje: ")
            regla_inicio = input("Introduce una regla para el inicio de la cadena (deja en blanco si no aplica): ")
            if pertenece_lenguaje(cadena, alfabeto, regla_inicio):
                print(f"La cadena '{cadena}' pertenece al lenguaje.")
            else:
                print(f"La cadena '{cadena}' NO pertenece al lenguaje.")

        elif opcion == 3:
            longitud = int(input("Introduce la longitud de las palabras: "))
            prefijo = input("Introduce un prefijo: ")
            sufijo = input("Introduce un sufijo: ")
            cadenas_prefijo_sufijo = generar_cadenas_con_prefijo_sufijo(alfabeto, longitud, prefijo, sufijo)
            print(f"Cadenas con prefijo y sufijo: {cadenas_prefijo_sufijo}")

        elif opcion == 4:
            L1, L2, L3 = crear_lenguajes(alfabeto)
            print("\nAplicando operaciones entre lenguajes:")
            print(f"Unión (L1 ∪ L2): {union(L1, L2)}")
            print(f"Concatenación (L1 ∘ L2): {concatenacion(L1, L2)}")
            print(f"Estrella (L1*): {estrella(L1)}")

        elif opcion == 5:
            longitud_palindromo = int(input("Introduce la longitud de los palíndromos a generar: "))
            palindromos = generar_palindromos(alfabeto, longitud_palindromo)
            print(f"Palíndromos generados: {palindromos}")
            cadena = input("Introduce una cadena para verificar si es un palíndromo: ")
            if es_palindromo(cadena):
                print(f"La cadena '{cadena}' es un palíndromo.")
            else:
                print(f"La cadena '{cadena}' NO es un palíndromo.")

        elif opcion == 6:
            cadena = input("Introduce una cadena para transformar: ")
            print("Reglas de transformación:")
            print("1. Reemplazar 'a' por 'x'")
            print("2. Invertir la cadena")
            regla = int(input("Selecciona una regla de transformación: "))
            cadena_transformada = transformar_cadena(cadena, regla)
            print(f"Cadena transformada: {cadena_transformada}")

        elif opcion == 7:
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")


# Ejecutar el menú principal
if __name__ == "__main__":
    menu()
