# Aprendizaje automatico

## Clase 14

En nuestras redes tendremos neuronas donde reciben información de otras neuronas, y luego de la aplicación de cierta **función de activación** sobre toda esa información recibida. Producen un valor de activación.

**Paradigma neuronal**

Lo importante no esta en la complejidad de las neuronas, sino en la complejidad de la arquitectura de las conexiones, llamadas sinapsis. 

En gral una neurona tiene el siguiente esquema:

![](2024-08-15-19-04-30-image.png)

Donde luego de realizarse la suma ponderada se aplica una **funcion de activación** a dicho resultado. Y esa es la salida de la neurona.
Algunas funciones de activación:

![g-activación](2024-08-15-19-04-17-image.png)

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
![](Pasted%20image%2020241021105946.png)

![](Pasted%20image%2020241017210630.png)
Y esto se llama **REGLA DEL APRENDIZAJE DEL PERCEPTRON**. Y dado un problema **linealmente separable**, esta regla converge a una solución en un numero finito de pasos.

Esto busca que W maximice la distancia mínima entre el hiperplano de separación y los puntos del conjunto de entrenamiento. 
## Clase 16

### Descenso por el gradiente
Definimos el error o **loss function**: (error cuadratico medio)
![](Pasted%20image%2020241021111133.png)
Este error compara las **salidas deseadas** con las **salidas generadas** por nuestro perceptron lineal (en este caso ses simplemente la suma ponderada). La idea es poder minimizar la función de error encontrando un W optimo.
En este caso tenemos que:
- $\xi_i^\mu$ : **VALOR DESEADO**
- $O_i^\mu$: **SALIDA NEURONAL** : $\overline{w}_i .\overline{\xi}$ (pesos . datos entrada)

Puedo calcular el gradiente que es el valor que me dirá hacia que dirección debo moverme para ir hacia el máximo crecimiento. Se calcula haciendo las derivadas de cada función de error por cada $w_{ik}$ 
![](Pasted%20image%2020241021114255.png)

Como queremos minimizar, nos moveremos en la dirección **contraria** al gradiente. 

Para ello luego de cada estimación del error, recalcularemos nuestro $W$ para poder acercarnos aun mas al mínimo de la función de error. 

## Clase 17

Retomamos el caso de neuronas de salida con función lineal identidad.  Buscamos resolver como minimizar el **error cuadrático medio**.
![](Pasted%20image%2020241021182757.png)
Donde :
![](Pasted%20image%2020241021120348.png)

Vemos que lo único que podemos variar dentro de esta función son nuestros valores $w_{ik}$.  Lo variamos hasta tener una configuración de W que nos de un error pequeño.

Luego de calcular el error, debo encontrar un nuevo $\overline{w}$ que se dara de la sig forma:
![](Pasted%20image%2020241021121611.png)
Luego de calcular el gradiente para un $w_{ik}$ arbitrario, y teniendo una **razon de aprendizaje** $\eta$ . Tengo que 
![](Pasted%20image%2020241021122106.png)
donde $d_i^\mu = \xi_i^\mu - O_i^\mu$

Esto solo vale cuando la función de salida de la neurona es la función identidad.
Y nos permite buscar un mínimo local de una función de muchas variables. En este caso buscamos el mínimo de la función **Error cuadrático medio**.

### Perceptron simple NO LINEAL

![](Pasted%20image%2020241021124421.png)

Para este caso mi error queda dado por 
![](Pasted%20image%2020241021130308.png)
Donde $E^1$ es el error cuadrático medio para la neurona de salida $i$ par el primer elemento del conjunto de entrenamiento. Y $O_i^1$ es la función de salida para los datos de entrada del primer elemento del conjunto de entrenamiento.  

Y podemos aplicar le método del descenso por el gradiente usando la misma definicion del **ECM**.
![](Pasted%20image%2020241021131634.png)
donde $O_i^\mu=g(h_i^\mu)$. Y podemos calcular cada componente $ik$ del gradiente:
![](Pasted%20image%2020241021131729.png)
redefinimos:
![](Pasted%20image%2020241021131950.png)
Y el descenso por el gradiente a la sinapsis $W$ queda:
![](Pasted%20image%2020241021132032.png)

