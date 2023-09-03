def Dime_tu_peso():
    peso = float(input("introduce tu peso en KG: "))
    return peso


def Dime_tu_estatura():
    estatura = float(input("introduce tu estatura en cm: "))
    return estatura


def calcular_calorias():

    tmb = 65.5
    edad = int(input("por favor introduce tu edad: "))
    calorias_diarias = tmb+13.75*Dime_tu_peso()+5.003*Dime_tu_estatura()-6.75*edad
    return calorias_diarias


def calcular_proteina():
    proteina_diaria = 1.6*Dime_tu_peso()
    return proteina_diaria


def calcular_grasas():
    calorias_grasas = calcular_calorias()*0.25
    req_grasas = calorias_grasas/9
    return req_grasas


def calcular_carbohidratos():
    carbos_diarios = calcular_calorias()/4
    return carbos_diarios


def main():
    nombre = input("Hola cual es tu nombre?: ")
    print(f"Bienvenido {nombre}!!!")
    print("Muy bien, comencemos!!!")
    print(f"tus calorias a consumir son {calcular_calorias()}kcal")
    print(f"tu requerimiento de proteina diaria es de {calcular_proteina()}g")
    print(f"tu requerimiento de grasas diaria es de {calcular_grasas()}g")
    print(
        f"tu requerimiento de carbohidratos es de {calcular_carbohidratos()}g")
    print(f"MUCHAS GRACIAS {nombre} nos vemos pronto")


main()
