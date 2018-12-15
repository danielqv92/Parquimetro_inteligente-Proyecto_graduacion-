# coding=utf-8
"""
Fecha:14 de diciembre del 2018

@author: Daniel Quesada Vindas

@ITCR_sede_San_Carlos

@Logros:se imprime la coordenada del puntero del mouse sobre el video
@Notas: El video esta enciclado para poder trabajar con un demo
@Siguiente paso: detectar en espacio especifico
"""
#Headers a utilizar:
import cv2
import time
import numpy as np

#Crear el clasificador para automoviles
clasificador_autos = cv2.CascadeClassifier('Haarcascades/cars.xml')

#Variables globales para la funcion dibujar_rect_mouse/// borrar esto...
dibujando = False
punto1 = ()
punto2 = ()


############################...Funciones...#############################

'''
Funcion que imprime en consola la posicion del puntero al mover el mouse
sobre el cuadro de la imagen
''' 
def coordenada_puntero(evento, x, y, banderas, parametros):
    global punto1, punto2, dibujando
   
    if evento == cv2.EVENT_MOUSEMOVE: 
       print "X: {} || Y: {}".format(x,y)

########################################################################
cv2.namedWindow('Cuadro')
cv2.setMouseCallback('Cuadro', coordenada_puntero)

#Iniciar video captura de un archivo de video para pruebas
captura = cv2.VideoCapture('images/cars.avi')

#Si el video abre correctamente se inicia el siguiente loop

while captura.isOpened():

    #time.sleep(.05)            #time sleep para ver el video más lento
    # Lee el primer cuadro:
    ret, cuadro = captura.read() #captura cuadro por cuadro
    
    
    """if ret:
        gris = cv2.cvtColor(cuadro, cv2.COLOR_BGR2GRAY)

        # Pasa el cuadro por nuestro clasificador de autos
        autos = clasificador_autos.detectMultiScale(gris, 1.4, 2)

        # Dibujar un rectangulo donde se identifique un auto
        for (x,y,w,h) in autos:
            cv2.rectangle(cuadro, (x, y), (x+w, y+h), (0, 255, 255), 2)
            
            cv2.imshow('Autos', cuadro)
            cv2.waitKey()
    """
    #if punto1 and punto2:
    #    cv2.rectangle(cuadro, punto1, punto2, (0, 255, 0),2)
    
    #Si hay captura entonces ret=True
    if ret:
        
        gris = cv2.cvtColor(cuadro, cv2.COLOR_BGR2GRAY)

        # Pasa el cuadro por nuestro clasificador de autos
        autos = clasificador_autos.detectMultiScale(gris, 1.4, 2)
        
        x_1 = 228
        y_1 = 114
        x_2 = 264
        y_2 = 155
        
        cv2.rectangle(cuadro, (x_1, y_1), (x_2, y_2), (0, 0, 255), 2)
        
        
        

        # Dibujar un rectangulo donde se identifique un auto
        for (x,y,w,h) in autos:
            cv2.rectangle(cuadro, (x, y), (x+w, y+h), (0, 255, 255), 2)
            
        cv2.imshow('Cuadro', cuadro)
        #cv2.waitKey()
        
    #Si el video se termina    
    elif ret==False:    
        captura = cv2.VideoCapture('images/cars.avi')   #Descomentar para enciclar el video
        #break                                          #Descomentar y comentar linea anterior para quebrar el while cuando termina el video...
            

    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

print "Se cerro el video"




    


captura.release()
cv2.destroyAllWindows()
