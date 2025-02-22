class LL1Parser:
    def __init__(self, grammar, table):
        self.grammar = grammar
        self.table = table

    def parse(self, input_string):
        STACK_END = '$'
        stack = [STACK_END, self.grammar['start']]
        input_string += STACK_END

        input_index = 0
        derivation = []

        while stack:
            top = stack[-1]
            current_input = input_string[input_index]

            if top == current_input:
                if top == STACK_END:
                    return True, derivation, None  # Aceptación
                stack.pop()
                input_index += 1
            elif top in self.grammar['non_terminals']:
                if current_input in self.table and top in self.table[current_input]:
                    production = self.table[current_input][top]
                    stack.pop()
                    derivation.append(production)
                    symbols = self.grammar['productions'][production]
                    for symbol in reversed(symbols):
                        if symbol != 'ε':
                            stack.append(symbol)
                else:
                    return False, derivation, f"Error: No entry in table for symbol '{current_input}' and non-terminal '{top}' at position {input_index}."
            else:
                return False, derivation, f"Error: Unexpected symbol '{current_input}', expected '{top}' at position {input_index}."

        return False, derivation, "Error: Parsing failed."

grammar = {
    'non_terminals': ['E', 'T', 'F'],
    'terminals': ['id', '+', '*', '(', ')'],
    'start': 'E',
    'productions': {
        'E -> T E\'': ['T', 'E\''],
        'E\' -> + T E\'': ['+', 'T', 'E\''],
        'E\' -> ε': ['ε'],
        'T -> F T\'': ['F', 'T\''],
        'T\' -> * F T\'': ['*', 'F', 'T\''],
        'T\' -> ε': ['ε'],
        'F -> ( E )': ['(', 'E', ')'],
        'F -> id': ['id']
    }
}

table = {
    'id': {'E': 'E -> T E\'', 'T': 'T -> F T\'', 'F': 'F -> id'},
    '+': {'E\'': 'E\' -> + T E\''},
    '*': {'T\'': 'T\' -> * F T\''},
    '(': {'E': 'E -> T E\'', 'T': 'T -> F T\'', 'F': 'F -> ( E )'},
    ')': {'E\'': 'E\' -> ε', 'T\'': 'T\' -> ε'},
    '$': {'E\'': 'E\' -> ε', 'T\'': 'T\' -> ε'}
}


accepted_string = "E$"
rejected_string = "(id+id)*id"


parser = LL1Parser(grammar, table)


result, derivation, error = parser.parse(accepted_string)
if result:
    print("Resultado: Aceptado")
    print("Derivación:", derivation)
else:
    print("Resultado: Rechazado")
    print("Derivación:", derivation)
    print("Error:", error)


result, derivation, error = parser.parse(rejected_string)
if result:
    print("Resultado: Aceptado")
    print("Derivación:", derivation)
else:
    print("Resultado: Rechazado")
    print("Derivación:", derivation)
    print("Error:", error)