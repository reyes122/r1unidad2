'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 16 de Noviembre 
 Description:
 Api Noticias
'''
import requests

# URL base de la API de noticias y clave de API
main_api = "https://newsapi.org/v2/everything?"
key = "90012c082ffb4a82848b1d7448c54fd5"

while True:
    # Solicitar parámetros al usuario
    keyword = input("Introduce una palabra clave (por ejemplo, Apple): ")
    from_date = input("Introduce la fecha de inicio (en el formato YYYY-MM-DD): ")

    # Construir la URL con los parámetros proporcionados
    url = f"{main_api}q={keyword}&from={from_date}&sortBy=popularity&apiKey={key}"

    # Imprimir la URL construida para referencia
    print("URL: " + url)
    print("=========================================")

    # Realizar la solicitud a la API y obtener la respuesta en formato JSON
    json_data = requests.get(url).json()

    # Verificar si la solicitud fue exitosa (status "ok")
    if json_data["status"] == "ok":
        # Imprimir el total de resultados encontrados por la búsqueda
        print("Total de resultados:", json_data["totalResults"])

        # Mostrar títulos de noticias y autores de los primeros 10 resultados
        articles = json_data.get("articles", [])
        for idx, article in enumerate(articles[:10]):  # Mostrar los primeros 10 títulos y sus autores
            print(f"\nTítulo {idx + 1}: {article['title']}")
            print(f"Autor : {article['author']}")
    else:
        # Manejar casos donde la solicitud no fue exitosa
        print("Ha ocurrido un error")

    # Preguntar al usuario si quiere continuar o salir del programa
    respuesta = input("¿Quieres continuar? (si/no): ")
    if respuesta.lower() != "si":
        break  # Salir del bucle si la respuesta no es "si"
