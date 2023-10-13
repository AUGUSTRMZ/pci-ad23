# Algoritmo de NUTRIBOT

## Problemática y contexto

El proyecto fue repensado para volverse un asistente virtual para nutriologos ya que finalmente al pensarlo si bien es cierto que es bueno que las personas tengan conceptos basicos sobre nutricion siempre es recomendable que asistan con un profesional en el tema para que su dieta este mas balanceada que solo cumplir con los macronutrientes y kcalorias necesarias consumiendo solo hamburguesas o pizza y es por esa razon que el usuario objetivo del programa cambio para ser usado por profesionales de la nutricion.

Mi proyecto consiste en un programa que sea capaz de calcular las calorías que debería consumir una persona sana de acuerdo a su peso y estatura, así como también la cantidad de los tres macronutrientes necesarios para llevar a cabo este requisito. Para poder calcular esto se utilizo el metodo de Harris-Benedict que es el metodo universal para calcular las necesidades caloricas de una persona para mantenerse en su peso ideal.

Esto me parece una idea bastante interesante, ya que llevo aproximadamente casi un año contando mis calorías y macronutrientes consumidos, y en algún futuro me gustaría ser fisicoculturista profesional. Tengo conocimientos en este tema y me resultaría interesante diseñar una herramienta que sea útil principalmente para mí en el futuro, y, por supuesto, podría serlo para otras personas.

## Algoritmo NUTRIBOT

### Entradas: datos del paciente (peso, estatura y sexo)
### Salida: calorías de mantenimiento y requerimientos diarios en macronutrientes para la persona según los datos proporcionados.

1. Por favor, ingresa el nombre del paciente: (nombre)
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

