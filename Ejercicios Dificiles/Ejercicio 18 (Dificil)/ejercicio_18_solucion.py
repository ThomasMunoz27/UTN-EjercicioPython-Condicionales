a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

# Validamos si forman un triángulo
if a + b > c and a + c > b and b + c > a:
	print("Forman un triángulo.")

	# Buscamos si es un triángulo rectángulo
	# a^2 + b^2 == c^2 (o cualquier combinación)
	if round(a**2 + b**2, 5) == round(c**2, 5) or \
	   round(a**2 + c**2, 5) == round(b**2, 5) or \
	   round(b**2 + c**2, 5) == round(a**2, 5):
		print("Además, es un triángulo rectángulo.")
	else:
		print("Pero no es un triángulo rectángulo.")
else:
	print("No forman un triángulo.")
