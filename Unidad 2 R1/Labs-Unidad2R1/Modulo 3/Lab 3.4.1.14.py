'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 16 de Noviembre
 Description:
 Laboratorio: 3.4.1.14
'''

import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        # Constructor que inicializa las coordenadas x e y del punto.
        self._x = x
        self._y = y

    def getx(self):
        # Método que devuelve la coordenada x del punto.
        return self._x

    def gety(self):
        # Método que devuelve la coordenada y del punto.
        return self._y

    def distance_from_xy(self, x, y):
        # Método que calcula y devuelve la distancia entre el punto y otro punto definido por las coordenadas (x, y).
        return math.hypot(self._x - x, self._y - y)

    def distance_from_point(self, point):
        # Método que calcula y devuelve la distancia entre el punto y otro punto definido por un objeto de la clase Point.
        return math.hypot(self._x - point.getx(), self._y - point.gety())

# Ejemplo de uso
point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))  # Distancia entre point1 y point2
print(point2.distance_from_xy(2, 0))       # Distancia entre point2 y el punto (2, 0)
