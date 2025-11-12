# condicionales_fp

## ejercicio 1.

Ejercicio 1
Vamos a mejorar la solución del Ejercicio 1 - Tarea 1.
Realice conversiones entre las unidades de medida presentadas en la siguiente tabla:

| Índice | Conversión                           | Factor |
|:------:|--------------------------------------|:------:|
| 0      | Kilómetro a metro                    | 1000   |
| 1      | Centímetro a metro                   | 0.01   |
| 2      | Kilómetro por hora a millas por hora | 0.62   |
| 3      | Nota en Educatic a nota en Canvas    | 20     |
| 4      | Nota en Canvas a nota en Educatic    | 0.05   |
| 5      | Mililitro a centímetro cúbico        | 1      |
| 6      | Dólar (USA) a peso colombiano        |Actualizar|
| 7      | Peso colombiano a dólar (USA)        |Actualizar|
| 8      | Libra a kilogramo                    | 0.45   |
| 9     | Minuto luz a kilómetro               | 17987539.67|

Para este ejercicio se deben almacenar los factores de conversión en un vector (tipo de dato ```list``` de Python) para luego:

- Solicitar al usuario que escoja el tipo de conversión que quiere realizar, para esto hay dos opciones:
 - Si trabajas en Google Colab puedes usar una lista desplegable, que es un tipo de campo de [formulario](https://www.youtube.com/watch?v=vx7yOZ5_Cw8) llamado *dropdown*
 - Si trabajas en otro editor puedes imprimir un menú de opciones numeradas y solicitarle al usuario que ingrese con ```input```el número de la opción que le interesa.

- Solicitar al usuario que ingrese el dato que quiere convertir.
- **Realizar una estructura de selección que convierta el dato ingresado por el usuario según el tipo de conversión que ha escogido.**

Al igual que en la Tarea 1, se debe acceder al factor de conversión correspondiente de acuerdo a su posición o índice en el vector de factores de conversión.

## ejercicio 2.
Estudie cómo realizar conversiones entre los sistemas de numeración Hexadecimal, Binario y Decimal.

Programe un algoritmo que solicite al usuario un número entre 0 y 15 y entregue el valor correspondiente en los sistemas numéricos Hexadecimal y Binario.

Nota: No está permitido usar funciones de conversión nativas como bin(), hex(), etc, o funciones similares de librerías.