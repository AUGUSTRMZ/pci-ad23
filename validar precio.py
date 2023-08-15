# float lo convierte en un numero decimal
precio = float(input("introduce precio: "))
mensaje = ""  # se puede introducir una variable vacia para usarlo en lugar de print
print(f"precio: ${precio}")
if precio < 0:
    print("el precio no es valido")
    mensaje = "el precio no es valido"
else:
    print("el precio es valido")
    mensaje = "el precio es valido"
print(mensaje)
print("fin de la operacion")
