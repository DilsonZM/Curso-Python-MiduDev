###
# Sentencias condicionales if, elif e else
# Permiten ejecutar bloques de código basados en múltiples condiciones
###

# Ejemplo de uso de if, elif y else para clasificar la edad

print("Clasificador de etapas de la vida por edad")

edad_str = input("Por favor, introduce tu edad: ")

# Es importante validar que el usuario introdujo un número
try:
    edad = int(edad_str)

    if edad < 0:
        print("La edad no puede ser un número negativo.")
    elif edad <= 12:
        print("Eres un niño/a.")
    elif edad <= 17:
        print("Eres un adolescente.")
    elif edad <= 64:
        print("Eres un adulto.")
    else: # Si no es ninguna de las anteriores, es mayor de 64
        print("Eres un adulto mayor.")

except ValueError:
    print(f"Error: '{edad_str}' no es un número válido. Por favor, introduce solo números.")

