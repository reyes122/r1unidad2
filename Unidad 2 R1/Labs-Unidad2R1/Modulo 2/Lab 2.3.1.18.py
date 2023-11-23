'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 14 de Noviembre
 Description:
 Laboratorio: 2.3.1.18
'''

def mysplit(strng):
    # Verifica si la cadena está vacía y devuelve una lista vacía en ese caso
    if not strng:
        return []
    
    # Inicializa una lista para almacenar las palabras
    words = []
    
    # Inicializa una variable para almacenar la palabra actual
    current_word = ""
    
    # Itera a través de cada caracter en la cadena
    for char in strng:
        # Si el caracter no es un espacio en blanco, agrega el caracter a la palabra actual
        if char != " ":
            current_word += char
        # Si el caracter es un espacio en blanco y la palabra actual no está vacía,
        # agrega la palabra actual a la lista de palabras y reinicia la palabra actual
        elif current_word:
            words.append(current_word)
            current_word = ""
    
    # Agrega la última palabra a la lista si la cadena no termina con un espacio en blanco
    if current_word:
        words.append(current_word)
    
    return words

# Pruebas
print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

