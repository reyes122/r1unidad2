'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 17 de Noviembre 
 Description:
 Laboratorio: 4.6.1.13
'''

import calendar

# Definición de una nueva clase MyCalendar que hereda de la clase Calendar
class MyCalendar(calendar.Calendar):
    # Definición de un nuevo método count_weekday_in_year
    def count_weekday_in_year(self, year, weekday):
        # Inicialización de variables
        current_month = 1
        number_of_days = 0

        # Iteración a través de los meses del año
        while current_month <= 12:
            # Iteración a través de las semanas del mes
            for data in self.monthdays2calendar(year, current_month):
                # Comprobación si el día de la semana tiene un valor diferente de 0 
                if data[weekday][0] != 0:
                    # Incremento del contador de días
                    number_of_days = number_of_days + 1

            # Incremento del contador de meses
            current_month = current_month + 1

        # Retorno del número total de días encontrados en el año
        return number_of_days

# Creación de una instancia de la clase MyCalendar
my_calendar = MyCalendar()

# Llamada al método count_weekday_in_year para contar el número de días lunes en el año 2019
number_of_days = my_calendar.count_weekday_in_year(2019, calendar.MONDAY)

# Impresión del resultado
print(number_of_days)
