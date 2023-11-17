'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 16 de Noviembre 
 Description:
 Api Noticias
'''

import requests

base_url = "https://newsapi.org/v2/everything?"
api_key = "90012c082ffb4a82848b1d7448c54fd5"

while True:
    keyword = input("Introduce una palabra clave (por ejemplo, Apple): ")
    
    while True:
        from_date = input("Introduce la fecha de inicio (en el formato YYYY-MM-DD): ")
        if len(from_date) == 10 and from_date.count('-') == 2:
            break
        else:
            print("Fecha no válida. Introduce la fecha en el formato correcto.")

    url = f"{base_url}q={keyword}&from={from_date}&sortBy=popularity&apiKey={api_key}"

    print("URL: " + url)
    print("=========================================")

    response = requests.get(url).json()

    if response["status"] == "ok":
        print("Total de resultados:", response["totalResults"])

        for idx, article in enumerate(response.get("articles", [])[:10]):
            print(f"\nTítulo {idx + 1}: {article['title']}")
            print(f"Autor: {article['author']}")
    else:
        print("Ha ocurrido un error:", response.get("message", "No se proporcionó un mensaje de error"))

    respuesta = input("¿Quieres continuar? (si/no): ")
    if respuesta.lower() != "si":
        break
