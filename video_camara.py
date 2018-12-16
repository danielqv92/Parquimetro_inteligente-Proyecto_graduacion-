# coding=utf-8
"""
Fecha:14 de diciembre del 2018

@author: Daniel Quesada Vindas

@ITCR_sede_San_Carlos

@Funcion: Mostrar video en tiempo real
"""


#Headers a utilizar:
import cv2
import time
import numpy as np



############################...Funciones...#############################

'''
Funcion que imprime en consola la posicion del puntero al mover el mouse
sobre el cuadro de la imagen
''' 
def coordenada_puntero(evento, x, y, banderas, parametros):
   
    if evento == cv2.EVENT_MOUSEMOVE: 
       print "X: {} || Y: {}".format(x,y)



#Funcion que debo llamar en el main.py para 
def func_video_camara():
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
		
		#Si hay captura entonces ret=True
		if ret:
						
			cv2.imshow('Cuadro', cuadro)
			#cv2.waitKey()
			
		#Si el video se termina    
		elif ret==False:    
			captura = cv2.VideoCapture('images/cars.avi')   #Descomentar para enciclar el video
			#break                                          #Descomentar y comentar linea anterior para quebrar el while cuando termina el video...
				

		#si se presiona la tecla de ord() entonces:
		if cv2.waitKey(33) == ord('q') or cv2.waitKey(33) == ord('Q'):	
			break
		
			

	print "Se cerro el video"	#sale del while


	captura.release()
	cv2.destroyAllWindows()
	return 0


