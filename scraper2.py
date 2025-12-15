import requests
from bs4 import BeautifulSoup
import pandas as pd

url ="https://es.wikipedia.org/wiki/Tabla_(informaci%C3%B3n)"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
}

response= requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
tabla = soup.find_all("table", class_="wikitable")
tabla_real = tabla[2]

data = []
for fila in tabla_real.find_all("tr"):
    columnas = fila.find_all("td")
    if len(columnas) == 4:
        nombre = columnas[0].text.strip()
        radio = columnas[1].text.strip()
        masa = columnas[2].text.strip()
        signo = columnas[3].text.strip()
        print([nombre,radio,masa,signo])
        data.append([nombre,radio,masa,signo])

df = pd.DataFrame(data, columns=[nombre,radio,masa,signo])
df.to_excel("Tabla_Espacial.xlsx", index=False)


