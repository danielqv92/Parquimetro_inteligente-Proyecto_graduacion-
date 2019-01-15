# coding=utf-8
"""
Fecha:12 de Enero del 2019

@author: Daniel Quesada Vindas

@ITCR_sede_San_Carlos

@Funcion: Enviar y recibir datos de ubidots, crea un dispositivo por cada espacio de estacionamiento y envia una variable a ubidots junto con la latitud y longitud

@Fuente: ubidots.com
"""

import time
import requests
import math
import deteccion_en_area_especifica as det

TOKEN = "BBFF-bk5I3PyBtRVjWPNMmd5Yd9qN1fb9Ov"  # Put your TOKEN here

contador_hilos = 0	#usado para contar las veces que se esta ejecutando la funcion enviar_ubidots

"""
    13/01/19 02:00 horas
    Nota: se debe de colocar un contador que sume 1 al inicio de la funcion y reste 1 al final.
    De esta manera se lleva la cuenta de cuantos hilos de esta funcion estan corriendo...
    Debe de ser una variable donde se pueda llevar la cuenta en deteccion_en_area_especifica.py 
    porque es ahi donde se decidira si puede o no crear mas hilos.
    Esto es una medida meramente preventiva para evitar que se creen muchos hilos y que se trate de 
    enviar del mismo ID o dispositivo. En teoria si no se envian datos del dispositivo antes de que 
    se terminen de enviar los anteriores no debe de haber problemas debido a que serian atrasos de 
    maximo 1 o 2 segundos y en la practica un auto estacionado no se va mover tan rapido, aparecer
    o desaparecer como para que eso sea un problema...
""" 
def enviar_ubidots(ID, estado, latitud, longitud):
    global contador_hilos
    print "\nID: {} || Estado: {}".format(ID, estado)
    contador_hilos += 1
    DEVICE_LABEL = ID	#ID del dispositivo, uno por cada espacio de estacionamiento
    variable1 = "estado"
    variable2 = "position"
    #TEST estado:
    #estado = 1  #COMENTAR ESTA LINEA>>>>>>><<<<<<<<<<<<<COMENTAR ESTA LINEA
    #se envia dos veces el estado para utilizar uno como indicador y otro como punto del mapa!
    payload = {variable1: estado, variable2: {"value": estado, "context": {"lat": latitud, "lng": longitud }}}	#payload a enviar
	
    # Creates the headers for the HTTP requests
    url = "http://things.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 2:	#2 intentos, uno cada medio segundo...
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(0.5)

    # Processes results
    if status >= 400:
        print("[ERROR] No se pudo enviar datos luego de varios intentos, por favor revisar \
            su token y su conexion a internet")
        return False	
		
    print("[INFO] solicitud exitosa! , tu dispositivo actualizo datos!")
	
    contador_hilos -= 1
    return True			
