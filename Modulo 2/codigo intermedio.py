class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def construir_arbol(expresion):
    """Construye un árbol de derivación a partir de una expresión aritmética."""

    operadores = ['+', '-', '*', '/']
    pila_nodos = []
    pila_operadores = []

    def precedencia(operador):
        if operador in ['+', '-']:
            return 1
        elif operador in ['*', '/']:
            return 2
        return 0

    def aplicar_operador():
        operador = pila_operadores.pop()
        derecha = pila_nodos.pop()
        izquierda = pila_nodos.pop()
        nodo = Nodo(operador, izquierda, derecha)
        pila_nodos.append(nodo)

    i = 0
    while i < len(expresion):
        if expresion[i].isdigit():
            j = i
            while j < len(expresion) and expresion[j].isdigit():
                j += 1
            nodo = Nodo(expresion[i:j])
            pila_nodos.append(nodo)
            i = j
        elif expresion[i] in operadores:
            while pila_operadores and precedencia(pila_operadores[-1]) >= precedencia(expresion[i]):
                aplicar_operador()
            pila_operadores.append(expresion[i])
            i += 1
        elif expresion[i] == '(':
            pila_operadores.append(expresion[i])
            i += 1
        elif expresion[i] == ')':
            while pila_operadores[-1] != '(':
                aplicar_operador()
            pila_operadores.pop()  # Eliminar el '('
            i += 1
        else:
            i += 1

    while pila_operadores:
        aplicar_operador()

    return pila_nodos[0]

def imprimir_arbol(nodo, sangria=""):
    """Imprime el árbol de derivación."""

    if nodo:
        print(sangria + nodo.valor)
        imprimir_arbol(nodo.izquierda, sangria + "  ")
        imprimir_arbol(nodo.derecha, sangria + "  ")

# Ejemplo de uso
expresion = "3 + 4 * (2 - 1)"
arbol = construir_arbol(expresion)
imprimir_arbol(arbol)