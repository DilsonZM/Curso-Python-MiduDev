# Ejercicios de repaso - Curso Python MiduDev (01_basic)

# Nivel 1 – Repaso básico

# 1. Casting y tipos
# Convierte edad_str a entero y muestra el doble de su valor.
edad_str = "26"
edad_entero = int(edad_str)
print(f"El doble de la edad es: {edad_entero * 2}")

# Convierte numero_decimal a string y muestra su tipo.
numero_decimal = 3.1416
numero_decimal_str = str(numero_decimal)
print(f"El número decimal como string es: {numero_decimal_str} y su tipo es: {type(numero_decimal_str)}")

# 2. Uso de print()
# Crea variables nombre y edad y muestra una frase con f-string.
# Muestra también la suma de 5 y 3.

nombre = "Dilson"
edad = 30
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")
print(f"La suma de 5 y 3 es: {5 + 3}")


# 3. Tipos y variables
# Crea variables precio (float), producto (string) y disponible (boolean).
# Muestra el tipo de cada variable.

precio = 19.99
producto = "Camiseta"
disponible = True
print(f"El tipo de la variable precio es: {type(precio)}")
print(f"El tipo de la variable producto es: {type(producto)}")
print(f"El tipo de la variable disponible es: {type(disponible)}")


# Nivel 2 – Variables + input

# 4. Pedir datos al usuario
# Pregunta el nombre y la edad, y muestra un mensaje con la edad que tendrá el próximo año.

nombre_usuario = input("¿Cuál es tu nombre? ")
edad_usuario = int(input("¿Cuál es tu edad? "))
edad_proximo_año = edad_usuario + 1
print(f"Hola {nombre_usuario}, el próximo año tendrás {edad_proximo_año} años.")

# 5. Mini calculadora
# Pide dos números y muestra:
# Suma, resta, multiplicación y división (2 decimales).

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2 if numero2 != 0 else "Error: División por cero"    


# Nivel 3 – Reto final

# 6. Conversor de temperatura
# Pide una temperatura en °C y conviértela a °F.

temperatura_celsius = float(input("Introduce la temperatura en °C: "))
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
print(f"La temperatura en °F es: {temperatura_fahrenheit:.2f}°F")   

# 7. Adivina el número
# Guarda un número secreto y pide al usuario adivinarlo.
# Si acierta, muestra mensaje de éxito; si no, mensaje de error.
numero_secreto = 7
numero_adivinado = int(input("Adivina el número secreto (entre 1 y 10): "))
if numero_adivinado == numero_secreto:
    print("¡Felicidades! Has adivinado el número secreto.")
else:
    print("Lo siento, no has adivinado el número secreto. Inténtalo de nuevo.")

# 8. Conversor de divisas
# Pide una cantidad en euros y conviértela a dólares (1 euro = 1.1 dólares).
cantidad_euros = float(input("Introduce la cantidad en euros: "))
cantidad_dolares = cantidad_euros * 1.1
print(f"La cantidad en dólares es: {cantidad_dolares:.2f} $")
