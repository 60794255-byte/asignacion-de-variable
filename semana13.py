# # break - ejemplo

# print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")
# ejemplo de continue 2
largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

# El bucle while y el bloque else
# ejemplo 1
i = 1                    # el valor inicial de i es 1
while i < 5:             # mientras i sea menor que 5
    print(i)             # se imprime el valor de i
    i += 1               # se incrementa el valor de i en 1
else:                    # de lo contrario, si i no es menor que 5
    print("else:", i)    # se imprime el valor de i
# ejemplo 2
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

# ejemplo 3
for i in range(5):
    print(i)
else:
    print("else:", i)

    # ejemplo 4
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)

# Fundamentos del bucle while


bloques = int(input("Ingrese la cantidad de bloques: "))

altura = 0
bloques_capa = 1

while bloques >= bloques_capa:
    bloques -= bloques_capa
    altura += 1
    bloques_capa += 1

print("La altura de la pirámide es:", altura)