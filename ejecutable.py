# Función recursiva para generar todas las cadenas posibles de una longitud dada
def generar_cadenas(alfabeto, longitud, cadena_actual=""):
    # Caso base: si la cadena alcanza la longitud deseada
    if len(cadena_actual) == longitud:
        return [cadena_actual]

    # Generar nuevas cadenas agregando cada letra del alfabeto a la cadena actual
    cadenas = []
    for letra in alfabeto:
        cadenas += generar_cadenas(alfabeto, longitud, cadena_actual + letra)

    return cadenas


# Función para verificar si una cadena pertenece al lenguaje
def pertenece_lenguaje(cadena, alfabeto, regla_inicio=None):
    # Verificar si todas las letras de la cadena están en el alfabeto
    for letra in cadena:
        if letra not in alfabeto:
            return False

    # Verificar si hay una regla para el inicio de la cadena
    if regla_inicio and not cadena.startswith(regla_inicio):
        return False

    return True


# Función para generar cadenas con prefijos y/o sufijos específicos
def generar_cadenas_con_prefijo_sufijo(alfabeto, longitud, prefijo="", sufijo=""):
    longitud_restante = longitud - len(prefijo) - len(sufijo)

    # Si la longitud restante es negativa, la cadena no puede formarse
    if longitud_restante < 0:
        return []

    # Generar las posibles combinaciones para la parte central de la cadena
    cadenas_centrales = generar_cadenas(alfabeto, longitud_restante)

    # Unir el prefijo, la parte central y el sufijo
    cadenas_resultantes = [prefijo + central + sufijo for central in cadenas_centrales]

    return cadenas_resultantes


# Función para mostrar alfabetos predefinidos y permitir la creación de uno personalizado
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


# Función principal (main) que ejecuta el programa
def main():
    print("Laboratorio de Simulación en Python")

    # Seleccionar alfabeto
    alfabeto = seleccionar_alfabeto()
    print(f"\nAlfabeto seleccionado: {alfabeto}")

    # Parte A: Generar cadenas de una longitud dada con un alfabeto
    longitud_palabra = int(input("\nIntroduce la longitud de las palabras a generar: "))
    print("\nGenerando todas las cadenas posibles...")
    cadenas = generar_cadenas(alfabeto, longitud_palabra)
    print(cadenas)

    # Parte B: Verificar si una cadena pertenece al lenguaje
    cadena = input("\nIntroduce una cadena para verificar si pertenece al lenguaje: ")
    regla_inicio = input("Introduce una regla para el inicio de la cadena (deja en blanco si no aplica): ")
    if pertenece_lenguaje(cadena, alfabeto, regla_inicio):
        print(f"La cadena '{cadena}' pertenece al lenguaje.")
    else:
        print(f"La cadena '{cadena}' NO pertenece al lenguaje.")

    # Parte C: Generar cadenas con prefijos y sufijos específicos
    prefijo = input("\nIntroduce un prefijo para generar las cadenas: ")
    sufijo = input("Introduce un sufijo para generar las cadenas: ")
    print("\nGenerando cadenas con prefijo y sufijo...")
    cadenas_con_prefijo_sufijo = generar_cadenas_con_prefijo_sufijo(alfabeto, longitud_palabra, prefijo, sufijo)
    print(cadenas_con_prefijo_sufijo)


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
