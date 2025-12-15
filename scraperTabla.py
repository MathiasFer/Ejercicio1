import requests
from bs4 import BeautifulSoup
import pandas as pd

url ="https://es.wikipedia.org/wiki/Tabla_(informaci%C3%B3n)"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

tabla = soup.find("table", class_="wikitable col3cen")

data =[]
for fila in tabla.find_all("tr"):
    columnas = fila.find_all("td")
    if len(columnas) == 3:
        nombre = columnas[0].text.strip()
        apellido = columnas[1].text.strip()
        edad = columnas[2].text.strip()
        data.append([nombre, apellido, edad])


df = pd.DataFrame(data, columns=["Nombre", "Apellido", "Edad"])
df.to_excel("tabla_wikipedia.xlsx", index=False)


