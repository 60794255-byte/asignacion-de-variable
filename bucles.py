#bucle infinito
while True:
    print("Estoy atrapado dentro de un bucle.")

tamanio_numero = -999999999

numero = int(input("Ingrese un número o escribe -1 para detener:"))
while numero != -1:
    if numero > tamanio_numero:
        tamanio_numero = numero
    numero = int(input("Ingrese un número o escribe -1 para detener:"))

print("El número más grande es: ", tamanio_numero)


odd_numero = 0
even_numbero = 0

numero = int(input("Ingrese un número o escribe -1 para detener:"))
while numero != 0:
    #verificar si el número es impar
    if numero % 2 == 1:
        #incrementar el contador de números impares
        odd_numero += 1
    else:
        #incrementar el contador de números pares
        even_numbero += 1
    numero = int(input("Ingrese un número o escribe 0 para detener:"))

print("conteo de números impares: ", odd_numero)
print("Conteo de números pares: ", even_numbero)    

contador = 5
while contador != 0:
    print("Dentro del bucle.", contador)
    contador -= 1
print("Fuera del bucle.", contador)


numero_secreto = 7

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

numero = int(input("ingrea el numero: "))
while numero != numero_secreto:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero = int(input("Ingrese un numero nuevamente: "))

print("el número secreto es:", numero_secreto," ¡Bien hecho, muggle! Eres libre ahora.")    




