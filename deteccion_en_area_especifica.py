# coding=utf-8
"""
Fecha:14 de diciembre del 2018

@author: Daniel Quesada Vindas

@ITCR_sede_San_Carlos

@Funcion: Detectar vehiculos en los espacios de estacionamiento previamente definidos
"""


#Headers a utilizar:
import cv2
import time
import numpy as np


#Clasificador para automoviles
clasificador_autos = cv2.CascadeClassifier('Haarcascades/cars.xml')


############################...Funciones...#############################



#Funcion que debo llamar en el main.py para 
def func_deteccion_vehiculos():
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

	print "Se cerro el video"	#sale del while


	captura.release()
	cv2.destroyAllWindows()
	return 0


