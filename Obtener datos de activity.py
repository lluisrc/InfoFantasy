## README.MD este script recoge la información de "Activity" de todo el fantasy, de momento lo utilizo para obtener información del mas hijoputa haciendo clausulazos
## Para hacer funcionar este script debemos ejecutar e introducimos manualmente la contraseña del fantasy, después con colocamos en la pestaña de Activity. Finalmente clicamos enter en el terminal para continuar

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

operacionDelMercado = []
onceIdeal = []

# Instanciar el navegador web
driver = webdriver.Chrome()  # Asegúrate de tener el controlador de Chrome adecuado instalado y en tu PATH

# Abrir la página web
driver.get("https://fantasy.laliga.com/")

# Esperar a que el usuario introduzca manualmente el nombre de usuario y la contraseña
input("Una vez hayas entrado con usuario y contraseña al fantasy presiona Enter en este termianl para continuar...")

# Localizar el boton siguiente
botonSiguiente = driver.find_element(By.CSS_SELECTOR, "div.nextPage button.btn-fantasy")

# Localizar el boton anterior
botonAnterior = driver.find_element(By.CSS_SELECTOR, "div.previousPage button.btn-fantasy")

# Localizar el elemento con la clase "timeline"
timelineElemento = driver.find_element(By.CLASS_NAME, "timeline")

# Bucle infinito hasta que aparezca la imagen de Sin Resultados
while True:
    driver.implicitly_wait(1)  # Espera implícita de 1 segundos
    # Intenta encontrar la imagen de Sin Resultados si no la encuentra clica en el botón siguiente
    try:
        imagenSinResultados = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@src, 'empty_state_no_activity')]")))
        break
    except:
        # Obtener datos        
        soup = BeautifulSoup(timelineElemento.get_attribute('innerHTML'), 'html.parser')

        # Buscar todos los elementos con la clase "ltr timeline__card"
        cards = soup.find_all(class_="ltr timeline__card")

        for card in cards:
            title = card.find(class_="title").text.strip()
            body = card.find(class_="card__body").text.strip()

            # Aqui hago el filtrado
            if title == 'Operación de mercado':
                operacionDelMercado.append(body)
            
            if title == '11 ideal':
                onceIdeal.append(body)

        # Hacer clic en el elemento siguiente
        botonSiguiente.click()

        
print(operacionDelMercado)
print('')
print(onceIdeal)
input("Ver los resultados")


# Cuando hayas terminado, cierra el navegador
driver.quit()
