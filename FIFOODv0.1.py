
# establezco algunas variables y datos fijos como lo es tmb, y solicitar el nombre del usuario
nombre = input("dime tu nombre: ")
print(f"bienvenid@ a FIDOOD {nombre} por favor sigue las instrucciones. ")
Tmb = 65.5


# defino el codigo principal como main() y dentro defino las funciones para
# tener mas comodiad a la hora de crear el ciclo de repeticion con while


def main():
    while True:
        # estas son las variables que son solicitadas al usuario
        peso = float(input("introduce tu peso:"))
        estatura = float(input("introduce tu estatura en cm: "))
        edad = float(input("introduce tu edad: "))
# defino algunas funciones

        def kcalorias_hombre():
            return Tmb+13.75*peso+5.003*estatura-6.75*edad

        def kcalorias_mujer():
            return Tmb+9.75*peso+4.003*estatura-4.7*edad
# una variable donde el usuario elige entre 2 opciones
        sexo = int(input("""introduce tu sexo
1)Hombre
2)Mujer
introduce tu respuesta: """))
# establezco una condicion que dicta dependiendo de la opcion seleccionada
# por el usuario que cambia algunos datos que arroje al usuario
        if sexo == 1:
            print(f"tus kcal de consumo diario son {kcalorias_hombre()}kcal")
        elif sexo == 2:
            print(f"tus kcal de consumo diario son {kcalorias_mujer()}kcal")
# aqui continuo definiendo funciones  que necesito antes de que se impriman las salidas
# que se mostraran al usuario

        def proteina():
            return 1.6*peso

        def carbohidratos():
            return kcalorias_hombre()/4

        def grasas():
            return (kcalorias_hombre()*0.25)/9
# aqui se imprimen las salidas y datos que seran arrojados al usuario
        print(f"tu consumo de proteina diaria es de {proteina()}g")
        print(f"tu consumo de carbohidratos diarios es de {carbohidratos()}g")
        print(f"tu consumo de grasas diario es de {grasas()}g")
        respuesta1 = input(
            'para salir escribe "salir" si quieres introducir nuevos datos escribe  "no": ')
# establezco de nuevo una condicion para que el usario pueda finalizar el ciclo o bucle
        if respuesta1.lower() == 'salir':
            print("Muchas gracias por usar mi programa vuelve pronto")
            break
        else:
            continue


main()
