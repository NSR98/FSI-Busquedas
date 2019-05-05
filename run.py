# Search methods
import search

'''
# BÚSQUEDA EN ANCHURA Y PROFUNDIDAD, AB
print("\n------------------- EJEMPLO AB -------------------")
print(search.breadth_first_graph_search(ab).path())
print("\n-------- Búsqueda en profundidad --------")
print(search.depth_first_graph_search(ab).path())
'''

# COMPARATIVA RAMIFICACIÓN Y ACOTACIÓN VS RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACIÓN

# PRUEBA AB
ab = search.GPSProblem('A', 'B'
                       , search.romania)
print("------------------- EJEMPLO AB -------------------")
print("\n- Ramificación y acotación")
print(search.ramification(ab).path())
print("\n- Ramificación y acotación con subestimación")
print(search.ramification_underestimated(ab).path())


# PRUEBA BA
ba = search.GPSProblem('B', 'A'
                       , search.romania)
print("\n\n------------------- EJEMPLO BA -------------------")
print("\n- Ramificación y acotación")
print(search.ramification(ba).path())
print("\n- Ramificación y acotación con subestimación")
print(search.ramification_underestimated(ba).path())


# PRUEBA AL
al = search.GPSProblem('A', 'L'
                       , search.romania)
print("\n\n------------------- EJEMPLO AL -------------------")
print("\n- Ramificación y acotación")
print(search.ramification(al).path())
print("\n- Ramificación y acotación con subestimación")
print(search.ramification_underestimated(al).path())


# PRUEBA ER
er = search.GPSProblem('E', 'R'
                       , search.romania)
print("\n\n------------------- EJEMPLO ER -------------------")
print("\n- Ramificación y acotación")
print(search.ramification(er).path())
print("\n- Ramificación y acotación con subestimación")
print(search.ramification_underestimated(er).path())


# PRUEBA AU
au = search.GPSProblem('A', 'U'
                       , search.romania)
print("\n\n------------------- EJEMPLO AU -------------------")
print("\n- Ramificación y acotación")
print(search.ramification(au).path())
print("\n- Ramificación y acotación con subestimación")
print(search.ramification_underestimated(au).path())


# PRUEBA DO
do = search.GPSProblem('D', 'O'
                       , search.romania)
print("\n\n------------------- EJEMPLO DO -------------------")
print("\n- Ramificación y acotación")
print(search.ramification(do).path())
print("\n- Ramificación y acotación con subestimación")
print(search.ramification_underestimated(do).path())


# PRUEBA CS
cs = search.GPSProblem('C', 'S'
                       , search.romania)
print("\n\n------------------- EJEMPLO CS -------------------")
print("\n- Ramificación y acotación")
print(search.ramification(cs).path())
print("\n- Ramificación y acotación con subestimación")
print(search.ramification_underestimated(cs).path())

