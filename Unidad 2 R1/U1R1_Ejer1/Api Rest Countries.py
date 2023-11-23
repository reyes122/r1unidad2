'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 17 de Noviembre 
 Description:
 Api Rest Countries
'''
import requests

# URL de la API que proporciona información sobre todos los países
url = "https://restcountries.com/v3.1/all"
print(url)

while True:
    # Realizar la solicitud GET a la API
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener datos en formato JSON directamente desde la respuesta
        data = response.json()

        # Solicitar al usuario el nombre del país
        country_name = input("Ingresa el nombre del país: ")

        # Buscar el país en los datos utilizando una expresión generadora y next()
        found_country = next((country for country in data if country_name.lower() in country['name']['common'].lower()), None)

        # Imprimir la capital si se encuentra algún país que coincida
        if found_country:
            print(f"La capital de {country_name} es: {found_country['capital'][0]}")
        else:
            print(f"No se encontró información para el país: {country_name}")

    else:
        # Imprimir un mensaje en caso de error en la solicitud
        print(f"Error al realizar la solicitud. Código de estado: {response.status_code}")

    # Preguntar al usuario si desea realizar otra consulta
    respuesta = input("¿Quieres realizar otra consulta? (sí/no): ")
    if respuesta.lower() != "sí":
        break


