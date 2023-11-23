'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 14 de Noviembre
 Description:
 Laboratorio: 3.2.1.14
'''

class Stack:
    def __init__(self):
        self.__stk = []  # Inicializa una lista privada para almacenar elementos.

    def push(self, val):
        self.__stk.append(val)  # Agrega un elemento al final de la lista.

    def pop(self):
        val = self.__stk[-1]  # Obtiene el último elemento de la lista.
        del self.__stk[-1]  # Elimina el último elemento de la lista.
        return val  # Devuelve el valor obtenido.

class CountingStack(Stack):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase base.
        self.__counter = 0  # Inicializa el contador en cero en el constructor.

    def get_counter(self):
        return self.__counter  # Devuelve el valor actual del contador.

    def pop(self):
        val = super().pop()  # Llama al método pop de la clase base.
        self.__counter += 1  # Incrementa el contador al hacer un pop.
        return val  # Devuelve el valor obtenido.

# Ejemplo de uso
stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()

print(stk.get_counter())  # Imprime el valor final del contador.
