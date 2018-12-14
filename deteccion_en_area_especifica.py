# coding=utf-8
"""
Fecha:13 de diciembre del 2018

@author: Daniel Quesada Vindas

@ITCR_sede_San_Carlos
"""
#Headers a utilizar:
import cv2
import time
import numpy as np
import argparse         #para analizar linea de comandos

#Inicializa la lista de puntos de referencia y boleanos, indicando si el recorte se esta realizando o no...
refPuntero = []          #para guardas las dos coordenadas del click del mouse
click_recorte = False    #para indicar si el click izq del mouse esta presionado...

#Argumentos relacionados con la funcion click_y_recortar:
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", )


#Crear el clasificador para automoviles
clasificador_autos = cv2.CascadeClassifier('Haarcascades/cars.xml')

#Iniciar video captura de un archivo de video para pruebas
captura = cv2.VideoCapture('images/cars.avi')




#Si el video abre correctamente se inicia el siguiente loop
"""
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
            cv2.waitKey()

    if cv2.waitKey(1) == 13: #13 is the Enter Key
            break
"""
if captura.isOpened():
    ret, cuadro = captura.read() #captura cuadro por cuadro
    cv2.imshow('Autos', cuadro)
    cv2.waitKey()

#fuente de referencia:
#https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
def click_y_recortar(evento, x, y, banderas, parametros):
    
    global refPuntero, click_recorte       #variables globales
    
    
    #si el click izq del mouse se presiona, da la direccion del punto inicial (x,y)
    #e indica que el recorte va a empezar
    if evento == cv2.EVENT_LBUTTONDOWN:
        refPuntero = [(x, y)]
        click_recorte = True    #cambia el estado de recorte a Verdadero (inicia aqui...)
    
    #Revisa si el boton izq del mouse se dejo de presionar...
    elif evento == cv2.EVENT_LBUTTONUP:
        #Graba el final de las coordenadas (x,y) e indica que la operacion de recorte finalizo
        refPuntero.append((x,y))
        click_recorte = False   #cambia el estado de recorte a Falso... deja de recortar
        
        #dibujar rectangulo alrededor dela region de interes:
        cv2.rectangle(cuadro, refPuntero[0], refPuntero[1], (0, 255, 0), 2)
        
        

#Captura solo el primer cuadro y congela la imagen hasta que se presione un tecla





captura.release()
cv2.destroyAllWindows()
