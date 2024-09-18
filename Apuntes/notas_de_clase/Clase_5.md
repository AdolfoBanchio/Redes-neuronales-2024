# Clase 5

## El problema de valor inicial

dada una ecuacion diferencial
$$
\dot{x} = f(x,t)
$$
tenemos infinitas soluciones a partir de la condición inicial $x(t=t_0)=x_0=\alpha$  
pero podemos determinar una única trayectoria de interés entre las infinitas posibles.

![Pasted image 20240826182003 1.png](imgs/Pasted%20image%2020240826182003%201.png)

la trayectoria es lo naranja, vemos que se aleja de la solución real. Y ese error se puede estimar a partir de el tamaño del paso h y del método utilizado para calcular dichos pasos.

Obtenemos dicha trayectoria en un **conjunto de puntos** espaciados por *h* .

![Pasted image 20240826182324.png](imgs/Pasted%20image%2020240826182324.png)

- n: dimension de mi problema, dimension de x.
- en general usamos 0 como nuestro valor inicial.
  
![Pasted image 20240828135828 1.png](imgs/Pasted%20image%2020240828135828%201.png)

En general, alcanza que la razón de cambio (el lado derecho de la EDO) sea una función "un poco suave" para que la solución exista y sea única. Es decir, no existen dos trayectorias que se crucen en un mismo instante t, pues eso supondría que existen dos razones de cambio diferentes.
