from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


# Instanciar el navegador web
driver = webdriver.Chrome()  # Asegúrate de tener el controlador de Chrome adecuado instalado y en tu PATH

# Abrir la página web
driver.get("https://fantasy.laliga.com/")

# Esperar a que el usuario introduzca manualmente el nombre de usuario y la contraseña
input("Una vez hayas entrado con usuario y contraseña al fantasy presiona Enter en este termianl para continuar...")

# Obtiene el HTML de la página
html = driver.page_source

## Para obtener este html necesitas inspecionar elemento en la tabla de todos los juagadores del mercado y copiar toda la etiqueta [<tbody _ngcontent-ng-c1901109146="">]
soup = BeautifulSoup(html, 'html.parser')

# Encuentra todas las etiquetas con la clase "player-item"
player_items = soup.find_all(class_='player-item')

clases = ["fy-icon-ico_player_status_doubtful", "fy-icon-ico_player_status_ok", "fy-icon-ico_player_status_injured", "fy-icon-ico_player_status_sanctioned"]
# Itera sobre las etiquetas encontradas
for player_item in player_items:
        # Realiza las operaciones necesarias con cada etiqueta
        # Por ejemplo, puedes imprimir el contenido de la etiqueta

        # Encuentra la etiqueta <span> con la clase "name" dentro de la etiqueta <td> con la clase "player"
        name = player_item.find('td', class_='player').find('span', class_='name').text.strip()

        # Encuentra la etiqueta <span> con la clase "player-1 position" dentro de la etiqueta <td> con la clase "player"
        position = player_item.find('td', class_='player').find('span', class_='position').text.strip()

        # Encuentra la etiqueta <span> con la clase "owner" dentro de la etiqueta <div> con la clase "player-owner"
        owner = player_item.find('div', class_='player-owner').find('span', class_='owner').text.strip()

        # Encuentra la etiqueta <label> dentro de la etiqueta <td> con la clase "team" y obtén el texto dentro de esta etiqueta
        team = player_item.find('td', class_='team').find('label').text.strip()

        valor = player_item.find('td', class_='value').find('span', class_='value').text.strip().replace(".","")

        # Encuentra la etiqueta <td> con la clase "points" y obtén el texto dentro de esta etiqueta
        points = player_item.find('td', class_='points').text.strip().split(" ")[1]

        status = ""
        
        if player_item.find(class_="fy-icon-ico_player_status_doubtful"):
                status = "Dudoso"
        if player_item.find(class_="fy-icon-ico_player_status_ok"):
                status = "Alineable"
        if player_item.find(class_="fy-icon-ico_player_status_injured"):
                status = "Lesionado"
        if player_item.find(class_="fy-icon-ico_player_status_sanctioned"):
                status = "Sancionado"



        # Imprime la información obtenida
        print(f"{name};{position};{owner};{team};{points};{valor};{status}")


