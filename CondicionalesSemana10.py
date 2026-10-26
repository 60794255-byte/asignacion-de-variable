# HACIENDO USO DE LAS RESPUESTAS
# nm_leones = 15
# nm_tigres = 10
# Respuesta = nm_leones >= nm_tigres
# print(Respuesta)

# # LAB   Variables ‒ Preguntas y Respuestas
# n = int(input("Ingrese un número:"))
# print(n >=100)

# Condiciones y ejecución condicional
# Ejecución condicional: la sentencia 
Contador = 122
if Contador >= 120:
    print("Dormir y Soñar")
    
Contador = 150
if Contador >=120:
    print("Preparar la cama")
    print("Tomar una ducha")
    print("Dormir y soñar ")
print("Alimentar perros y ovejas")

clima = 39
if clima < 20:
    print("Salir al parque")
else:
    print("Quedarce en casa sombreado")
    
print("Tomar el almuerzo")

# Sentencias if-else anidadas
Calificacion_restaurant = 5
Cantidad_boletos = 0
clima = float(input("Ingreseel clima actual en Grados Celsius;    "))
print("El clima actual es: ", clima, "C°")
if clima > 20:
    print("Salir al parque")
    if Calificacion_restaurant >= 8:
        print("Almorzaremos")
    else:
        print("Comeremos Sandwitch")
else:
    print("Iremos al cine")
    if Cantidad_boletos > 0:
        print("Veremos una pelicula")
    else:
        print("Iremos de Shoping a Real Plaza")
            