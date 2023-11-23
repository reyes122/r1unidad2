'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 15 de Noviembre
 Description:
 Laboratorio: 3.4.1.13
'''

class WeekDayError(Exception):
    pass

class Weeker:
    # Días de la semana permitidos
    _DAYS = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

    def __init__(self, day):
        # Inicializa el objeto Weeker con el día de la semana proporcionado
        if day not in self._DAYS:
            raise WeekDayError("Día de la semana no válido")
        self._current_day_index = self._DAYS.index(day)

    def __str__(self):
        # Representación en cadena del día de la semana actual
        return self._DAYS[self._current_day_index]

    def add_days(self, n):
        # Añade n días al día de la semana actual
        self._current_day_index = (self._current_day_index + n) % 7

    def subtract_days(self, n):
        # Resta n días al día de la semana actual
        self._current_day_index = (self._current_day_index - n) % 7

# Ejemplo de uso
try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lun')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")

