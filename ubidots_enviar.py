# coding=utf-8
"""
Fecha:27 de diciembre del 2018

@author: Daniel Quesada Vindas

@ITCR_sede_San_Carlos

@Funcion:Ubidots--> Crear dispositivo en la nube con sus variables, para mostrarlas en un dashboard de ubidots.com

@Fuente: https://help.ubidots.com/connect-your-devices/connect-the-raspberry-pi-with-ubidots
"""

import time
import requests
import math
import random

TOKEN = "BBFF-bk5I3PyBtRVjWPNMmd5Yd9qN1fb9Ov"  # Put your TOKEN here
DEVICE_LABEL = "raspberry_parquimetro"  # Put your device label here 


def build_payload():
    variable_1 = "A"
    variable_2 = "B"
    variable_3 = "C"
    lat1 = 10.360505
    long1 = -84.442829
    lat2 = 10.360505
    long2 = -84.442782
    lat3 = 10.360510
    long3 = -84.442724
    
    payload = {variable_1: {"value": True, "context": {"lat": lat1, "lng": long1 }},
               variable_2: {"value": False, "context": {"lat": lat2, "lng": long2}},
               variable_3: {"value": True, "context": {"lat": lat3 , "lng": long3}}}

    return payload
	
def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://things.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    if status >= 400:
        print("[ERROR] No se pudo enviar datos luego de 5 intentos, por favor revisar \
            su token y su conexion a internet")
        return False

    print("[INFO] solicitud exitosa! , tu dispositivo actualizo datos!")
    return True



def main():
    payload = build_payload()

    print("[INFO] Intentando enviar datos...")
    post_request(payload)
    print("[INFO] Finalizado")


if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)
