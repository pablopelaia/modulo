Ejercicio realizado en Python para resolver un puzzle matemático solicitado en una búsqueda de trabajo. Cabe aclarar que en dicha búsqueda pedían resolusión en java, pero al estar estudiando Python en este momento intenté realizarlo en dicho lenguaje.

Logré llegar a la respuesta con un código que logré simplificarlo tras estudiar el comprotamiento de la operación módulo con las distintas operaciones matemáticas utilizadas para resolver el problema. De esta manera, un código que parecía imposible resolver con los recursos de una notebook por la cantidad de operaciones que implicaría, con estas reglas matemáticas encontradas, pude realizar un código que resuelve el problema en un par de segundos y podría resolver cualquier otro número entero que se le agregara sin ningún inconveniente.

Actualizaron el desafío ahora el mismo es módulo 2021 y el número buscado es el 67489454811002199

¡Desafío para desarrolladores!

Si te interesa participar postulate a la búsqueda, para luego poder enviar la solución del siguiente puzzle.

¿Podrías decirnos cuál es el resultado de ejecutar el siguiente código? (suponiendo que la máquina tiene los recursos suficientes para terminar de ejecutarlo). Por favor no olvides comentarnos cuál fue tu razonamiento para llegar al resultado.

Puzzle.java

import java.math.BigInteger;

class Puzzle {

final static BigInteger M = new BigInteger("2017");

private static BigInteger compute(long n) {

String s = "";

for (long i = 0; i < n; i++) {

s = s + n;

}

return new BigInteger(s.toString()).mod(M);

}

public static void main(String args[]) {

for (long n : new long[] { 1L, 2L, 5L, 10L, 20L, 58184241583791680L }) {

System.out.println("" + n + ": " + compute(n));

}

}

}

Resultado parcial por consola

$ javac Puzzle.java

$ java Puzzle

1: 1

2: 22

5: 1096

10: 1197

20: 57

58184241583791680: ...
