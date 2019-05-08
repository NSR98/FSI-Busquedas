# FSI-Búsquedas
#### Práctica 1. Búsquedas mediante ramificación y acotación con y sin subestimación.

La práctica consiste en añadir dos métodos de búsqueda nuevos al proyecto y comprobar mediante varias pruebas si los resultados mejoran los obtenidos con la búsqueda en anchura y con la búsqueda en profundidad.

El primer método desarrollado es la búsqueda de ramificación y acotación que  se  basa  en  ordenar  la  lista abierta   tomando   como   criterio   el   coste   acumulado   de   cada   trayectoria   parcial, representada ésta por cada nodo de la lista abierta ("path_cost").La función que realiza esta búsqueda se denomina "ramification" y se localiza en el fichero "search.py", donde se realiza la llamada a la función "calculateRamification", del fichero "utils.py", que es la encargada de realizar todo el proceso operacional.

El segundo método implementado es la búsqueda de ramificación y acotación basada en el procedimiento anterior con la peculiridad de que las decisiones tendrán un parámetro más a tener  en cuenta: la heurísitca. En este problema la heurística viene dada y muestra el coste en línea recta desde el nodo origen hasta el nodo destino. La función que lleva a cabo esta búsqueda se denomina "ramification_underestimated" ubicada en "search.py", desde donde llamamos a la función "calculateRamificationUnderestimated".

Cabe mencionar el formato de salida de la ejecución. Se muestran para ambos métodos tanto los nodos visitados como los nodos expandidos, además de la trayectoria que se sigue hasta llegar al destino. Dicha trayectoria debe coincidir para garantizar la búsqueda correcta y la cifra de nodos visitados y expandidos nos permitirá comprobar la eficiencia de ambos algoritmos. 

	------------------- EJEMPLO AB -------------------

	- Ramificación y acotación
	Nodos visitados: 24
	Nodos expandidos: 23
	[<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]

	- Ramificación y acotación con subestimación
	Nodos visitados: 6
	Nodos expandidos: 5
	[<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]


	------------------- EJEMPLO BA -------------------

	- Ramificación y acotación
	Nodos visitados: 29
	Nodos expandidos: 28
	[<Node A>, <Node S>, <Node R>, <Node P>, <Node B>]

	- Ramificación y acotación con subestimación
	Nodos visitados: 5
	Nodos expandidos: 4
	[<Node A>, <Node S>, <Node R>, <Node P>, <Node B>]


	------------------- EJEMPLO AL -------------------

	- Ramificación y acotación
	Nodos visitados: 9
	Nodos expandidos: 8
	[<Node L>, <Node T>, <Node A>]

	- Ramificación y acotación con subestimación
	Nodos visitados: 4
	Nodos expandidos: 3
	[<Node L>, <Node T>, <Node A>]


	------------------- EJEMPLO ER -------------------

	- Ramificación y acotación
	Nodos visitados: 13
	Nodos expandidos: 12
	[<Node R>, <Node P>, <Node B>, <Node U>, <Node H>, <Node E>]

	- Ramificación y acotación con subestimación
	Nodos visitados: 6
	Nodos expandidos: 5
	[<Node R>, <Node P>, <Node B>, <Node U>, <Node H>, <Node E>]


	------------------- EJEMPLO AU -------------------

	- Ramificación y acotación
	Nodos visitados: 30
	Nodos expandidos: 29
	[<Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node A>]

	- Ramificación y acotación con subestimación
	Nodos visitados: 9
	Nodos expandidos: 8
	[<Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node A>]


	------------------- EJEMPLO DO -------------------

	- Ramificación y acotación
	Nodos visitados: 27
	Nodos expandidos: 26
	[<Node O>, <Node S>, <Node R>, <Node C>, <Node D>]

	- Ramificación y acotación con subestimación
	Nodos visitados: 12
	Nodos expandidos: 11
	[<Node O>, <Node S>, <Node R>, <Node C>, <Node D>]


	------------------- EJEMPLO CS -------------------

	- Ramificación y acotación
	Nodos visitados: 6
	Nodos expandidos: 5
	[<Node S>, <Node R>, <Node C>]

	- Ramificación y acotación con subestimación
	Nodos visitados: 3
	Nodos expandidos: 2
	[<Node S>, <Node R>, <Node C>]
	

A la vista de los resultados podemos afirmar rotundamente el beneficio de haber aplicado una heurística adecuada a este problema concreto.  Gracias a esta la cantidad de nodos visitados y expandidos se reduce notablemente para la mayoría de casos. 
