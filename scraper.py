import requests
from bs4 import BeautifulSoup
import pandas as pd



url = "https://es.wikipedia.org/wiki/Base_de_datos"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("h2")

data= []

for title in titles:
    print(title.text)
    data.append(title.text)

df = pd.DataFrame(data, columns=["Subtitulos"])
df.to_excel("subtitulos_wikipedia.xlsx", index=False)

