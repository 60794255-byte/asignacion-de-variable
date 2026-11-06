#LAB   Fundamentos de la sentencia if-else
#LAB CALCULO DE IMPUESTO
ingreso = float(input("Introduce el ingreso anual: "))
lim_ingreso= 85528
igv_fijado = 0.18
if ingreso < lim_ingreso:
	igv = ingreso * igv_fijado - 556.02
else:
    igv = 14839.02
    igv = igv + 0.32 * (ingreso -lim_ingreso)
if igv < 0 :
    igv = 0
igv = round(igv,0)
print("El impuesto es:", igv, "pesos")

#LAB AÑO BISIESTO



anio = int(input("Introduce un año: "))

if anio < 1582:
	print("No esta dentro del período del calendario Gregoriano")
elif anio % 4 != 0 :
    print(anio," es ","Año comun")
elif 0 != anio /100:
    print(anio," es ","Año biciesto")
elif 0 != anio /400:
    print(anio," es ","Año Comun")
else:
    print(anio," es ","Año Bisiesto")