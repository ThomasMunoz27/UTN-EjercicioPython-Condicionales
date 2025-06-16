a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

# Primero, verificar si los lados forman un triángulo válido
if a + b > c and a + c > b and b + c > a:
	# Ahora clasificamos el tipo de triángulo
	if a == b == c:
		print("Es un triángulo equilátero.")
	elif a == b or a == c or b == c:
		print("Es un triángulo isósceles.")
	else:
		print("Es un triángulo escaleno.")
else:
	print("Los lados no forman un triángulo válido.")
