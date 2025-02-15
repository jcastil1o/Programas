import re

def analizador(ingreso):
    tokens = []
    return tokens

code = """
    const nombreUsuario = "Jonathan";
    let edad = 21;
    if (edad >= 18)
    {
        console.log("Es mayor de edad");
    }
"""

tokens = analizador(code)
for token in tokens:
    print(f"{token['Tipo: ']} -> {token['Valor: ']}")

palabras_clave = ['const', 'let', 'function', 'if', 'else', 'return']
