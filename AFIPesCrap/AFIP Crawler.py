from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from idlelib import window


# Entrar a la pagina de Afip y scraping del input() ingreso #

driver.get('https://auth.afip.gob.ar/contribuyente_/login.xhtml')
login = driver.find_element(By.ID, "F1:username").send_keys(20359013354)
submit = driver.find_element(By.ID, "F1:btnSiguiente").click()

#Pausa para que recargue la pagina, tiempo arbitrario.
time.sleep(2) 

# Clave e ingresar
password = driver.find_element(By.ID, "F1:password").send_keys()
ingreso = driver.find_element(By.ID, "F1:btnIngresar").click()
time.sleep(3)

# Seleccionar el aplicativo "Comprobantes en linea"
driver.get(window.open('https://portalcf.cloud.afip.gob.ar/portal/app/index-compat.html'))
comprobantes = driver.find_element(By.xpath, '//*[@id="servicesContainer"]/div[8]/div/div/div/div[2]/h4').click()

# Moverse al popup y seleccionar el container "Empresa"
driver.get(window.open('https://serviciosjava2.afip.gob.ar/rcel/jsp/index_bis.jsp'))
empresa = driver.find_element(By.id, 'contenido').click()

# Seleccionar "Consultas"
driver.get(window.open('https://serviciosjava2.afip.gob.ar/rcel/jsp/menu_ppal.jsp'))
consultas = driver.find_element(By.xpath, '/html/body/div[2]/table/tbody/tr[2]/td/a/span[2]').click()

# Insert() de fechas en cada input()
driver.get('https://serviciosjava2.afip.gob.ar/rcel/jsp/filtrarComprobantesGenerados.do')
FechaDesde = driver.find_element(By.ID, "fed").send_keys()
FechaHasta = driver.find_element(By.ID,"feh").send_keys()
buscar = driver.find_element(By.ID, "contenido").click()

# (9 Creacion de carpeta con el nombre del mes y el año



# (10 Seleccion del class_ Button "Ver" y descarga de comprobantes a su carpeta - for loop



# (11 class_ button "Volver" - Time sleep repetir pasos 8, 9, 10.



# (12 PyPDF2 para scrapping de resultados - output() en diccionarios


# (13 Carga de cada diccionario a la base MySQL