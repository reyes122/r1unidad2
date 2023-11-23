'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 17 de Noviembre 
 Description:
 Laboratorio: 4.4.1.8
'''

import os

def find(path, target_dir):
    # Obtiene la ruta absoluta del directorio inicial
    abs_path = os.path.abspath(path)

    # Función auxiliar para buscar el directorio de forma recursiva
    def search_directory(current_path):
        for root, dirs, _ in os.walk(current_path):
            # Verifica si el directorio objetivo está en la lista de subdirectorios
            if target_dir in dirs:
                # Imprime la ruta absoluta del directorio encontrado
                print(os.path.join(root, target_dir))

            # Llama recursivamente a la función para los subdirectorios
            for subdir in dirs:
                search_directory(os.path.join(root, subdir))

    # Llama a la función auxiliar para iniciar la búsqueda
    search_directory(abs_path)

# Solicitar al usuario la entrada de ejemplo
path = input("Ingrese la ruta del directorio de inicio: ")
target_directory = input("Ingrese el nombre del directorio a buscar: ")

# Llama a la función find con los parámetros proporcionados por el usuario
find(path, target_directory)
