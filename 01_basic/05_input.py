#input forma de pedir datos al usuario
print("Input en Python")
nombre = input("¿Cual es tu nombre?: ")  # El texto dentro del input
# es el mensaje que se muestra al usuario
print("Hola", nombre)   

edad = input("¿Cual es tu edad?: ")
print("Tu edad es", edad)

print(f"Dentro de 20 años tendras {int(edad) + 20 } años")  # Convertimos la edad a entero para sumar 20

print("Obtener miltibles inputs a la vez") 

Ciudad, pais = input("¿En que ciudad y pais vives? (separados por coma): ").split(",")
print(f"Vives en el pueblo de {Ciudad.strip()} en el pais {pais.strip()}")  # Usamos strip() para eliminar espacios en blanco