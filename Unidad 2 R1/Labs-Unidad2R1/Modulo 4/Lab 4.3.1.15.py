'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 16 de Noviembre 
 Description:
 Laboratorio: 4.3.1.15
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

        # Imprimir el histograma en orden alfabético
        for letra in sorted(recuento_letras):
            print(f"{letra} -> {recuento_letras[letra]}")

        # Verificar si el histograma contiene resultados válidos
        if not any(recuento_letras.values()):
            print("El archivo no contiene letras latinas.")

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print(f"Error: {e}")

# Crear un archivo de prueba
with open("samplefile.txt", 'w') as test_file:
    test_file.write("aBc")

# Nombre del archivo de prueba
nombre_archivo = "samplefile.txt"

# Generar y mostrar el histograma
generar_histograma(nombre_archivo)
