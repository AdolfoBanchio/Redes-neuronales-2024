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

### Aprendizaje supervisado en un perceptron simple

Un perceptron simple solo lo podemos ver en redes de una sola capa. 

Si tenemos una sola entrada de salida y **N** entradas, podemos pensar el conjunto de entradas como un vector arbitrario en $R^N$   , $\overline{\xi} = (\xi_1,...,\xi_n)$  , estos valores pueden ser discretos, continuos acotados o no acotados. 

El valor de salida de la neurona $O_i$ dependerá de la función de activación $g(x)$ 
$$
O = g(\overline{w}_i.\overline{\xi}-\mu_i)
$$
donde w es la eficacia sinaptica entre la entrada k y la neurona de salida i, y $\mu$ es el umbral de activación.

en el aprendizaje supervisado tendremos el valor que debe tomar la salida para cierto conjunto de valores de entrada, de modo que tenemos el conjunto de datos etiquetados $\{ \overline{\xi^\alpha},\xi^\alpha_i \}$ . Donde $\xi^\alpha_i$ representa el valor que debe tomar $O_i$ pero en realidad la neurona tomara el valor:
$$
O = g(\overline{w}_i.\overline{\xi}-\mu_i)
$$
Por lo que debemos encontrar el w y el umbral tal que sean capaces de hacer que nuestra red asigne correctamente las entradas y las respectivas salidas para el conjunto de datos de entrenamiento, de modo que luego sea capaz re resolver bien los casos que nunca vio y poder asignar una salida correcta a una entrada arbitraria.

Suponiendo que tenemos una entrada extra con indice k = 0 que vale -1, podemos olvidarnos del valor del umbral.
![](Pasted%20image%2020241017193408.png)

Entonces que la red **aprenda** significa encontrar un vector **N+1** que resuelva los datos provistos en el conjunto de entrenamiento.
![](Pasted%20image%2020241017193456.png)
![](Pasted%20image%2020241017193512.png)
(esto es lo deseado)

Como esto no es posible, trabajaremos con una **tolerancia al error**, de modo que:
**Error de entrenamiento** $\leq$ **Tolerancia al error**

**Clasificación binaria**
se da cuando tenemos sets de datos que pueden ser clasificados en dos posibles valores de salida de nuestra neurona. Y decimos que un problema de este tipo es **LINEALMENTE SEPARABLE** cuando tenemos que en $R^N$ debe existir al menos un hiperplano en $R^{N-1}$ que deje de un lado todos los vectores de entrenamiento.

![](Pasted%20image%2020241017203614.png)

Tratamos entonces de encontrar un vector $\overline{W}$ que deje menos ejemplos del lado equivocado.

**Regla de aprendizaje del perceptron**

Supongamos tenemos un perceptron simple con **N** entradas y una salida binaria.

La idea es partir de un vector W aleatorio, e ir presentando a la red cada elemento del conjunto de entrenamiento. Dependiendo del resultado (correcto o no) modificamos los parámetros. 
$O = g(h^\alpha)$ . 
![](Pasted%20image%2020241017205500.png)
Vectorialmente: $\Delta\overline{W}^\alpha = 2.\eta.\xi^\alpha . \overline{\xi}^\alpha$  (recordamos $\xi^\alpha$ es nuestro valor esperado de salida para un valor de entrenamiento)

![](Pasted%20image%2020241017205717.png)

El parametro $\eta$ se llama **razon de aprendizaje** y es un **hiperparámetro**, y en general se mantiene fijo durante el aprendizaje.

Una actualización del vector $\overline{W}$ implica mostarle todos los elementos del conjunto de entrenamiento. A este numero de interaciones lo llamamos **EPOCA**.

Para poder encontrar la mejor solución pedimos que:
![](Pasted%20image%2020241017210614.png)
Donde:
![](Pasted%20image%2020241017210630.png)
Y esto se llama **REGLA DEL APRENDIZAJE DEL PERCEPTRON**. Y dado un problema **linealmente separable**, esta regla converge a una solución en un numero finito de pasos.

## Clase 16

### Descenso por el gradiente
