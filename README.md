# pci-ad23
**Cesar Augusto Ramirez Davila  A01712439**

**Problematica y contexto:**
Una problematica muy comun que ocurre con las personas, es que desconocen por completo cuantas calorias deberian consumir diariamente asi como tambien el poder estructurar esas calorias en una dieta balanceada que contemple todos sus requerimientos diarios de proteina, carbohidratos y grasas, que son principalmento los macronutrientes mas importantes para la construccion de musculo. Entonces mi proyecto consiste en un programa que sea capaz de calcular las calorias que deberia consumir una persona sana acorde a su peso y estatura, asi como tambien la cantidad de los tres macronutrientes necesarios para llevar a cabo este requisito, asi como tambien ser adaptable acorde al tiempo de ejercicio que se realiza diariamente, para esto ultimo voy a utiizar los registros de mi smartwatch para tener un calculo mas preciso de cuantas calorias queman 2 horas de ejercicio 5 dias a la semana.
Esto me parece una idea bastante interesante ya que yo llevo aproximadamente casi un año contando mis calorias y macronutrientes consumidos ya que en algun futuro me gustaria ser fisicoculturista profesional, y es un tema del que conozco mucha informacion al respecto por lo que me reesultaria intersante diseñar una herramienta que sea util principalmente para mi en un futuro, y por supuesto, de paso podria serlo para las demas personas.

**Algoritmo FitBodyBuilding(nombre en proceso en proceso creativo)**

//ENTRADAS: datos del usuario (peso, estatura y sexo)
//SALIDA: calorias de mantenimiento y requerimientos diarios en macronutrientes para la persona acorde con los datos proporcionados.
Estatura=input
Peso=input
escribir("Porfavor ingresa tu nombre")
Nombre=input
**Si** es usuario nuevo escribir ("Hola {Nombre}, bienvenido a FitBodyBuilding, por favor ingresa los datos que te solicitaremos a continuacion")
**Sino** escribir ("Hola bienvenido de nuevo {nombre}, por favor ingresa tus datos mas recientes")
escribir("Por favor ingresa tu peso: ")
Peso= input
escribir("Por favor ingresa tu estatura en cm: ")
Estatura=input
escribir ("Por favor ingresa tu edad")
escribir("Por favor, ingresa si eres hombre o mujer")
Hombre=H
Mujer=M
escribir("AVISO IMPORTANTE: ASEGURATE DE QUE LOS DATOS INGRESADOS SON CORRECTOS YA QUE UN DATO INCORRECTO PUEDE LLEVAR A UNA RECOMENDACION ERRONEA Y POR TANTO TENER EFECTOS NEGATIVOS EN EL LOGRO DE TUS METAS")
escribir("estos datos son correctos? peso:{peso}kg, estatura:{estatura}cm, sexo{sexo seleccionada H/M})
input: Y/N
**Si **los datos son correctos entonces continuar
**Sino** escribir("por favor ingresa nuevamente tus datos")
escribir("Por favor ingresa tu peso: ")
Peso= input
escribir("Por favor ingresa tu estatura en cm: ")
Estatura=input
escribir ("Por favor ingresa tu edad")
escribir("Por favor, ingresa si eres hombre o mujer")
Hombre=H
Mujer=M
**Si** Hombre=True entonces:
                 TMB(TASA METABOLICA BASAL)=65.5
                 escribir("Por favor, ingresa tu nivel de actividad fisica")
                 *sedentario(nada de ejercicio)=TMB*1.2
                 *levemente activo(1-3 dias a la semana)=TMB*1.375
                 *moderadamente activo(4-5 dias a la semana)=TMB*1.55
                 *Muy activo(6.7 dias a la semana)=TMB*1.725
                 *Atleta profesional(ejercicio intenso todos los dias)=TMB*1.9
                   escribir("muy bien comencemos")
				   calorias a consumir= {nivel de actividad fisica}+(13.75*{Peso})+(5.003*     {Estatura})-(6.75*Edad)
				   escribir("tus calorias a consumir son {calorias a consumir}kcal")
				   proteinas a consumir= 1.6*{Peso}
				   escribir:("tus proteinas a consumir son {proteinas a consumir} gramos")
				   carbohidratos a consumir={calorias a consumir}/4
				   escribir("tus carbohidratos a consumir son {carbohidratos a consumir} gramos")
				   kcal en grasa a consumir=({calorias a consunir}*0.25)
				   grasas a consumir={kcal en grasas a consumir}/9
				   escribir("tus grasas a consumir son {grasas a consumir}gramos")
** Sino** /**or ** mujer=True
                    TMB(TASA METABOLICA BASAL)=65.5
                 escribir("Por favor, ingresa tu nivel de actividad fisica")
                 *sedentario(nada de ejercicio)=TMB*1.2
                 *levemente activo(1-3 dias a la semana)=TMB*1.375
                 *moderadamente activo(4-5 dias a la semana)=TMB*1.55
                 *Muy activo(6.7 dias a la semana)=TMB*1.725
                 *Atleta profesional(ejercicio intenso todos los dias)=TMB*1.9
                   escribir("muy bien comencemos")
				   calorias a consumir2=({nivel de actividad fisica}+(9.563*{Peso})+(1.850*{Altura})-(4.676*{edad})
				   escribir("tus calorias a consumir son{calorias a consumir2}kcal")
				   proteinas a consumir= 1.6*{Peso}
				   escribir:("tus proteinas a consumir son {proteinas a consumir} gramos")
				   carbohidratos a consumir={calorias a consumir}/4
				   escribir("tus carbohidratos a consumir son {carbohidratos a consumir} gramos")
				   kcal en grasa a consumir=({calorias a consunir}*0.25)
				   grasas a consumir={kcal en grasas a consumir}/9
				   escribir("tus grasas a consumir son {grasas a consumir}gramos")
escribir("gracias por usar mi aplicacion, regresa en 2 semana para obtener nuevos parametros, mucho exito en tu camino")

//SALIDA: kcal de mantenimiento y requerimientos de macronutrientes diarios
