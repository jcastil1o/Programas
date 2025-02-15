import ply.lex as lex
import time

tokens = ['NUMERO', 'MAS', 'MENOS', 'MULTIPLICAR', 'DIVIDIR']

t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICAR = r'\*'
t_DIVIDIR = r'\/'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Error: (Caracter incorrecto) '%s'" %t.value[0])
    t.lexer.skip(1)
    time.sleep(1)

lexer = lex.lex()
print("\tAnalizador Lexico")
print("Ingrese una operacion matematica: ")
print("\t\tEjemplo: 2 + 2")
lexer.input(input())

while True:
    token = lexer.token()
    if not token:
        print("\nLeyendo cola de tokens...")
        try:
            resultado = eval(lexer.lexdata)
            print(f"\n\033[1m**     Resultado del token: {resultado}    **")
            time.sleep(2)
        except Exception as e:
            print(f"\033[0mError al evaluar la expresión: {e}")
        print("No se encontraron nuevos tokens")
        time.sleep(2)
        break
    print(token)