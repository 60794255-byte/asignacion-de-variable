# Ejemplo 1:
numero1 = int(input("Ingresar el primer número"))
numero2 = int(input("Ingresar el segundo número"))

# Sentencia if
# Elige el número más grande
if numero1 > numero2:
    tamaño_numero = numero1
else:
    tamaño_numero = numero2

# Mostramos el resultado
print("El número más grande es: ", tamaño_numero)



# Ejemplo 1:
numero1 = int(input("Ingresar el primer número"))
numero2 = int(input("Ingresar el segundo número"))
# Sentencia if
# Elige el número más grande
if numero1 > numero2:tamaño_numero = numero1
else:tamaño_numero = numero2
# Mostramos el resultado
print("El número más grande es: ", tamaño_numero)



# Se leen tres números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Asumir temporalmente que numero1 es el mayor
tamano_numero = numero1
if numero2 > tamano_numero:
    tamano_numero = numero2

if numero3 > tamano_numero:
    tamano_numero = numero3



    print("El número más grande es: ", tamano_numero)

planta = input("Ingrese nombre de la planta:")

if planta == "Espatifilo":
    print("¡Espatifilo es la mejor planta de todas!")
    exit()
if planta == "ESPATIFILO":
    print("Si - ¡El Espatifilo! es la mejor planta de todos")
    exit()
if planta == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
    exit()
else:
    print("¡Espatifilo!, ¡No ", planta, "!")

