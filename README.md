# Algoritmo FitBodyBuilding (nombre en proceso creativo)

## Problemática y contexto

Una problemática muy común que ocurre con las personas es que desconocen por completo cuántas calorías deberían consumir diariamente, así como también el poder estructurar esas calorías en una dieta balanceada que contemple todos sus requerimientos diarios de proteína, carbohidratos y grasas, que son principalmente los macronutrientes más importantes para la construcción de músculo.

Mi proyecto consiste en un programa que sea capaz de calcular las calorías que debería consumir una persona sana de acuerdo a su peso y estatura, así como también la cantidad de los tres macronutrientes necesarios para llevar a cabo este requisito. Además, el programa será adaptable de acuerdo al tiempo de ejercicio que se realiza diariamente. Para esto último, utilizaré los registros de mi smartwatch para tener un cálculo más preciso de cuántas calorías queman 2 horas de ejercicio 5 días a la semana.

Esto me parece una idea bastante interesante, ya que llevo aproximadamente casi un año contando mis calorías y macronutrientes consumidos, y en algún futuro me gustaría ser fisicoculturista profesional. Tengo conocimientos en este tema y me resultaría interesante diseñar una herramienta que sea útil principalmente para mí en el futuro, y, por supuesto, podría serlo para otras personas.

## Algoritmo FitBodyBuilding (nombre en proceso creativo)

### Entradas: datos del usuario (peso, estatura y sexo)
### Salida: calorías de mantenimiento y requerimientos diarios en macronutrientes para la persona según los datos proporcionados.

1. Por favor, ingresa tu nombre: (nombre)
2. Si eres un usuario nuevo, te damos la bienvenida a FitBodyBuilding. Por favor ingresa los datos que te solicitaremos a continuación. Si no, te damos la bienvenida de nuevo.
3. Por favor ingresa tu peso: (peso)
4. Por favor ingresa tu estatura en cm: (estatura)
5. Por favor ingresa tu edad: (edad)
6. Por favor, ingresa si eres hombre (H) o mujer (M).
7. AVISO IMPORTANTE: ASEGÚRATE DE QUE LOS DATOS INGRESADOS SON CORRECTOS, YA QUE UN DATO INCORRECTO PUEDE LLEVAR A UNA RECOMENDACIÓN ERRÓNEA Y, POR TANTO, TENER EFECTOS NEGATIVOS EN EL LOGRO DE TUS METAS.
8. ¿Son estos datos correctos? Peso: {peso} kg, estatura: {estatura} cm, sexo: {sexo seleccionado (H/M)} (Y/N)

Si los datos son correctos, continuamos. Sino, ingresa nuevamente tus datos.

Si eres un hombre (H):
- Tasa Metabólica Basal (TMB) = 65.5
- Por favor, ingresa tu nivel de actividad física:
  - Sedentario (nada de ejercicio) = TMB * 1.2
  - Levemente activo (1-3 días a la semana) = TMB * 1.375
  - Moderadamente activo (4-5 días a la semana) = TMB * 1.55
  - Muy activo (6-7 días a la semana) = TMB * 1.725
  - Atleta profesional (ejercicio intenso todos los días) = TMB * 1.9

Muy bien, comencemos.

Calorías a consumir = {nivel de actividad física} + (13.75 * {peso}) + (5.003 * {estatura}) - (6.75 * {edad})

Tus calorías a consumir son {calorías a consumir} kcal.

Proteínas a consumir = 1.6 * {peso}

Tus proteínas a consumir son {proteínas a consumir} gramos.

Carbohidratos a consumir = {calorías a consumir} / 4

Tus carbohidratos a consumir son {carbohidratos a consumir} gramos.

Kilocalorías en grasa a consumir = ({calorías a consumir} * 0.25)

Grasas a consumir = {kcal en grasas a consumir} / 9

Tus grasas a consumir son {grasas a consumir} gramos.

Si eres una mujer (M):
- Tasa Metabólica Basal (TMB) = 65.5
- Por favor, ingresa tu nivel de actividad física:
  - Sedentario (nada de ejercicio) = TMB * 1.2
  - Levemente activo (1-3 días a la semana) = TMB * 1.375
  - Moderadamente activo (4-5 días a la semana) = TMB * 1.55
  - Muy activo (6-7 días a la semana) = TMB * 1.725
  - Atleta profesional (ejercicio intenso todos los días) = TMB * 1.9

Muy bien, comencemos.

Calorías a consumir = {nivel de actividad física} + (9.563 * {peso}) + (1.850 * {estatura}) - (4.676 * {edad})

Tus calorías a consumir son {calorías a consumir} kcal.

Proteínas a consumir = 1.6 * {peso}

Tus proteínas a consumir son {proteínas a consumir} gramos.

Carbohidratos a consumir = {calorías a consumir} / 4

Tus carbohidratos a consumir son {carbohidratos a consumir} gramos.

