# Primer intento
usuario = input("Usuario: ")
clave = input("Contraseña: ")

if usuario == "admin" and clave == "1234":
	print("Acceso concedido.")
else:
	print("Credenciales incorrectas. Intentá nuevamente.")

	# Segundo intento
	usuario = input("Usuario: ")
	clave = input("Contraseña: ")

	if usuario == "admin" and clave == "1234":
		print("Acceso concedido.")
	else:
		print("Acceso denegado.")
