dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

# Determinamos si el año es bisiesto
es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Definimos los días por mes
if mes == 2:
	dias_mes = 29 if es_bisiesto else 28
elif mes in [4, 6, 9, 11]:
	dias_mes = 30
elif mes in [1, 3, 5, 7, 8, 10, 12]:
	dias_mes = 31
else:
	print("Mes inválido.")
	exit()

if dia == dias_mes:
	print("Es el último día del mes.")
else:
	print("No es el último día del mes.")
