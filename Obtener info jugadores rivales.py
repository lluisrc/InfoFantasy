from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

jugadores = ["Ensaimada_City", "PRATS", "Tugoressss", "Sporting_de_Cananu", "Elpu7", "makinaone", "Payo_Cayetano", "Jorch579", "muletjr10", "Al_bert_Ibn_al_Ettif"]

# Instanciar el navegador web
driver = webdriver.Chrome()  # Asegúrate de tener el controlador de Chrome adecuado instalado y en tu PATH

# Abrir la página web
driver.get("https://fantasy.laliga.com/")

for jugador in jugadores:
        input(f"Dirigete a los jugadores del club {jugador}")
        
        player_name = ""
        player_value = ""
        player_average = ""
        player_clause = ""
        player_points = ""
        player_position = ""
        hist5 = ""
        hist4 = ""
        hist3 = ""
        hist2 = ""
        hist1 = ""
        team_image_url = ""

        # Obtiene el HTML de la página
        html = driver.page_source

        ## Para obtener este html necesitas inspecionar elemento en la tabla de todos los juagadores del mercado y copiar toda la etiqueta [<tbody _ngcontent-ng-c1901109146="">]
        soup = BeautifulSoup(html, 'html.parser')

        # Encuentra todas las etiquetas con la clase "player-item"
        newHtml = soup.find(class_='tab-pane fade show active')
        player_items = newHtml.find_all(class_='col-9 col-sm-9 info card-player-data')
        team_items = newHtml.find_all(class_='col-3 col-sm-3 picture-team-badge padding-sm')

        # Itera sobre las etiquetas encontradas
        for indice, player_item in enumerate(player_items):

            # Extraer el nombre del jugador
            player_name = player_item.select_one('.market-player-nickname').text.strip()

            # Extraer el valor del jugador
            player_value = player_item.select_one('.value').text.strip()

            # Extraer la media del jugador
            player_average = player_item.select_one('.average-points').text.strip()

            try:
                # Extraer la cláusula del jugador
                player_clause = player_item.select_one('.buyoutClause').text.strip()
            except:
                try:
                    # Encuentra el elemento que contiene el texto de los días
                    player_clause = player_item.find('span', string=lambda text: text and 'día' in text).text.strip()
                except:
                    player_clause = "Menos de 1 día"

            # Extraer los puntos del jugador
            player_points = player_item.select_one('.points-stat').text.strip().split('  ')[1]

            # Extraer la posición del jugador
            player_position = player_item.select_one('.position').text.strip()

            player_team = team_items[indice].find('span', class_='player-card-team-badge')['data-bg'].split('/')[6].split('_')[1].split('.png')[0]

            # Extraer el historial del jugador
            hist5 = [stat.text.strip() for stat in player_item.select('.stat label')][0]
            hist4 = [stat.text.strip() for stat in player_item.select('.stat label')][1]
            hist3 = [stat.text.strip() for stat in player_item.select('.stat label')][2]
            hist2 = [stat.text.strip() for stat in player_item.select('.stat label')][3]
            hist1 = [stat.text.strip() for stat in player_item.select('.stat label')][4]
            
            try:
                hist1 = int(hist1)
            except:
                hist1 = 0
            try:
                hist2 = int(hist2)
            except:
                hist2 = 0
            try:
                hist3 = int(hist3)
            except:
                hist3 = 0
            try:
                hist4 = int(hist4)
            except:
                hist4 = 0
            try:
                hist5 = int(hist5)
            except:
                hist5 = 0
            
            average5 = round((hist1 + hist2 + hist3 + hist4 + hist5) / 5, 1)
            average3 = round((hist1 + hist2 + hist3) / 3, 1)

            print(f"{jugador};{player_name};{player_value};{player_clause};{player_points};{player_average};{average5};{average3};{player_position};{player_team};{hist1};{hist2};{hist3};{hist4};{hist5}")
        