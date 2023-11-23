'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 16 de Noviembre
 Description:
 Laboratorio: 3.4.1.15
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

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        # Constructor que inicializa los tres vértices del triángulo.
        self._vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        # Método que calcula y devuelve el perímetro del triángulo.
        side1 = self._vertices[0].distance_from_point(self._vertices[1])
        side2 = self._vertices[1].distance_from_point(self._vertices[2])
        side3 = self._vertices[2].distance_from_point(self._vertices[0])
        return side1 + side2 + side3

# Ejemplo de uso
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
