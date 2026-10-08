#Exercice1
import requests
response = requests.get("https://api.open-meteo.com/v1/forecast", params= params, headers = headers, timeout = 10)
params = {
    "latitude": 45.46, "longitude": 73.47,
    "current": "temperature_2m"
}
headers = {
    "Accept": "application/json"
}
print(response.url)
print(response.status_code)
response.raise_for_status()
data = response.json
temperature = data["current"]["temperature_2m"]
unite = data["current_units"]["temperature_2m"]
print(f"{temperature} {unite}")


#Exercice2
def temperature_actuelle(latitude, longitude):
    import requests
    params = {
        "latitude": 45.46, "longitude": 73.47,
        "current": "temperature_2m"
    }
    headers = {
        "Accept": "application/json"
    }
    try:
        response = requests.get("https://api.open-meteo.com/v1/forecast", params= params, headers = headers, timeout = 10)
        print(response.url)
        print(response.status_code)
        response.raise_for_status()
    except requests.Exceptions.HTTPError:
        print("Erreur HTTP")
    except requests.Exceptions.connetError:
        print("Erreur reseau")
    except requests.Exceptions.Timeout:
        print("Le delai d'attente est depasser")
    try:    
        data = response.json
    except requests.jsonError:
        print("La reponse recu n'est pas un Json valide")
    temperature = data["current"]["temperature_2m"]
    unite = data["current_units"]["temperature_2m"]
    print(f"{temperature} {unite}")
return temperature
if isinstance(data, dict) and "current" in data:
    current = data["current"]
    if isinstance(current, dict) and "temperature_2m" in current:
        temp = current["temperature_2m"]
        print(f"temperature : {temp} C")
    else:
        print("Donnees indisponibles : temperature_2m manquant")
else:
        print("Donnees indisponibles : current manquant")

try:
    response = request.get(url)
    response.raise_for_status()
    data = response.json()
    if "'current" in data and "temperature_2m" in data["current"]:
        print(f"temperature : {data["current"]["temperature_2m"]} C")
    else:
        print("Echec : donnes incompletes")
except Exception as e:
    print(f"Echec de recuperation: {e}")


#Exercice3
while True:
    try:
        lat = intput("latitude (90 a 90) : ")
        latitude = float(lat)
        if -90 <= latitude <= 90:
          break
        else: 
            print("doit etre un nombre entre -90 et 90.")
    except valueError:
        print("entrer un nombre pas un texte")

while True:
    try:
        lon = intput("logitude(-180 a 180) : ")
        longitude = float(lon)
        if-180 <= longitude <= 180:
          break
        else:
            print("doit etre entre -180 et 180.")
    except valueError:
        print("entrer un nombre pas un texte")

temp = get_meteo(lat, lon)
if temp is not None:
    print(f"{temp} C")
else:
    print("Donnés indisponibles.")

new = intput("Nouvelle recherche? (0/n):")
if new.lower() != "0":
    break
