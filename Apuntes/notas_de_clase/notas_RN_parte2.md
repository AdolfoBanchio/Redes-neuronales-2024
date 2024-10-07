# Aprendizaje automatico

## Clase 14

En nuestras redes tendremos neuronas donde reciben información de otras neuronas, y luego de la aplicación de cierta **función de activación** sobre toda esa información recibida. Producen un valor de activación.

**Paradigma neuronal**

Lo importante no esta en la complejidad de las neuronas, sino en la complejidad de la arquitectura de las conexiones, llamadas sinapsis. 

En gral una neurona tiene el siguiente esquema:

![](2024-08-15-19-04-30-image.png)

Donde luego de realizarse la suma ponderada se aplica una **funcion de activación** a dicho resultado. Y esa es la salida de la neurona.
Algunas funciones de activación
![](2024-08-15-19-04-17-image.png)

### Aprendizaje supervisado

consiste en estimar el valor de una función arbitraria sin conocer su expresión funcional. A partir de un **conjunto de datos etiquetados**.

### Redes feed-forward

Las neuronas se organizan en una sucesión de capas. La información entra por la capa de entrada, procesa la información y la envía a la primera capa, procesan y envían a la siguiente y así hasta llegar a la capa de salida.

**Dentro de cada capa** no se intercambian información entre las neuronas, ni hacia atrás ni se saltean capas. Siempre va de la capa i a la capa i+1.

Los valores de entrada son siempre un numero.

La alternativa a las redes feed-forward son las **redes recurrentes**.

el desafío en una red siempre consiste en encontrar la correcta matriz de pesos **W**. para así poder permitir que la red asigne correctamente los patrones de entrada con los de salida.

De todos los datos etiquetados, un subconjunto se utiliza para entrenar la red y buscar el conjunto de sinapsis de cada neurona $\{ w_0,w_1,...,w_N\}$ y luego el resto se utiliza para evaluar el desempeño.


**Perceptron de una única capa**

Dada una red neuronal feed forward

![](Pasted%20image%2020241007162812.png)

Podemos ver que se pueden encontrar subredes desacopladas entre si. Donde hay una única salida para cada una. Donde cada subred tiene su propia matriz W de sinapsis. Y esto nos permitirá poder tratar cada subred en forma independiente de las otras (paralelizar).

## Clase 15
