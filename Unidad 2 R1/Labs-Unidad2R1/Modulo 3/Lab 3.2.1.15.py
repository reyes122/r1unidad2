'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 15 de Noviembre
 Description:
 Laboratorio: 3.2.1.15
'''

class QueueError(Exception):
    pass  # Define la excepción base para la cola.

class Queue:
    def __init__(self):
        self._data = []  # Inicializa una lista para almacenar elementos en la cola.

    def put(self, elem):
        self._data.insert(0, elem)  # Agrega un elemento al principio de la lista (modelo FIFO).

    def get(self):
        if not self._data:
            raise QueueError("La cola está vacía")  # Lanza la excepción si la cola está vacía al intentar obtener un elemento.
        return self._data.pop()  # Elimina y devuelve el último elemento de la lista (modelo FIFO).

# Ejemplo de uso
que = Queue()
que.put(1)
que.put("perro")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Error de Cola")

