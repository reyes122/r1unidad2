'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 14 de Noviembre
 Description:
 Laboratorio: 2.4.1.6
'''
def mostrar_display(numero):
    # Definir los patrones de los dígitos con un diseño alternativo
    digitos = [
        ["###", "# #", "# #", "# #", "###"],  # 0
        ["  #", " # ", " # ", " # ", "###"],  # 1
        ["###", "  #", "###", "#  ", "###"],  # 2
        ["###", "  #", "###", "  #", "###"],  # 3
        ["# #", "# #", "###", "  #", "  #"],  # 4
        ["###", "#  ", "###", "  #", "###"],  # 5
        ["###", "#  ", "###", "# #", "###"],  # 6
        ["###", "  #", "  #", "  #", "  #"],  # 7
        ["###", "# #", "###", "# #", "###"],  # 8
        ["###", "# #", "###", "  #", "###"]   # 9
    ]

    # Convertir el número ingresado a una cadena
    numero_str = str(numero)

    # Iterar sobre cada fila del patrón de cada dígito
    for i in range(5):
        # Inicializar la cadena de la fila actual
        fila = ""

        # Iterar sobre cada dígito en el número ingresado
        for digito in numero_str:
            # Obtener el índice del dígito en la lista de dígitos
            indice = int(digito)

            # Agregar el patrón del dígito a la fila actual
            fila += digitos[indice][i] + "   "

        # Imprimir la fila actual
        print(fila)

# Solicitar al usuario ingresar un número
numero_usuario = int(input("Ingrese un número no negativo: "))

# Mostrar el display de siete segmentos para el número ingresado
mostrar_display(numero_usuario)
