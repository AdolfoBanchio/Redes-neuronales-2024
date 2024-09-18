# Clase 3

# Sistemas dinámicos

Un sistema dinámico es cualquier sistema físico cuyo estado evoluciona con el tiempo, nos permiten modelar y ganar capacidad preventiva e la neurociencia teórica y computacional.

- Sistemas dinámicos continuos: las variables que describen el estado del sistema toman valores continuos y sus razones de cambio se rigen por ecuaciones diferenciales ordinarias

![Pasted image 20240826110533.png](imgs/Pasted%20image%2020240826110533.png)

- Sistemas dinámicos discretos: las variables que describen el estado son relaciones de recurrencia. La variable independiente de tiempo es discreta. Las variables del estado del sistema pueden ser discretas o continuas.

Nos vamos a concentrar en **Sistemas dinámicos continuos**

Existen sistemas que estan descriptos por una única variable continua **x**. Que cambia con el tiempo y para ello tenemos la funcion **x(t)** para cierto dominio **D** de la variable **t**.
$$
\begin{align*}
t \in \mathbb{R} \\
x(t) \in \mathbb{R}
\end{align*}
$$
Tener un **modelo** es tener una ecuación que nos permita deducir o aproximar la función **x(t)**. Deducimos como depende la razón de cambio de **x** del tiempo **t**.
Podemos aproximar **x(t)** a partir de una **ecuación diferencial ordinaria**:
$$
\frac{dx(t)}{dt} = f(x(t), t)
$$
La razón de cambio puede depender explícitamente de **t** y también implícitamente a través de la variable **x**.

Estos sistemas son unidimensionales pues una única variable describe el estado del sistema,

Si el tiempo t no aparece explicitamente en la razón de cambio **f**, decimos que la ecuación diferencial ordinaria es autónoma. Y el sistema es **AUTÓNOMO**.

Todo sistema no autónomo se puede reducir a un sistema autónomo. Por lo que nos centraremos en sistemas que tienen **n** variables dinámicas y que cada una depende solo del tiempo **t**. En este caso la dinámica de nuestro sistema estará descrita por un sistema de **n** ecuaciones diferenciales ordinarias de la forma:

![Pasted image 20240826113219 1.png](imgs/Pasted%20image%2020240826113219%201.png)
