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


## Clase 18

El método de **back propagation** es el metodo utilizado para poder entrenar redes neuronales feed-forward con multiples capas ocultas intermedias.

![](Pasted%20image%2020241114113547.png)

A partir de la capa de entrada se calculan los valores de salida de las neuronas intermedias como:
![](Pasted%20image%2020241114113645.png)

($\overline{w_j}$ son los pesos sinapticos de la neurona intermedia j, y $\overline{\xi^\mu}$ es el vector de las N entradas de la red. )

Y luego de la capa de salida  
![](Pasted%20image%2020241114113845.png)

Ahora que tengo el valor de salida, puedo calcular el error cuadrático medio para este resultado obtenido, y luego calcular el gradiente para este resultado obtenido para luego aplicar el método del descenso por el gradiente. Dado el ejemplo $\mu$ del conjunto de entrenamiento podemos calcular nuestro ECM.
![](Pasted%20image%2020241114114043.png)

De esta forma ahora podremos calcular el gradiente y actualizar los pesos sinapticos de atrás hacia adelante. Es decir comenzando por los pesos de la ultima capa oculta con la capa de salida. 

![](Pasted%20image%2020241114114505.png)

![](Pasted%20image%2020241114114522.png)

En una red donde tenemos capas ocultas, nuestros parametros seran:
$$
(N\times L)+(L\times M)
$$
**¿Cuando actualizamos los pesos?**
Podemos actualizarlos luego de cada ejemplo del conjunto de entrenamiento, a esto se lo denomina **actualización en linea**. Pero es muy costoso para redes con muchos parámetros y un set muy grande. 

La Otra alternativa es la actualización en lotes (**batches**). Que consiste en actualizar luego de cada **EPOCA**. Osea luego de mostrarle todo el conjunto de entrenamientos.

## clase 19

Generalizamos el metodo de back propagation para un numero arbitrario de capas ocultas. si queremos actualizar los acoplamientos $\overline{w}_{pq}$ entre la capa q (anterior) y p (posterior)

![](Pasted%20image%2020241114124330.png)
## Clase 20

Redes neuronales como aproximadores universales de funciones sin dar una forma analítica.  

## Clase 21

### Problemas de back-propagation
Notamos como se reduce la capacidad de aprendizaje a medida que agregamos mas capas ocultas a la red. Porque como utilizamos funciones sigmoideas o relus, estas derivadas son muy pequeñas. Y vemos que a medida que agregamos mas capas, las neuronas mas cercanas a la entrada se ven afectadas por aun mas derivadas, por lo que toman valores cada vez mas pequeños. A esto se lo llama **supresión del gradiente**

![](Pasted%20image%2020241114140141.png)

Algunos problemas:
- Rugosidad de la funcion: mayor cantidad de parametros, mayor cantidad de maximos y minimos de la funcion de error
- Valores iniciales de los pesos
- Dependencia con derivadas (valores muy pequeños hacen que avancemos muy lento)
- dependencia con la razón de aprendizaje
- overfitting: la red predice muy bien los elementos del conjunto de entrenamiento pero no responde de forma deseada cuando se le presentan los conjuntos de testeos, por ende no generaliza bien. 

**Mejora para back propagation**
**Auto encoder**: Entrenamos una red feed forward para que aprenda la funcion identidad, donde tiene la misma cantidad de neuronas de salida como de entrada, y una capa oculta con menor cantidad de neuronas. Una vez que esta red aprenda lo mejor posible la identidad, estos serán nuestros pesos para colocar entre nuestra capa de entrada a primera capa oculta en nuestra red original. Y así vamos generando autoencoders agregandole las capas necesarias para cubrir todas las que tendrá nuestra red feedforward original.

## Clase 22

**Mejora para back propagation**
- **Minibatch:** dividir el conjunto de entrenamiento en mini grupos, de manera que en cada época se hace una re-asignación aleatoria de todos los ejemplos. Batch mas pequeños atraen el descenso por el gradiente a mínimos mas planos, de modo que es mas fácil escapar de los mínimos locales. 
- **Dropout**: suprimir un cierto número de neuronas de manera aleatoria por lo que cuando se calcula la salida no se considera toda la información. Neuronas no se tendrán en cuenta con una probabilidad p=0.5, de modo que habrán dimensiones que no serán tenidas en cuenta a la hora de calcular el gradiente, y alguna de estas dimensiones puede ser la que evita salir de un mínimo local. Esto permite reducir el overfitting y que la red responda correctamente a los test. 

**Memoria y adaptación al MDG:** 
	![](Pasted%20image%2020241114181243.png)
	Con este parámetro "manejamos" el incremento persistente y pequeño haciendolo próximo a uno para hacer que esos incrementos en zonas planas aun mas grande. Aumenta la velocidad en direcciones de gradiente pequeño.
	![](Pasted%20image%2020241114204826.png)

Existen métodos adaptativos que busca que cada dimensión del problema tenga su propio criterio en el descenso por el gradiente. 
![](Pasted%20image%2020241114204928.png)
Existen diferentes métodos que nos definen como establecer dicho parámetro especifico:
- ADGRAD
- ADADELTA
- RPPROP
- RMSprop (hinton)
- ADAM
Estos ultimos dos metodos, agregan **nuevos** **hiperparametros** a tener en cuenta a la hora de configurar nuestro modelo neuronal. 

## Clase 23

**Regularizaciones**: consiste en agregar un termino adicional a la función de error. 
![](Pasted%20image%2020241114180837.png)

Existen dos tipos de regularización conocidos. L1 y L2.

![](Pasted%20image%2020241114180923.png)
Donde acá $\lambda$ es nuestro nuevo hiperparametro.

### Reemplazo de la función ECM por otra función de error
**Cross Entropy**: 
Se basa en primero obtener el mínimo número de bits por segundo para representar información (**razón de entropía H**). Y el número máximo de bits por unidad de tiempo que puede transferirse con confianza en la presencia de ruido (**capacidad de información C**). Se puede enviar información a menos que H < C.

### Problema de la regresión polinomial
## Clase 24
