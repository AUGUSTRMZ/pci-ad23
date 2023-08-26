print("Hola!!!, bienvenido a FIFOOD")
print("Porfavor, ingresa los siguientes datos")

# pedir los parametros al usuario
peso = float(input("Introduce tu peso en KG: "))
estatura = int(input("introduce tu estatura en cm ej.170: "))
if estatura > 300:
    print("esta altura es irreal porfavor ingresa datos reales")
    mensaje = "reinicia el programa para volver a introducir tus datos"
    print(mensaje)
edad = int(input("por favor introduce tu edad: "))
print("asegurate de que tus datos sean correctos")
# definir la constante
tmb = 65.5
print("Muy bien, comencemos!!!")

# definir las kcal diarias, estos calculos fueron hechos acorde a formulas que encontre en internet y otras que ya conocia
consumo_calorias = tmb+13.75*peso+5.003*estatura-6.75*edad
print(f"tus calorias a consumir son {consumo_calorias}kcal.")

# definir los macronutrientes
req_proteina = 1.6*peso
print(f"deberias consumir aprox {req_proteina}g de proteina.")

# para calcular las grasas se requieren 2 calculos para los cuales decidi divir la op en 2 para agregar mas complejidad al programa
kcal_grasas = consumo_calorias*0.25
req_grasas = kcal_grasas/9
print(f"deberias consumir aprox {req_grasas}g de grasas ")

# definimos el ultimo macronutriente que es el mas sencillo
req_carbohidratos = consumo_calorias/4
print(f" deberias consumir aprox {req_carbohidratos}g de carbohidratos")
print("gracias por usar la app")
