import requests
import pyperclip
from bs4 import BeautifulSoup

url = 'https://new.yapo.cl/biobio/marketplace/computadores-electronica'

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

cositas = soup.find_all('div', class_='d-flex img-inner justify-content-center align-items-center ng-star-inserted')

# imagenes = []

# for publicacion in publicaciones:
#     imagen = publicacion.find('img')['src']
#     imagenes.append(imagen)

# for imagen in imagenes:
#     print(imagen)

# print(len(cositas))
pyperclip.copy(soup.prettify())
pyperclip.copy("terrible gay el pive")
# print(soup.prettify())
