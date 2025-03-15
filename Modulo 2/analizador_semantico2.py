import re

class TablaDeSimbolos:
    def __init__(self):
        self.tabla = {}

    def declarar_variable(self, nombre, tipo):
        if nombre in self.tabla:
            print(f"⚠️ Advertencia: La variable '{nombre}' ya ha sido declarada.")
        self.tabla[nombre] = tipo

    def obtener_tipo(self, nombre):
        if nombre not in self.tabla:
            raise Exception(f"❌ Error: La variable '{nombre}' no está declarada.")
        return self.tabla[nombre]

    def mostrar_tabla(self):
        print("\n📌 Tabla de Símbolos:")
        for nombre, tipo in self.tabla.items():
            print(f"---------------------")
            print(f"| {nombre}:| {tipo}    |")
            print(f"---------------------")

class AnalizadorSemantico:
    def __init__(self):
        self.tabla_simbolos = TablaDeSimbolos()

    def declarar(self, nombre, tipo):
        self.tabla_simbolos.declarar_variable(nombre, tipo)

    def verificar_expresion(self, expr):
        tokens = re.findall(r"[a-zA-Z_]\w*|\d+|[+\-*/]", expr)
        if not tokens:
            raise Exception("❌ Error: Expresión vacía o inválida.")

        operandos = [token for token in tokens if token.isalpha()]
        for op in operandos:
            self.tabla_simbolos.obtener_tipo(op)

        tipos = [self.tabla_simbolos.obtener_tipo(op) if op.isalpha() else "int" for op in tokens if re.match(r"[a-zA-Z_]\w*|\d+", op)]
        
        if "float" in tipos:
            return "float"
        return "int"

    def mostrar_arbol(self, expr):
        tokens = re.findall(r"[a-zA-Z_]\w*|\d+|[+\-*/]", expr)
        print("\n🌳 Árbol Semántico:")
        
        def construir_arbol(tokens, nivel=0):
            if not tokens:
                return
            token = tokens.pop(0)
            print("  " * nivel + f"📌 {token}")
            if token in "+-*/":
                construir_arbol(tokens, nivel + 1)
                construir_arbol(tokens, nivel + 1)
        
        construir_arbol(tokens)

analizador = AnalizadorSemantico()

n = int(input("📝 Ingrese el número de variables a declarar: "))
for _ in range(n):
    nombre = input("🔹 Nombre de la variable: ")
    tipo = input("🔹 Tipo (int o float): ")
    analizador.declarar(nombre, tipo)

while True:
    print("\n📌 Opciones:")
    print("  1️⃣ Ingresar expresión y evaluar tipo")
    print("  2️⃣ Mostrar tabla de símbolos")
    print("  3️⃣ Mostrar árbol semántico de una expresión")
    print("  4️⃣ Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        expresion = input("\n✏️ Ingrese una expresión: ")
        try:
            tipo_resultado = analizador.verificar_expresion(expresion)
            print(f"✅ Tipo de la expresión '{expresion}': {tipo_resultado}")
        except Exception as e:
            print(e)

    elif opcion == "2":
        analizador.tabla_simbolos.mostrar_tabla()

    elif opcion == "3":
        expresion = input("\n🌱 Ingrese una expresión para ver su árbol semántico: ")
        try:
            analizador.mostrar_arbol(expresion)
        except Exception as e:
            print(e)

    elif opcion == "4":
        print("👋 Saliendo del programa...")
        break

    else:
        print("❌ Opción inválida. Intente nuevamente.")
