'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 14 de Noviembre
 Description:
 Laboratorio: 2.8.1.4
'''
def read_int(prompt, min, max):
    while True:
        try:
            # Solicitar al usuario ingresar un valor
            user_input = input(prompt)
            
            # Intentar convertir la entrada a un entero
            value = int(user_input)

            # Verificar si el valor está dentro del rango especificado
            if min <= value <= max:
                # Si es válido, regresar el valor
                return value
            else:
                # Si está fuera del rango, imprimir un mensaje de error
                print(f"Error: el valor no está dentro del rango permitido ({min}..{max})")
        except ValueError:
            # Si la conversión a entero falla, imprimir un mensaje de error
            print("Error: entrada incorrecta")


# Prueba de la función
v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)
print("El número es:", v)
