# bienvenida al programa
print('bienvenido a NutriBot el asistente virtual para el nutriologo moderno')

# establezco las contasntes y la contsnte de tasa metabolica basal misma que sera necesaria para todos los calculos
Tmb = 65.5*1.2
user = 'profe'
password = 'password'
registros_paciente = []


def iniciar_sesion():
    while True:
        input_user = (input('ingresa tu user: '))
        if input_user == user.strip():
            print('usuario enocntrado.'*1)
            break
        else:
            print('usuario incorrecto')
    while True:
        input_password = (input('introduce tu password: '))
        if input_password == password.strip():
            print(f'password correcto bienvenido {user}!')
            break
        else:
            print('password incorrecto intente de nuevo')

# defino la funcion que tiene mas funciones y ciclos anidados que pide los datos del paciente y los procesa para guardarlos y hacer los calculos


def datosycalculos():
    while True:
        nombre_paciente = input('ingrese el nombre del paciente: ')
        peso = float(input('ingresa el peso del paciente en kg: '))
        estatura = int(input('ingresa la estatua del paciente en cm: '))
        edad = int(input('ingresa la edad del paciente: '))
        sexo = input('selecciona tu sexo (hombre/mujer):')
        print(f"""los datos ingresados del paciente son correctos:
1. peso: {peso}kg
2. estatura: {estatura}cm 
3. edad:  {edad} años
4. sexo: {sexo}""")
# se solicita una una confirmacion al nutriologo de los datos del paciente para asegurarse de que los datos sean correctos
        confirmar_datos = input('datos del paciente correctos?: ')
        if confirmar_datos == 'si'.lower().strip():
            break
        if confirmar_datos == 'no'.lower().strip():
            print('vuelve a introducir los datos del paciente:')
            continue
        break

# se definen funciones para los calculos para ser llamadas mas tarde
    while True:
        def kcal_hombre():
            return 88.356+(13.397 * peso)+(4.799*estatura)-(5.677*edad)

        def kcal_mujer():
            return 497.593+(9.247*peso)+(3.098*estatura)-(4.330*edad)

        def proteina():
            return 1.6*peso

        def carbohidratos():
            return (Tmb + 13.75 * peso + 5.003 * estatura - 6.75 * edad) / 4

        def grasas():
            return ((Tmb + 13.75 * peso + 5.003 * estatura - 6.75 * edad) * 0.25) / 9

        break


# se establece la funcion que abre el menu principal con ciclos anidados para menus de opciones con condiciones que imprimen diferentes datos de acuerdo a la seleccion del usuasrio


    def menu_prinicpalresultados():
        while True:
            answer = int(
                input('estoy listo para calcular presiona, 1 para iniciar:'))
            if answer == 1 and sexo == 'hombre'.lower().strip():
                print(f"""
realizar una dieta con una base de {kcal_hombre()}kcal
el consumo diario de proteina del paciente debe ser de {proteina()}g
el consumo diario de carbohidratos del paciente debe ser de {carbohidratos()}g
el consumo diario de grasas del paciente debe ser de {grasas()}g
se recomienda tomar al menos 2 litros de agua al dia """)
                break
            elif answer == 1 and sexo == 'mujer'.lower().strip():
                print(f"""
realizar una dieta con una base de {kcal_mujer()}kcal
el consumo diario de proteina del paciente debe ser de {proteina()}g
el consumo diario de carbohidratos del paciente debe ser de {carbohidratos()}g
el consumo diario de grasas del paciente debe ser de {grasas()}g
se recomienda tomar al menos 2 litros de agua al dia """)


# se establece una funcion para guardar los registros del paciente en la lista definida al inicio


    def guardar_registros_paciente():
        while True:
            print('quieres guardar los registros del paciente: ?')
            decision = input('si o no: ')
            if decision == 'si'.lower().strip():
                paciente = {
                    "nombre": nombre_paciente,
                    "peso": peso,
                    "estatura": estatura,
                    "edad": edad,
                    "sexo": sexo
                }
                registros_paciente.append(paciente)
                print(f'paciente:{nombre_paciente} guardado en registros. ')
                break
            elif decision == 'no'.lower().strip():
                print('entendido :)')
                break


# se establece una funcion que nos permite consultar la lista de registros de los pacientes


    def consultar_registros():
        while True:
            pregunta = input('quieres re/consultar los datos del paciente?: ')
            if pregunta == 'no'.lower().strip():
                print('entendido :)')
                break
            if pregunta == 'si'.lower().strip():
                if len(registros_paciente) == 0:
                    print('no hay registros de pacientes disponibles')
                else:
                    for paciente in registros_paciente:
                        print('datos del paciente: ')
                        print(f'nombre: {paciente["nombre"]}')
                        print(f'peso: {paciente["peso"]}kg')
                        print(f'estatura: {paciente["estatura"]}')
                        print(f'edad: {paciente["edad"]}')
                        print(f'sexo: {paciente["sexo"]}')

    menu_prinicpalresultados()

    guardar_registros_paciente()

    consultar_registros()


# se establecen ciclos para confirmar varias veces si no se desea reconfirmar los datos del paciente dando varias oportunidades antes de que los datos sean borrados
    while True:
        print('necesitas volver a consultar los datos de/los paciente(s)? o deseas salir de esta interfaz?: ')
        consultar = input('escribe si o salir: ')
        if consultar == 'si'.lower().strip():
            consultar_registros()
        elif consultar == 'salir'.lower().strip():
            print('entendido, saliendo...')
            break


# este es el menu principal
def main():
    while True:
        print('Bienvenido al menu principal')
        iniciar = input(
            '¿Deseas iniciar/reiniciar el programa de nuevo? (si/no): ')
        if iniciar == 'no'.lower().strip():
            print('Cerrando programa')
            print('nos vemos pronto')
            break
        elif iniciar == 'si'.lower().strip():
            iniciar_sesion()
# este ciclo nos permite agregar mas pacientes a la base de datos y al mismo tiempo recalcula para ese nuevo paciente entregando calculos nuevos y se agrega a la base de datos del dia
            while True:
                datosycalculos()
                reiniciar = input(
                    '¿Deseas agregar un nuevo paciente? (si/no): ')
                if reiniciar == 'no'.lower().strip():
                    break
        else:
            print('Opción no válida. Por favor, ingresa "si" o "no".')


main()
