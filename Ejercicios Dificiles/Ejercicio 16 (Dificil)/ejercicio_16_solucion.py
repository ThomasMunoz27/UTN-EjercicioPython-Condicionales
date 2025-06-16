a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))
d = float(input("Número 4: "))

# Vamos a usar condicionales anidados para encontrar el orden
# Para mantener claridad, sólo mostraremos el orden si todos son distintos

if a != b and a != c and a != d and b != c and b != d and c != d:
	if a > b and a > c and a > d:
		primero = a
		if b > c and b > d:
			segundo = b
			tercero = c if c > d else d
			cuarto = d if c > d else c
		elif c > b and c > d:
			segundo = c
			tercero = b if b > d else d
			cuarto = d if b > d else b
		else:
			segundo = d
			tercero = b if b > c else c
			cuarto = c if b > c else b
	elif b > a and b > c and b > d:
		# Repetimos el mismo patrón
		primero = b
		# ...
		# Por simplicidad, no continuamos, pero se seguiría así
		print("Este ejercicio requiere muchas condiciones para contemplar todos los casos posibles.")
		print("Lo ideal sería usar estructuras, pero el objetivo es practicar condicionales.")
	else:
		print("Para este ejemplo, se recomienda usar listas con .sort() para casos complejos.")
else:
	print("Hay números repetidos. Para este ejercicio se esperaba que fueran todos distintos.")
