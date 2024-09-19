## Clase 9

Sistemas de ecuaciones diferenciales BIDIMENSIONALES.

Nuestro sistemas tendran la forma

  

$$

\begin{align*}

\dot{x_1} = f_1(x_1,x_2) \\

\dot{x_2} = f_2(x_1,x_2)

\end{align*}

$$

  

Lo que queremos encontrar son dos funciones $x_1(t),x_2(t)$ . En este sistema, estas funciones estan acopladas. Entonces ahora lo que buscamos son dos funciones que al ser derivadas con respecto al tiempo nos den $f_1, f_2$

  

Tener sistemas de dos dimensiones, nos permite tener soluciones **oscilatorias**. En una dimension cuando tenemos un punto fijo, solo podemos aproximarnos a el desde un lado y quedarnos allí. Con dos dimensiones podemos tener una variable fija y otra oscilando.

Donde $x_1(t),x_2(t)$ son mis funciones incógnitas.

  

![Pasted image 20240909181614 1.png](imgs/Pasted%20image%2020240909181614%201.png)

  

Lo que vamos a hacer es obtener aproximaciones de las funciones $x_1,x_2$ en diferentes tiempos t para poder asi reconstruir la **trayectoria** del sistema.

  

![Pasted image 20240917200716.png](imgs/Pasted%20image%2020240917200716.png)

  

El tiempo t parametriza la curva pero no aparece explicitamente. También se puede ver como $\dot{\overline{x}}(t)$ representa la velocidad de cambio de la curva.

  

Al igual que en las ecuaciones unidimensionales, también existe:

  

![Pasted image 20240912155719 1.png](imgs/Pasted%20image%2020240912155719%201.png)

  

En estos sistemas nuestro **punto fijo** sera $\bar{x}* = (x*,y*)$ tal que al evaluar las funciones $f_1,f_2$ en dichos valores las razones de cambio permanecen en 0.

  

Ahora pasamos a describir el problema desde dicho punto fijo de manera generalizada, dado un punto fijo sabremos que ($f_1 = f, f_2=g$)

  

$$

\begin{align*}

f(x*,y*) = 0 \\ g(x*,y*) = 0

\end{align*}

$$

  

$$

\begin{align*}

\dot{x} &= f(x,y) \\

\dot{y} &= g(x,y) \\

\end{align*}

$$

"corremos" el eje de coordenadas y mantenemos nuestro centro en dicho punto critico.

  

$$\text{Reescribimos nuestras funciones x e y}$$

$$

\begin{align*}

x = x* + u &\qquad \dot{x} = \dot{u} \\

y = y* + v &\qquad \dot{y} = \dot{v} \\

\end{align*}

$$

  

![Pasted image 20240917202450.png](imgs/Pasted%20image%2020240917202450.png)

  

De esta forma podemos describir como se comporta el sistema al rededor de cada punto fijo.

Como $\dot{x} = f(x,y)$ , usando las igualdades anteriores puedo reescribir (reemplazando correctamente, y utilizando taylor para representar las funciones f y g)

  

![alt text](imgs/Pasted%20image%2020240917203349%201.png)

  

y eliminando el resto me quedo con que:

  

$$

\begin{align*}

\dot{u} \approx u\frac{df}{dx}_{x*,y*} + v\frac{df}{dy}_{x*,y*} \\

\dot{v} \approx u\frac{dg}{dx}_{x*,y*} + v\frac{dg}{dy}_{x*,y*} \\

\end{align*}

$$

  

Y de esta forma tengo un sistema de ecuaciones diferenciales acopladas lineal. que lo puedo escribir:

![](imgs/Pasted%20image%2020240919095327.png)

A esta matriz se la llama Jacobiano del punto fijo de la ecuación bidimensional. Linealiza mi problema al rededor del punto fijo.

Entonces cuando tengo un sistema de ecuaciones diferenciales acoplado, ya encontre la forma de obtener una **aproximación lineal** del mismo a partir de:

1. Encontrar puntos fijos
2. Crear matriz jacobiana a partir de dicho punto fijo.

Ahora queremos encontrar un sistema de coordenadas (rotando y trasladando) que nos de una representación mas sencilla del problema. Esto lo hago descomponiendo en **autovalores y autovectores**.

![alt text](imgs/Pasted%20image%2020240917211925%201.png)

Encontrar el determinante (y los auto-vectores y auto-valores) me permite poder **diagonalizar** la matriz A de forma que desde ese eje de coordenadas, yo veo que mi sistema se a **desacoplado** es decir no dependen entre si.