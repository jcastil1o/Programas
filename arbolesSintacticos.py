import graphviz

def generar_arbol(reglas):
    dot = graphviz.Digraph()
    for regla in reglas:
        padre, hijos = regla[0], regla[1:]
        dot.node(padre)
        for hijo in hijos:
            dot.node(hijo)
            dot.edge(padre, hijo)
    return dot

# Ejemplo para la cadena "id"
reglas_id = [('E', 'T'), ('T', 'F'), ('F', 'id')]
arbol_id = generar_arbol(reglas_id)
arbol_id.render('arbol_id', format='pdf', cleanup=True)