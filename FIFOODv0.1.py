# Listas de alimentos para desayuno, comida y cena
desayuno = ["2 Huevos", "40g Avena", "250ml Leche", " 2 Frutas"]
comida = ["200g Pollo", "150g Arroz", "200g Brócoli"]
cena = ["150g Pescado", "100g Quinua",
        "150g Espinacas", "10ml Aceite de oliva"]
Tmb = 65.5  # Establezco la constante Tmb
# Función para mostrar una lista de alimentos
# Función para calcular los macronutrientes necesarios
# Función para mostrar una lista de alimentos


def mostrar_lista(comida_lista, nombre_comida):
    print(f"\n{nombre_comida}:")
    for alimento in comida_lista:
        print(f"- {alimento}")


def calcular_macronutrientes():
    # Se piden los datos variables al usuario
    while True:
        peso = float(input("Introduce tu peso en kg: "))
        estatura = float(input("Introduce tu estatura en cm: "))
        edad = int(input("Introduce tu edad: "))

    # Se imprimen los datos proporcionados por el usuario para su revisión
        print(f"""Los datos que has ingresado son:
    - Peso: {peso} kg
    - Estatura: {estatura} cm
    - Edad: {edad} años""")
        respuesta = input("son correctos estos datos escribe 'si' o 'no': ")
        if respuesta == 'no'.lower():
            print("vuelve a ingresar tus datos: ")
            continue
        elif respuesta == 'si'.lower():
            break
    # Cálculos de macronutrientes

    def proteina():
        return 1.6 * peso

    def carbohidratos():
        return (Tmb + 13.75 * peso + 5.003 * estatura - 6.75 * edad) / 4

    def grasas():
        return ((Tmb + 13.75 * peso + 5.003 * estatura - 6.75 * edad) * 0.25) / 9

    # Imprimir resultados de los cálculos
    print(f"Tu consumo de proteína diaria es de {proteina()} g")
    print(f"Tu consumo de carbohidratos diarios es de {carbohidratos()} g")
    print(f"Tu consumo de grasas diario es de {grasas()} g")


# Función principal


def main():
    while True:
        print("elije que necesitas escribiendo el numero de la lista en la terminal")
        print("1. calcular macronutrientes")
        print("2. menu para el desayuno")
        print("3. menu para la comida")
        print("4. menu para la cena")
        print("5. salir")

        seleccion = int(input("introduce tu respuesta: "))
        if seleccion == 1:
            print(f"{calcular_macronutrientes()}")
        elif seleccion == 2:
            mostrar_lista(desayuno, "desayuno")
        elif seleccion == 3:
            mostrar_lista(comida, "comida")
        elif seleccion == 4:
            mostrar_lista(cena, "cena")
        elif seleccion == 5:
            print("gracias por usar fifood")
            break
        else:
            print("por favor selecciona una opcion valida")
            continue


main()
