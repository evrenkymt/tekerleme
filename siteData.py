import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://sinemaakademi.com.tr/diksiyon/diksiyon-tekerlemeleri"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

tekerleme = soup.find_all("ul",{"class":""})

f = open("tekerlemeler.txt", "a")

liste = list()
for i in range(1):
    tekerleme[i] = (tekerleme[i].text).strip("::").strip()
    liste.append([tekerleme[i]])
    f.write(tekerleme[i])
f.close()