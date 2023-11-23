'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 16 de Noviembre 
 Description:
 Laboratorio: 4.3.1.17
'''
class StudentsDataException(Exception):
    pass


class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_content):
        self.line_number = line_number
        self.line_content = line_content
        super().__init__(f"Error in line {line_number}: {line_content}")


class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__("Error: El archivo está vacío.")


def process_student_data(file_name):
    # Crear un diccionario para almacenar la suma de puntos por estudiante
    student_points = {}

    try:
        # Abrir el archivo y leer su contenido
        with open(file_name, 'r') as file:
            lines = file.readlines()

            # Verificar si el archivo está vacío
            if not lines:
                raise FileEmpty()

            # Procesar cada línea del archivo
            for line_number, line in enumerate(lines, start=1):
                try:
                    # Dividir la línea en nombre, apellido y puntos
                    name, last_name, points_str = line.split()

                    # Convertir los puntos a un número flotante
                    points = float(points_str)

                    # Actualizar la suma de puntos para el estudiante
                    student_points[(name, last_name)] = student_points.get((name, last_name), 0) + points

                except ValueError:
                    raise WrongLine(line_number, line.strip())

    except FileNotFoundError:
        raise StudentsDataException("Error: Archivo no encontrado.")
    except StudentsDataException as e:
        print(e)
    except Exception as e:
        print(f"Error: {e}")
    else:
        # Imprimir el informe ordenado
        sorted_report = sorted(student_points.items(), key=lambda x: x[0])
        for (name, last_name), total_points in sorted_report:
            print(f"{name} {last_name}\t {total_points:.1f}")


# Solicitar al usuario el nombre del archivo del profesor Jekyll
file_name = input("Ingrese el nombre del archivo del profesor Jekyll: ")

# Procesar el archivo y mostrar el informe
process_student_data(file_name)
