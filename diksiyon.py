import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://sinemaakademi.com.tr/diksiyon/diksiyon-tekerlemeleri"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

ul_element = soup.find("ul")

tekerleme = ul_element.find_all('li')

liste = list()
for i in range(len(tekerleme)):
    tekerleme[i] = (tekerleme[i].text).strip("\n").strip()
    liste.append([tekerleme[i]])
df = pd.DataFrame(liste,columns = ["Tekerlemeler"])
print(df)
