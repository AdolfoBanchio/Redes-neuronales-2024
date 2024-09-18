# Clase 8

## Bifurcaciones y parámetros

Analizamos las bifurcaciones para EDOs unidimensionales.
Veamos como ejemplo la función $$\dot{x} = r+x^2$$
En este caso, el r sera un parámetro **externo** al sistema.

![Pasted image 20240905183648 1.png](imgs/Pasted%20image%2020240905183648%201.png)

En este caso, los diferentes valores de r nos da diferentes puntos criticos de la ecuación diferencial. Lo que buscamos es encontrar el punto ($r_c$)tal que es el ultimo valor de x(t) tal  que $\dot{x}$ tiene dos puntos criticos. En este ejemplo vemos que para r mayor que 0 la ecuación diferencial tiene un punto estable. Cuando pasa el 0, estos puntos x* se bifurcan. Por lo que **r=0** es nuestro $r_c$ .

![Pasted image 20240905185155.png](imgs/Pasted%20image%2020240905185155.png)

### Formas normales

Existen funciones que son mas difíciles de resolver para ello buscamos llevarlo a formas normales.

Por el teorema de Taylor, podemos expresar cualquier función infinita en una serie de polinomios para poder obtener una aproximación en un intervalo especifico sabiendo de cuanto es el error.

De esta forma podemos obtener una aproximación polinomica cuando los valores de x esten cercanos a x* dado un cierto $r_c$

 Para obtener x* y r_c debo primero igualar la ecuacion diferencial a 0 y despejar x(t) y quedara algo en funcion de mi parametro r. De ahi a partir de las graficas debo encontrar cual es el r_c

![Pasted image 20240905185602 1.png](imgs/Pasted%20image%2020240905185602%201.png)

Para este caso, el punto critico sera cuando r este cercano a 1.

Esto nos dice que muchas ecuaciones diferenciales no polinomiales con diferentes parametros de condicion inicial, Podemos mediante series de Taylor llevarlos con un correcto cambio de variables a expresiones polinomicas mas facil de interpretar.
COMO?
![Pasted image 20240905190232.png](imgs/Pasted%20image%2020240905190232.png)

Desarrollo la serie de Taylor centrada en  **x**** y $r_c$ (Dos dimensiones).

![Pasted image 20240905190505 1.png](imgs/Pasted%20image%2020240905190505%201.png)

De esta forma puedo obtener una función mas sencilla para poder evaluar la ecuación diferencial al rededor de mi parámetro r y mi punto critico **x**** de interés.

En general estas formas normales tendrán una forma polinomica mas alguna dependencia con el parámetro r. (Siempre para obtener esta forma normal debo tener mi x* y $r_c$)

Existen diferentes tipos de bifurcaciones que representan diferentes comportamientos de sistemas

![Pasted image 20240912155255.png](imgs/Pasted%20image%2020240912155255.png)

En este ejemplo, a partir de cierto valor del parametro $\beta$ , nos econtramos con que tenemos dos posibles valores de x que se estabilizan.
