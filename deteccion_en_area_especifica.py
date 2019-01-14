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
import ubidots_parking as ubi	#script que se encarga de enviar y recibir datos de la nube, en este caso de ubidots
import threading				#para utilizar hilos --> threads

#Clasificador para automoviles
clasificador_autos = cv2.CascadeClassifier('Haarcascades/autos_cascade.xml')


	
############################...Funciones...#############################



#Funcion que debo llamar en el main.py para 
def func_deteccion_vehiculos():
	########################################################################
	cv2.namedWindow('Cuadro')

	#Iniciar video captura de un archivo de video para pruebas
	#captura = cv2.VideoCapture('http://87.243.137.233/axis-cgi/mjpg/video.cgi?camera=?resolution=640x480')
	
	
	captura = cv2.VideoCapture('http://138.26.107.148/mjpg/video.mjpg?timestamp=1546935659075')
	
	#captura = cv2.VideoCapture('images/parqueo.mp4')

	#Si el video abre correctamente se inicia el siguiente loop
	while captura.isOpened():

		time.sleep(3)            #time sleep para ver el video más lento o menos captura de tomas en tiempo real
		#ademas el delay funciona para no saturar el envio a la nube
		# Lee el primer cuadro:
		ret, cuadro = captura.read() #captura cuadro por cuadro
		
		#Filtros:
		cuadro = cv2.GaussianBlur(cuadro,(5,5),0)	#Elimina ruido Gaussiano
		
		#Rescalar la imagen:
		porcentaje = 60
		ancho =  int(cuadro.shape[1] * porcentaje/100)
		alto =  int(cuadro.shape[0] * porcentaje/100)
		dimensiones = (ancho, alto)
		cuadro = cv2.resize(cuadro, dimensiones, interpolation = cv2.INTER_AREA)
			
		#cuadro = cv2.Canny(cuadro, 100, 300)	#no funciona ...
			
		#if punto1 and punto2:
		#    cv2.rectangle(cuadro, punto1, punto2, (0, 255, 0),2)
		
		#Si hay captura entonces ret=True
		if ret:
			
			#gris = cv2.cvtColor(cuadro, cv2.COLOR_BGR2GRAY)
			
			
			#for c in range (0,11):
				
			# Pasa el cuadro por nuestro clasificador de autos
			#autos = clasificador_autos.detectMultiScale(gris, 1.1, 1)
			
			
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
					
					#Cargar la clase a variables:
					#Se deben de pasar los string a enteros para realizar comparaciones matematicas...
					ID = eval('esp.espacio_%s.id_espacio'% i)
					#estado = int(eval('esp.espacio_%s.estado'% i))
					
					x_1 = int(eval('esp.espacio_%s.x_1'% i))
					y_1 = int(eval('esp.espacio_%s.y_1'% i))
					x_2 = int(eval('esp.espacio_%s.x_2'% i))
					y_2 = int(eval('esp.espacio_%s.y_2'% i))
					x_c = int(eval('esp.espacio_%s.x_c'% i))
					y_c = int(eval('esp.espacio_%s.y_c'% i))
					#coordenadas seran con flotantes porque tienen decimales
					latitud = float(eval('esp.espacio_%s.latitud'% i))
					longitud = float(eval('esp.espacio_%s.longitud'% i))			
					
					
					recorte = cuadro[y_1:y_2 , x_1:x_2]		#recorta la imagen --> imagen[y:y+h, x:x+w]
					gris = cv2.cvtColor(recorte, cv2.COLOR_BGR2GRAY)
					
					#pinta un rectangulo verde en el area de deteccion, verde significa que esta desocupado
					cv2.rectangle(cuadro, (x_1, y_1), (x_2, y_2), (0, 255, 0), 2)	
					#Clasificador
					autos = clasificador_autos.detectMultiScale(gris, 1.03, 2)
					
					estado = False	#bandera de deteccion, declarada como True y si detecta se cambia a True
					#si detecta el objeto devuelve las coordenadas:
					for (x,y,w,h) in autos:
						x2 = x + w	#coordenada x
						y2 = y + h	#coordenada y
						#Dibuja un rectangulo donde detecta el vehiculo (amarillo)
						cv2.rectangle(cuadro, (x_1+x, y_1+y), (x_1+x+w, y_1+y+h), (0, 255, 255), 2)	
						#cambiar a un solo if, por ahora de prueba
						if x2>x_c>x:
							print "Si calza con x"
							if y2>x_c>y:
								print "Tambien con y"
								estado = True				#detecto un auto en el punto especificado!
								#pinta un rectangulo rojo en el area de deteccion, rojo significa que esta ocupado
								cv2.rectangle(cuadro, (x_1, y_1), (x_2, y_2), (0, 0, 255), 2)
					
					#para evitar que se creen muchos hilos y por lo tanto evitar que se envie un dato al mismo tiempo se coloca la siguiente condicion:
					if ubi.contador_hilos < esp.n_esp :
					
						#envia el estado del espacio de estacionamiento a ubidots:
						hilo_ubidots = threading.Thread (target = ubi.enviar_ubidots, name=hilo, args = (ID, estado, latitud, longitud,))
						hilo_ubidots.start()	#inicia el thread 
					
					else	#esta condicion nunca deberia de ejecutarse...
						print "Se evito que se crearan muchos hilos"
						print ubi.contador_hilos
			#luego de "dibujar" todos los rectangulos en un cuadro, muestra la imagen final:	
			cv2.imshow('cuadro', cuadro)
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


