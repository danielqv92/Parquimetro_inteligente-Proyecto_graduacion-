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
import menu_espacios as esp     #script que guarda la cantidad de espacios de estacionamiento y los parametros de cada uno

#Clasificador para automoviles
clasificador_autos = cv2.CascadeClassifier('Haarcascades/cars.xml')


############################...Funciones...#############################



#Funcion que debo llamar en el main.py para 
def func_deteccion_vehiculos():
	########################################################################
	cv2.namedWindow('Cuadro')

	#Iniciar video captura de un archivo de video para pruebas
	#captura = cv2.VideoCapture('http://79.9.140.50:82/mjpg/video.mjpg')
	
	captura = cv2.VideoCapture('http://138.26.107.148/mjpg/video.mjpg?timestamp=1546935659075')
	
	#captura = cv2.VideoCapture('images/parqueo.mp4')

	#Si el video abre correctamente se inicia el siguiente loop
	while captura.isOpened():

		time.sleep(.5)            #time sleep para ver el video más lento
		# Lee el primer cuadro:
		ret, cuadro = captura.read() #captura cuadro por cuadro
		
		#Filtros:
		cuadro = cv2.GaussianBlur(cuadro,(5,5),0)
		
		#Rescalar la imagen:
		porcentaje = 60
		ancho =  int(cuadro.shape[1] * porcentaje/100)
		alto =  int(cuadro.shape[0] * porcentaje/100)
		dimensiones = (ancho, alto)
		cuadro = cv2.resize(cuadro, dimensiones, interpolation = cv2.INTER_AREA)
			
		#if punto1 and punto2:
		#    cv2.rectangle(cuadro, punto1, punto2, (0, 255, 0),2)
		
		#Si hay captura entonces ret=True
		if ret:
			
			gris = cv2.cvtColor(cuadro, cv2.COLOR_BGR2GRAY)
			
			
			#for c in range (0,11):
				
			# Pasa el cuadro por nuestro clasificador de autos
			autos = clasificador_autos.detectMultiScale(gris, 1.1, 1)
			
			
			'''
			 Si identifica autos devolvera las coordenadas (x,y), ademas de el ancho y el alto del area de deteccion.
			 Primero se dibujara un rectangulo alrededor de dichas coordenadas y luego se comparara si parte de este 
			se encuentra dentro del area de algun espacio de estacionamiento definido en la opcion 2 del sistema, de
			ser asi se dibujara un rectangulo de color rojo y se cambiara el estado del espacio a True (espacio ocupado).
			 Para los espacios donde no se detecte un auto la condicion sera False y se dibujara un rectangulo de color verde
			'''
			try:
				esp.n_esp = esp.n_esp
			except:
				print"Error: Debe de configurar primero los espacios de estacionamiento"
				time.sleep(3)
				return 2	#retorna un 2 en caso de que n_esp que es la cantidad de espacios no se haya definido y termina la funcion
			
			#dibuja cuadros donde se configuraron los espacios de estacionamiento
			for i in range(1,esp.n_esp+1):
					#Se deben de pasar los string a enteros para realizar comparaciones matematicas...
					x_1 = int(eval('esp.espacio_%s.x_1'% i))
					y_1 = int(eval('esp.espacio_%s.y_1'% i))
					x_2 = int(eval('esp.espacio_%s.x_2'% i))
					y_2 = int(eval('esp.espacio_%s.y_2'% i))
					cv2.rectangle(cuadro, (x_1, y_1), (x_2, y_2), (255, 0, 0), 2)	
			
				
			for (x,y,w,h) in autos:
				cv2.rectangle(cuadro, (x, y), (x+w, y+h), (0, 255, 255), 2)		#dibuja un rectangulo donde detecta vehiculo
				
				for i in range(1,esp.n_esp+1):
					#Se deben de pasar los string a enteros para realizar comparaciones matematicas...
					x = int(x)
					y = int(y)
					x_1 = int(eval('esp.espacio_%s.x_1'% i))
					y_1 = int(eval('esp.espacio_%s.y_1'% i))
					x_2 = int(eval('esp.espacio_%s.x_2'% i))
					y_2 = int(eval('esp.espacio_%s.y_2'% i))
					x2 = x + w
					y2 = y + h
					#cv2.rectangle(cuadro, (x_1, y_1), (x_2, y_2), (255, 0, 0), 2)	
					#Caso unico si se busca que el auto este totalmente dentro del espacio de estacionamiento
					#if x>x_1 and y>y_1 and x2<x_2 and y2<y_2:
					#	print 'Carro'
					
					'''
					Cuatro casos posibles para cuando se detecte al menos parcialmente un auto dentro
					del espacio de estacionamiento:
					'''
					#Caso 1 y 2:			
					if x_2>x2>x_1:
						if y_2>y2>y_1:
							print 'Carro caso 1'
						elif y_2>y>y_1:
							print 'Carro caso 2'
						else:
							print 'No carro caso 1 y 2'
					
					#Caso 3 y 4:
					elif x_2>x>x_1: 
						if y_2>y2>y_1:
							print 'Carro caso 3'
						elif y_2>y>y_1:
							print 'Carro caso 4'
						else:
							print 'No carro caso 3 y 4'
							
					#Ningun caso anterior:
					else:
						print 'NO carro Ningun caso!'
			

				
			
			#luego de dibujar todos los rectangulos en un cuadro, muestra la imagen final:	
			cv2.imshow('Cuadro', cuadro)
			#cv2.waitKey()
			
		#Si el video se termina    
		elif ret==False:    
			#captura = cv2.VideoCapture('images/cars.avi')   #Descomentar para enciclar el video
			print("ERROR: se detuvo la conexion con la camara")
			time.sleep(5)
			break                                          #Descomentar y comentar linea anterior para quebrar el while cuando termina el video...
				

		#si se presiona la tecla de ord('tecla') entonces:
		if cv2.waitKey(33) == ord('q') or cv2.waitKey(33) == ord('Q'):	
			break

	print "Se cerro el video"	#sale del while


	captura.release()
	cv2.destroyAllWindows()
	return 0


