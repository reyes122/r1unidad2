'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 15 de Noviembre
 Description:
 Laboratorio: 3.2.1.16
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

    def is_empty(self):
        return not bool(self._data)  # Devuelve True si la cola está vacía, False de lo contrario.

# Ejemplo de uso
que = Queue()
que.put(1)
que.put("perro")
que.put(False)

# Imprime los elementos de la cola y verifica si está vacía
for i in range(4):
    if que.is_empty():
        print("Cola vacía")
        break
    print(que.get())

# Verifica si la cola está vacía después de la extracción de elementos
print("Cola vacía:", que.is_empty())


