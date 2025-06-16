dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

# Definimos la cantidad de días por mes
dias_por_mes = {
	1: 31, 2: 28, 3: 31, 4: 30,
	5: 31, 6: 30, 7: 31, 8: 31,
	9: 30, 10: 31, 11: 30, 12: 31
}

# Validamos que el mes esté entre 1 y 12
if mes in dias_por_mes:
	# Verificamos que el día sea válido para ese mes
	if 1 <= dia <= dias_por_mes[mes]:
		print("La fecha es válida.")
	else:
		print("El día no es válido para ese mes.")
else:
	print("Mes inválido.")
