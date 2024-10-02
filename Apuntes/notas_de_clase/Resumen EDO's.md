# Resumen Sistemas dinámicos

Un sistema dinámico es cualquier sistema físico cuyo estado evoluciona con el tiempo. En nuestros sistemas existen variables que cambian con el tiempo. Lo que nos interesa es poder modelar como depende la razón de cambio de dichas variables con respecto al tiempo. 

## EDOs unidimensionales

$$
\frac{dx}{dt} = f(x)
$$
esto es un sistema unidimensional, pues la única variable que describe el estado del sistema es x. 

Lo que nos va a interesar es poder hacer un análisis cualitativo de los sistemas. Para ello graficamos $\dot{x} \ vs \ x$ . Y según el valor de la razón de cambio podemos ver hacia donde se dirigirá x. 

- Si f(x) es positiva, x ira a la derecha\
- Si f(x) es negativa, x ira a la izquierda
- Si f(x) = 0, el sistema permanecerá en dicho punto.

Llamamos **punto fijo** (o punto critico) del sistema a una raíz de $f(x)$. Es decir un $x*$ tal que $f(x*)=0$.

En una dimension para ciertos puntos fijos podemos decir que son:

- **Estables**: la trayectoria (de $\dot{x}$)se acerca al punto
- **Inestables**: repelen la trayectoria.

Esto dependera del valor de f(x)

![Pasted image 20240927164328.png](Pasted%20image%2020240927164328.png)

![Pasted image 20240927164407.png](Pasted%20image%2020240927164407.png)

En una sola dimension los resultados posibles de una solución es 
- ir a $\pm\infty$ 
- ir a un punto **estable** 


### Problema valor inicial
Consiste en tener una ecuación diferencial y un valor inicial de x en el sistema.

$$
\dot{x}=f(x) \qquad x(0)=x_0
$$
Supongamos que $f(x)$ y $f'(x)$ son continuas en un intervalo **R** del eje-x. Y supongamos $x_0 \in R$ . Entonces el problema tiene una solución **única** de $x(t)$. En algún intervalo $(-\tau,\tau)$ alrededor de $t=0$.

Cada $x_0$ me da una trayectoria diferente, esto me garantiza que no existan dos trayectorias que se crucen en un mismo instante de tiempo $t$.

Este resultado se generaliza para dimension n.

### Bifurcaciones unidimensionales

Acá nos interesa analizar la **dependencia en los parámetros** de un sistema. La estructura cualitativa de un sistema se puede ver muy perjudicada por los valores que toman los parámetros del mismo. En particular veremos un impacto en los puntos críticos. Pueden ser creados, destruidos o cambiar su estabilidad. Estos **cambios** cualitativos en la estructura del sistema lo llamaremos **bifurcaciones**, y al parámetro que la produce sera un **punto de bifurcación**.

#### Bifurcación Saddle-Node
Es un tipo de bifurcación donde los puntos fijos son creados y destruidos. A medida que el parametro varia, los puntos fijos se aproximan en valor, se convierten en uno solo y luego desaparecen. Veamos el ejemplo.
$$ \dot{x} = r + x^2 $$
![Pasted image 20240927171242.png](Pasted%20image%2020240927171242.png)
en este ejemplo $r_c=0$ es nuestro punto de bifurcación.

Otra forma de ver graficamente como se comportan las bifurcaciónes, es graficar $\dot{x} = 0$ . Es decir dar los **puntos fijos** para diferentes valores de $r$. En este caso seria $r = -(x*)^2$ 
![Pasted image 20240927171611.png](Pasted%20image%2020240927171611.png)

O tambien podemos tratar a nuestro parametro $r$ como la variable independiente y graficar $x*=\sqrt{-r}$

![Pasted image 20240927172940.png](Pasted%20image%2020240927172940.png)

**Formas normales** 

De cierta forma podemos decir que todas las bifurcaciones de tipo **saddle-node** se pareceran a $\dot{x}= r-x^2 \quad \text{o} \quad \dot{x}=r+x^2$

Como no todas las funciones tienen forma polinomica vamos a utilizar series de Taylor para poder expresar de manera polinomica nuestras funciones alrededor de un punto critico $x*$ y el parametro de bifurcacion $r$. Entonces a nuestra funcion $f$ la escribimos en parametros de $x$ y $r$ . Y damos la serie de Taylor centrada en ($x*,r_c$). 

![desarrollo taylor](Pasted%20image%2020240927173913.png) ^1b893a

sabemos que $f(x*,r_c)=0$ y que la primera derivada en x es tangencial a la parabola por ser una bifurcación de tipo saddle-node (en $r_c$ se condensan los dos pf en uno) entonces su valor es 0. Y obtenemos que.

![](Pasted%20image%2020240927174137.png)

Y vemos que ahora nuestra razón de cambio es parecida a nuestros prototipos de ejemplo de bifurcaciones saddle-node. Y podremos encontrar los puntos fijos y analizar el sistema. 

#### Bifurcación transcrítica
La forma normal de una bifurcación transcritica es:
$$
\dot{x} = rx -x^2 = x(r-x)
$$
Siempre tenemos un punto fijo $x*=0$ para cualquier valor de $r$

![](Pasted%20image%2020240927180445.png)

Notamos que siempre nuestro otro punto critico es $x*=r$. pero cuando $r<0$ es inestable y si $r>0$ es estable. intercambian estabilidad entre x*=0 y x*=r luego de la bifurcación.

![](Pasted%20image%2020240927180815.png)

Este grafico nos muestra las dos rectas de ambos puntos criticos y su estabilidad. Un punto critico siempre es 0 con respecto a r, y el otro es lineal a r. Pero intercambian estabilidad cuando r pasa de negativo a positivo. 

#### Bifurcaciones Pitchfork
**Supercriticas**

Si luego del desarrollo de [taylor](#^1b893a) que hacemos cerca de la bifurcación nos queda lo siguiente:
$$
\dot{x} = x(r-x^2)
$$
que es una función invariante (vale igual para -x). Tenemos la siguiente bifurcación.

![](Pasted%20image%2020240927183207.png)
Tenemos un unico punto critico en el 0, siempre y cuando r no sea positivo. Cuando r pasa a ser positivo, entonces el termino $r-x^2$ pude valer 0 cuando $x=\pm \sqrt{r}$ . Y tenemos 3 puntos criticos. Y vemos que en la bifurcación, nuestro punto critico en 0 pasa a ser inestable. 

![](Pasted%20image%2020240927183430.png)

**Subcriticas**
Sucede cuando 
$$\dot{x} = x(r+x^2)$$
En este caso tenemos que dentro del parentesis $x^2$ toma siempre un valor positivo. Entonces podran existir diferentes puntos fijos del 0, cuando r sea negativo. Ademas notamos que el unico punto estable es el 0 (cuando r es negativo).

![](Pasted%20image%2020240927184343.png)

![](Pasted%20image%2020240927184156.png)


## EDOs Bidimensionales

## EDOs Tridimensionales
