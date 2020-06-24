
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from PyPDF2 import *
import requests
import time
import mysql.connector

# (1 Interfaz simple para datos

root = Tk()
root.title("Consultas Facturación")
root.resizable(0,0)

#Etiquetas de campos de datos
ingreso = Label(root, text= 'Ingrese sus datos', fg = 'white', background='purple', width=50)
ingreso.grid(row=0, column=0, sticky=N, columnspan=5)
ruta = Label(root, text='CUIT')
ruta.grid(row=1, column=0,sticky=W, padx=2, pady=1)
Clave = Label(root, text='Clave')
Clave.grid(row=2, column=0,sticky=W, padx=2, pady=1)
FecDes = Label(root, text='Desde')
FecDes.grid(row=3, column=0,sticky=W, padx=2, pady=1)
FecHas = Label(root, text='Hasta')
FecHas.grid(row=4, column=0,sticky=W, padx=2, pady=1)

#Optimización de entradas
def UniEntry(val,wid,fil,col):
    entrada = Entry(root,text = val, width = wid,)
    entrada.grid(row = fil, column = col)
    return entrada

val1, val2, val3 = StringVar(), StringVar(), StringVar()

# Creación de DB y tabla
"""
def crearDB():
    try:
        mibase = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '')
        micursor = mibase.cursor()
        micursor.execute('CREATE DATABASE FacturacionAFIP')
    except:
        print('La Base de Datos que intenta crear ya existe')
    try: 
        mibase = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '', database='FacturacionAFIP')
        micursor = mibase.cursor()
        micursor.execute('CREATE TABLE AFIP(factura int(20) NOT NULL PRIMARY KEY, fecha date COLLATE utf8_spanish2_ci NOT NULL, razon_social varchar(128) COLLATE utf8_spanish2_ci NOT NULL, importe float(11) COLLATE utf8_spanish2_ci NOT NULL, cae int(30) COLLATE utf8_spanish2_ci NOT NULL, vto_cae date COLLATE utf8_spanish2_ci NOT NULL')
    except:
        print('La tabla que intenta crear ya existe')

"""

# (1 Entrar a la pagina de Afip y scraping del input() ingreso #

driver.get('https://auth.afip.gob.ar/contribuyente_/login.xhtml')
login = driver.find_element(by_xpath, '//*[@id="F1:username"]').send_keys(20359013354)
submit = driver.find_element(by_xpath, '//*[@id="F1:btnSiguiente"]').click()

time.sleep(2) #Pausa para que recargue la pagina, tiempo arbitrario.

# (2 Clave e ingresar

password = driver.find_element(by.xpath, '//*[@id="F1:password"]').send_keys(PASSWORD)
ingreso = driver.find_element(by.xpath, '//*[@id="F1:btnIngresar"]').click()
time.sleep(3)

# (3 Seleccionar el aplicativo "Comprobantes en linea"
driver.get(window.open('https://portalcf.cloud.afip.gob.ar/portal/app/index-compat.html'))
comprobantes = driver.find_element(by.xpath, '//*[@id="servicesContainer"]/div[8]/div/div/div/div[2]/h4').click()

# (6 Moverse al popup y seleccionar el container "Empresa"

driver.get(window.open('https://serviciosjava2.afip.gob.ar/rcel/jsp/index_bis.jsp'))
empresa = driver.find_element(by.id, '//*[@id="contenido"]/form/table/tbody/tr[4]/td/input[2]').click()

# (7 Seleccionar "Consultas"

driver.get(window.open('https://serviciosjava2.afip.gob.ar/rcel/jsp/menu_ppal.jsp'))
consultas = driver.find_element(by.xpath, '/html/body/div[2]/table/tbody/tr[2]/td/a/span[2]').click()

# (8 Insert() de fechas en cada input()

FechaDesde = driver.find_element(by.ID, "fed").send_keys()

FechaHasta = driver.find_element(by.ID,"feh").send_keys()

# (9 Creacion de carpeta con el nombre del mes y el año



# (10 Seleccion del class_ Button "Ver" y descarga de comprobantes a su carpeta - for loop



# (11 class_ button "Volver" - Time sleep repetir pasos 8, 9, 10.



# (12 PyPDF2 para scrapping de resultados - output() en diccionarios


# (13 Carga de cada diccionario a la base MySQL