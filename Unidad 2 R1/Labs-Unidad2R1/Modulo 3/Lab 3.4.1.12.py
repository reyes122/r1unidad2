'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 15 de Noviembre
 Description:
 Laboratorio: 3.4.1.12
'''


class Timer:
    def __init__(self, initial_hours=0, initial_minutes=0, initial_seconds=0):
        # Inicializa el temporizador con horas, minutos y segundos dados.
        self._hours = initial_hours
        self._minutes = initial_minutes
        self._seconds = initial_seconds

    def __str__(self):
        # Representación en cadena del temporizador con ceros a la izquierda cuando sea necesario.
        return f"{self._format_digit(self._hours)}:{self._format_digit(self._minutes)}:{self._format_digit(self._seconds)}"

    def _format_digit(self, value):
        # Agrega ceros a la izquierda cuando sea necesario para asegurar dos dígitos.
        return str(value).rjust(2, '0')

    def next_second(self):
        # Incrementa el tiempo almacenado en el temporizador en un segundo.
        self._seconds += 1
        if self._seconds == 60:
            self._seconds = 0
            self._minutes += 1
            if self._minutes == 60:
                self._minutes = 0
                self._hours += 1
                if self._hours == 24:
                    self._hours = 0

    def prev_second(self):
        # Decrementa el tiempo almacenado en el temporizador en un segundo.
        self._seconds -= 1
        if self._seconds == -1:
            self._seconds = 59
            self._minutes -= 1
            if self._minutes == -1:
                self._minutes = 59
                self._hours -= 1
                if self._hours == -1:
                    self._hours = 23

# Ejemplo de uso
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

