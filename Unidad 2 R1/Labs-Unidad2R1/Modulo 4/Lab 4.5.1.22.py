'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 17 de Noviembre 
 Description:
 Laboratorio: 4.5.1.22
'''
from datetime import datetime

# Crear objeto datetime para el 4 de noviembre de 2020, 14:53:00
fecha_hora = datetime(2020, 11, 4, 14, 53, 0)

# Mostrar resultados utilizando strftime con diferentes formatos
print(fecha_hora.strftime("%Y/%m/%d %H:%M:%S"))
print(fecha_hora.strftime("%y/%B/%d %I:%M:%S %p"))
print(fecha_hora.strftime("%a, %Y %b %d"))
print(fecha_hora.strftime("%A, %Y %B %d"))
print(f"Día de la semana: {fecha_hora.strftime('%w')}")
print(f"Día del año: {fecha_hora.strftime('%j')}")
print(f"Número de semana en el año: {fecha_hora.strftime('%U')}")
