class Buffer:
    def load_buffer(self):
        arq = open(r'G:\UMG\Plan Sábados\7mo\Compiladores\Programas Compiladores\ProyectoFinalCompiladores-master\MiLenguaje.compi', 'r')
        text = arq.readline()

        buffer = []
        cont = 1

        while text != "":
            buffer.append(text)
            text = arq.readline()
            cont += 1

            if cont == 10 or text == '':
                # Retornamos el buffer
                buf = ''.join(buffer)
                cont = 1
                yield buf

                # Reseteamos el buffer
                buffer = []

        arq.close()