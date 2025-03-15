import re

class TablaDeSimbolos:
    def __init__(self):
        self.tabla = {}

    def declarar_variable(self, nombre, tipo):
        if nombre in self.tabla:
            print(f"Advertencia: La variable '{nombre}' ya ha sido declarada.")
        self.tabla[nombre] = tipo

    def obtener_tipo(self, nombre):
        if nombre not in self.tabla:
            raise Exception(f"Error: La variable '{nombre}' no está declarada.")
        return self.tabla[nombre]

class AnalizadorSemantico:
    def __init__(self):
        self.tabla_simbolos = TablaDeSimbolos()

    def declarar(self, nombre, tipo):
        self.tabla_simbolos.declarar_variable(nombre, tipo)

    def verificar_expresion(self, expr):
        tokens = re.findall(r"[a-zA-Z_]\w*|\d+|[+\-*/]", expr)
        if not tokens:
            raise Exception("Error: Expresión vacía o inválida.")

        # Verificar si todos los operandos están declarados
        operandos = [token for token in tokens if token.isalpha()]
        for op in operandos:
            self.tabla_simbolos.obtener_tipo(op)

        # Determinar el tipo de la expresión
        tipos = [self.tabla_simbolos.obtener_tipo(op) if op.isalpha() else "int" for op in tokens if re.match(r"[a-zA-Z_]\w*|\d+", op)]
        
        if "float" in tipos:
            return "float"  # Promoción implícita si hay un float
        return "int"

# Ejecución interactiva
analizador = AnalizadorSemantico()

# Declaraciones de variables
n = int(input("Ingrese el número de variables a declarar: "))
for _ in range(n):
    nombre = input("Nombre de la variable: ")
    tipo = input("Tipo (int o float): ")
    analizador.declarar(nombre, tipo)

# Evaluación de expresiones
while True:
    try:
        expresion = input("\nIngrese una expresión (o 'salir' para terminar): ")
        if expresion.lower() == "salir":
            break
        tipo_resultado = analizador.verificar_expresion(expresion)
        print(f"Tipo de la expresión '{expresion}': {tipo_resultado}")
    except Exception as e:
        print(e)
        # Mostrar la tabla de símbolos
        print("\nTabla de Símbolos:")
        for nombre, tipo in analizador.tabla_simbolos.tabla.items():
            print(f"{nombre}: {tipo}")

        # Mostrar la tabla de derivación
        print("\nTabla de Derivación:")
        for token in re.findall(r"[a-zA-Z_]\w*|\d+|[+\-*/]", expresion):
            print(f"Token: {token}")

        # Mostrar el árbol semántico
        print("\nÁrbol Semántico:")
        def mostrar_arbol(tokens, nivel=0):
            if not tokens:
                return
            token = tokens.pop(0)
            print("  " * nivel + f"Token: {token}")
            if token in "+-*/":
                mostrar_arbol(tokens, nivel + 1)
                mostrar_arbol(tokens, nivel + 1)
        tokens = re.findall(r"[a-zA-Z_]\w*|\d+|[+\-*/]", expresion)
        mostrar_arbol(tokens)
        print("\nTabla de Símbolos:")
        for nombre, tipo in analizador.tabla_simbolos.tabla.items():
            print(f"{nombre}: {tipo}")

        # Mostrar la tabla de derivación
        print("\nTabla de Derivación:")
        for token in re.findall(r"[a-zA-Z_]\w*|\d+|[+\-*/]", expresion):
            print(f"Token: {token}")

        # Mostrar el árbol semántico
        print("\nÁrbol Semántico:")
        def mostrar_arbol(tokens, nivel=0):
            if not tokens:
                return
            token = tokens.pop(0)
            print("  " * nivel + f"Token: {token}")
            if token in "+-*/":
                mostrar_arbol(tokens, nivel + 1)
                mostrar_arbol(tokens, nivel + 1)
        tokens = re.findall(r"[a-zA-Z_]\w*|\d+|[+\-*/]", expresion)
        mostrar_arbol(tokens)