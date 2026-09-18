print("dime lo que sea:")
lo_que_sea = input()
print("Hm... ", lo_que_sea, "... ¿en serio? ")
#la funcion input() con un argumento 
lo_que_sea = input("dime lo q sea:")
print("Hm... ", lo_que_sea, "... ¿en serio? ")
numero = int(input("Ingresa un número:"))
resultado = numero ** 2.0
print(numero, "al cuadrado es", resultado)
#calcular hipotenusa

leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)

#operadores cadena
text1 = "samuel"
text2 = "arnol"
print(text1 * text2)

fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")


