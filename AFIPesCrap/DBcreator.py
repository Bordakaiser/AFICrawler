import mysql.connector



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
