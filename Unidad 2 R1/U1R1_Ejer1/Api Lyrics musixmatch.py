'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 17 de Noviembre 
 Description:
 Api musixmatch
'''
import requests

# URL base de la API de Musixmatch
base_url = "https://api.musixmatch.com/ws/1.1/"

# Clave de API
api_key = "&apikey=e0f3c5456182e12fa6ecd682bbbcac9d"

# Métodos de la API
a1 = lyrics_matcher = "matcher.lyrics.get"
metodos_api = [a1]

# Formato de URL
formato_url = "?format=json&callback=callback"

# Parámetros
p1 = artist_search_parameter = "&q_artist="
p2 = track_search_parameter = "&q_track="
parametros = [p1, p2]

# Listas con parámetros para cada método
x1 = lyrics_matcher_parameters = [p1, p2]
listas_parametros = [x1]

# Obtener los parámetros para el método correcto de la API
def obtener_parametros(opcion):
    if opcion == a1:
        return x1

while True:
    # Menú de opciones para el usuario
    print("1 - Escribe 1 para buscar la letra de una canción")
    print("0 - Escribe 0 para salir")
    print()
    opcion = input("> ")
    print()

    # Ejemplo
    if opcion == "1":
        print("¿Cuál es el nombre del artista?")
        nombre_artista = input("> ")
        print("¿Cuál es el nombre de la canción?")
        nombre_cancion = input("> ")
        print()

        # Realizar la llamada a la API
        call_api = base_url + lyrics_matcher + formato_url + artist_search_parameter + nombre_artista + track_search_parameter + nombre_cancion + api_key
        solicitud = requests.get(call_api)
        datos = solicitud.json()
        datos = datos['message']['body']
        
        # Mostrar la llamada a la API y la letra de la canción
        print("Llamada a la API: " + call_api)
        print()
        print(datos['lyrics']['lyrics_body'])

    # Verificar si el usuario desea continuar
    print()
    print("¿Desea otra letra? (s/n)")
    de_nuevo = input("> ")
    if de_nuevo.lower() == "n":
        break

