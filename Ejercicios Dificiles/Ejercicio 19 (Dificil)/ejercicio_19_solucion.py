numero = input("Ingresá un número de 3 cifras: ")

if len(numero) == 3 and numero.isdigit():
	if numero == numero[::-1]:
		print("Es un número capicúa.")
	else:
		print("No es capicúa.")
else:
	print("Entrada inválida. Ingresá un número de 3 cifras.")
