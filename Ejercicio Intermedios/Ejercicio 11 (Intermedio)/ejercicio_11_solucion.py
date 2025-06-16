a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
c = float(input("Ingresá el tercer número: "))

# Comparar los tres números
if a > b and a > c:
	print("El mayor es:", a)
elif b > a and b > c:
	print("El mayor es:", b)
elif c > a and c > b:
	print("El mayor es:", c)
elif a == b and a > c:
	print("El mayor es:", a, "y está repetido (a y b).")
elif a == c and a > b:
	print("El mayor es:", a, "y está repetido (a y c).")
elif b == c and b > a:
	print("El mayor es:", b, "y está repetido (b y c).")
else:
	print("Todos los números son iguales.")
