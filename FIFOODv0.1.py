"""FIFOOD"""


# se le pide el nombre al usuario para hacer sentir su experiencia mas personalizada
nombre = input("dime tu nombre: ")
print(f"bienvenid@ a FIDOOD {nombre} por favor sigue las instrucciones. ")

# establezco una constante que servira para los calculos de mas adelante
Tmb = 65.5

# defino el codigo principal y las funciones dentro del codigo principal ya que se me facilita mucho mas intender


def main():
    while True:
        # se piden los datos variables al usuario
        peso = float(input("introduce tu peso en kg:"))
        estatura = float(input("introduce tu estatura en cm: "))
        edad = int(input("introduce tu edad: "))
# se imprimen los datos proporcionados por el usuario para que los pueda revisar y poder cambiarlos si algo esta mal
        print(f"""los datos que has ingresado son 
tu peso es: {peso} kg
tu estatura es: {estatura} cm
tu edad es: {edad} años""")


# se le pregunta al usuario si quiere cambiar/corregir sus datos
        validacion_datos = input('''asegurate de que los datos ingresados sean correctos ya que
un mal calculo podria afectar tu progreso :(
si los datos son incorrectos escribe"restart"
si son correctos escribe cualquier cosa en la terminal ;) :   ''')


# se establece una condicion con if para repetir el bucle y reescribir los datos
        if validacion_datos == 'restart'.lower():
            print("ingresa tus nuevos datos :)")
            continue

        def kcalorias_hombre():
            return Tmb+13.75*peso+5.003*estatura-6.75*edad

        def kcalorias_mujer():
            return Tmb+9.75*peso+4.003*estatura-4.7*edad


# se pregunta al usuario su sexo lo que determinara su calculo calorico, mas no afectara al calculo de sus macronutrientes
        sexo = int(input("""introduce tu sexo
1)Hombre
2)Mujer
introduce tu respuesta: """))

# se establece la condicion con if para calcular el consumo calorico del usuario dependiendo de su sexo
        if sexo == 1:
            print(f"tus kcal de consumo diario son {kcalorias_hombre()}kcal")
        elif sexo == 2:
            print(f"tus kcal de consumo diario son {kcalorias_mujer()}kcal")

# se definen funciones para calcular los macronutrientes a consumir por el usuario
        def proteina():
            return 1.6*peso

        def carbohidratos():
            return kcalorias_hombre()/4

        def grasas():
            return (kcalorias_hombre()*0.25)/9

# se imprimen los resultados de las operaciones realizadas por las funciones definidas
        print(f"tu consumo de proteina diaria es de {proteina()}g")
        print(f"tu consumo de carbohidratos diarios es de {carbohidratos()}g")
        print(f"tu consumo de grasas diario es de {grasas()}g")

# se le da la opcion al usuario de ingresar datos nuevos o salir del programa
        respuesta1 = input(
            'para salir escribe "salir" si quieres introducir nuevos datos escribe  "restart": ')

        if respuesta1.lower() == 'salir':
            print("Muchas gracias por usar mi programa vuelve pronto")
            break
        elif respuesta1.lower() == 'restart':
            print("introduce tus nuevos datos :)")
            continue


main()
