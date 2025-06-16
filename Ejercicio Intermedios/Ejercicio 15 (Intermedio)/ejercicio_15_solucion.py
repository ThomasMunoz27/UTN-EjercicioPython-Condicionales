hora_str = input("Ingresá la hora en formato HH:MM: ")

# Dividimos la cadena en horas y minutos
try:
	hora, minuto = map(int, hora_str.split(":"))

	if 0 <= hora <= 23 and 0 <= minuto <= 59:
		# Clasificamos según el rango horario
		if 6 <= hora <= 11:
			print("Es de mañana.")
		elif 12 <= hora <= 19:
			print("Es de tarde.")
		else:
			print("Es de noche.")
	else:
		print("Hora o minuto fuera de rango.")
except ValueError:
	print("Formato inválido. Usá HH:MM.")
