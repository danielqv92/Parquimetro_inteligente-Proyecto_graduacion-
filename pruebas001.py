# coding=utf-8
"""
Fecha:07 de octubre del 2018

@author: Daniel Quesada Vindas

@ITCR_sede_San_Carlos
"""
#Headers a utilizar:
import cv2
import time
import numpy as np

#Crear el clasificador para automoviles
clasificador_autos = cv2.CascadeClassifier('Haarcascades/haarcascade_car.xml')

#Iniciar video captura de un archivo de video para pruebas
captura = cv2.VideoCapture('/home/daniel/MEGAsync/Proyecto de graduación/git/images/cars.avi')

#Si el video abre correctamente se inicia el siguiente loop
while captura.isOpened():

    #time.sleep(.05)            #time sleep para ver el video más lento
    # Lee el primer cuadro:
    ret, cuadro = captura.read() #captura cuadro por cuadro
    if ret:
        gris = cv2.cvtColor(cuadro, cv2.COLOR_BGR2GRAY)

        # Pasa el cuadro por nuestro clasificador de autos
        autos = clasificador_autos.detectMultiScale(gris, 1.4, 2)

        # Dibujar un rectangulo donde se identifique un auto
        for (x,y,w,h) in autos:
            cv2.rectangle(cuadro, (x, y), (x+w, y+h), (0, 255, 255), 2)
            cv2.imshow('Autos', cuadro)

    if cv2.waitKey(1) == 13: #13 is the Enter Key
            break

captura.release()
cv2.destroyAllWindows()
