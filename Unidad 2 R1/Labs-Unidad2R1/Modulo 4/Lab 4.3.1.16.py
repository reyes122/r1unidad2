'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 16 de Noviembre 
 Description:
 Laboratorio: 4.3.1.16
'''

from collections import defaultdict

def generar_histograma(archivo):
    # Crear un diccionario para almacenar el recuento de cada letra
    recuento_letras = defaultdict(int)

    try:
        # Abrir el archivo y leer su contenido
        with open(archivo, 'r') as file:
            contenido = file.read()

        # Iterar sobre cada caracter del contenido
        for caracter in contenido:
            # Verificar si el caracter es una letra latina
            if caracter.isalpha():
                # Convertir el caracter a minúsculas para tratar las mayúsculas y minúsculas por igual
                letra = caracter.lower()

                # Incrementar el recuento de la letra
                recuento_letras[letra] += 1

        # Ordenar el diccionario por frecuencia usando una lambda
        ordenado = sorted(recuento_letras.items(), key=lambda x: x[1], reverse=True)

        # Imprimir el histograma ordenado en función de la frecuencia
        for letra, recuento in ordenado:
            print(f"{letra} -> {recuento}")

        # Guardar el histograma en un archivo con extensión '.hist'
        nombre_archivo_salida = archivo.split('.')[0] + '.hist'
        with open(nombre_archivo_salida, 'w') as output_file:
            for letra, recuento in ordenado:
                output_file.write(f"{letra} -> {recuento}\n")

        print(f"Histograma guardado en {nombre_archivo_salida}")

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print(f"Error: {e}")

# Crear un archivo de prueba
with open("samplefile.txt", 'w') as test_file:
    test_file.write("cBabAa")

# Nombre del archivo de prueba
nombre_archivo = "samplefile.txt"

# Generar y mostrar el histograma, y guardar en archivo
generar_histograma(nombre_archivo)
