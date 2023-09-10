nombre = input("dime tu nombre: ")
print(f"bienvenid@ {nombre} por favor sigue las instrucciones. ")
peso = float(input("introduce tu peso:"))
estatura = float(input("introduce tu estatura en cm: "))
edad = float(input("introduce tu edad: "))
Tmb = 65.5
sexo = float(input("escribe 1 si eres hombre o 2 si eres mujer: "))


def kcalorias_hombre():
    return Tmb+13.75*peso+5.003*estatura-6.75*edad


def kcalorias_mujer():
    return Tmb+9.75*peso+4.003*estatura-4.7*edad


def proteina():
    return 1.6*peso


def carbohidratos():
    return kcalorias_hombre()/4


def grasas():
    return (kcalorias_hombre()*0.25)/9


def main():
    while True:

        if sexo == 1:
            print(f"tus kcal de consumo diario son {kcalorias_hombre()}kcal")
        elif sexo == 2:
            print(f"tus kcal de consumo diario son {kcalorias_mujer()}kcal")
        else:
            print(
                "Lo siento los datos que has ingresado no estan dentro de mis parametros.")
            print("Por favor vuelve a intentarlo. ")
            exit()

        print(f"tu consumo de proteina diaria es de {proteina()}g")
        print(f"tu consumo de carbohidratos diarios es de {carbohidratos()}g")
        print(f"tu consumo de grasas diario es de {grasas()}g")
        respuesta = input("Quieres salir?: s/n")
        if respuesta.lower() == 's':
            print("Muchas gracias por usar mi programa vuelve pronto")
            break


main()
