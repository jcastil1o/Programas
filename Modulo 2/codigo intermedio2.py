class NodoNumeroBinario:
    def __init__(self, valor):
        self.valor = valor

class NodoVariable:
    def __init__(self, nombre):
        self.nombre = nombre

class NodoOperacionBinaria:
    def __init__(self, operador, operando_izquierdo, operando_derecho):
        self.operador = operador
        self.operando_izquierdo = operando_izquierdo
        self.operando_derecho = operando_derecho

class NodoAsignacion:
    def __init__(self, variable, expresion):
        self.variable = variable
        self.expresion = expresion

class GeneradorCodigo3AC:
    def __init__(self):
        self.temporales = 0
        self.codigo_3ac = []

    def generar_temporal(self):
        self.temporales += 1
        return f"t{self.temporales}"

    def generar_codigo(self, nodo):
        if isinstance(nodo, NodoNumeroBinario):
            return str(nodo.valor) + "B"
        elif isinstance(nodo, NodoVariable):
            return nodo.nombre
        elif isinstance(nodo, NodoOperacionBinaria):
            izquierdo = self.generar_codigo(nodo.operando_izquierdo)
            derecho = self.generar_codigo(nodo.operando_derecho)
            temporal = self.generar_temporal()
            self.codigo_3ac.append(f"{temporal} = {izquierdo} {nodo.operador} {derecho}")
            return temporal
        elif isinstance(nodo, NodoAsignacion):
            resultado = self.generar_codigo(nodo.expresion)
            self.codigo_3ac.append(f"{nodo.variable} = {resultado}")
            self.codigo_3ac.append(f"{nodo.variable} = {resultado}")
            return resultado

    def obtener_codigo_3ac(self):
        return self.codigo_3ac
    
# Ejemplo de uso
ast = [
    NodoAsignacion("a", NodoNumeroBinario("1010")),
    NodoAsignacion("b", NodoNumeroBinario("1100")),
    NodoAsignacion("c", NodoOperacionBinaria("&", NodoVariable("a"), NodoVariable("b"))),
    NodoAsignacion("d", NodoOperacionBinaria("<<", NodoVariable("a"), NodoNumeroBinario(2))),
    NodoAsignacion("e", NodoOperacionBinaria("|", NodoVariable("c"), NodoVariable("d"))),
]

generador = GeneradorCodigo3AC()
for nodo in ast:
    generador.generar_codigo(nodo)

codigo_3ac = generador.obtener_codigo_3ac()
for linea in codigo_3ac:
    print(linea)