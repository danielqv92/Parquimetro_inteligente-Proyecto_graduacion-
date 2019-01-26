# coding=utf-8
"""
Fecha:18 de diciembre del 2018

@author: Daniel Quesada Vindas

@ITCR_sede_San_Carlos

@Logros:se imprime la coordenada del puntero del mouse sobre el video
@Notas: El video esta enciclado para poder trabajar con un demo
@Siguiente paso: detectar en espacio especifico
"""
#Headers a utilizar:
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')	#para evitar que python no encuentre el path de cv2... pasa muy seguido 
#si no funciona cambiar dist por site
import cv2
import time
import numpy as np
import menu                      #importa el script menu.py que contiene el menu inicial y el de opciones...
import video_camara as vidcam    #script que muestra el video en tiempo real (para tomar datos de posicion)
import menu_espacios as esp      #script que guarda la cantidad de espacios de estacionamiento y los parametros de cada uno
import dill					     #para guardar la sesion

#script que contiene el codigo necesario para detectar vehiculos dentro de los espacios definidos:
import deteccion_en_area_especifica as deteccion    


#Archivo para guardar datos de la sesion--> variables, etc...
archivo_main = 'tmp_main.pkl'
try:
	#espacio_estacionamiento = pickle.load(open("lista_espacios.dat","rb"))
	dill.load_session(archivo_main)				#carga el archivo con el nombre y extension
	print "Archivo de sesion cargado"
except:
	print "No hay archivo de sesion que cargar..."


    
menu.func_menu_inicial()        #Llama al menu inicial
menu.func_menu_opciones()       #Menu con las opciones

#MAIN:
while True:
    
    #luego de mostrar el menu con las opciones:
    entrada = raw_input("Digite una opcion valida: ")   #raw_input siempre devuelve un string 
    
    #Opciones:
    if entrada == '1':                  #Opcion 1: mostrar el video en tiempo real
        vidcam.func_video_camara()      #llama a la funcion que muestra el video en tiempo real
        menu.func_menu_opciones()       #Menu con las opciones
    
    elif entrada == '2':                #Configuracion de parametros de los espacios de estacionamiento
        k = esp.cant_espacios()
        if  k==1:
            print'\n\nSe definieron los parametros satisfactoriamente...'
            dill.dump_session(archivo_main)			#Guarda datos de sesion...			
            time.sleep(1) 
        elif k==3:	#si retorna 3 significa que se cancelo la opcion de insertar parametros de los espacios
			print "Cancelando..."
			time.sleep(1)
			
        else:
            print'Ocurrio un error...'
        
        enter_pr = raw_input("Presione la tecla enter para continuar")
        
        menu.func_menu_opciones()
        
    elif entrada == '3':	#Deteccion modo grafico
        deteccion.func_deteccion_vehiculos()    
        menu.func_menu_opciones()
    
    elif entrada == '4':	#definir parametros
	deteccion.parametros_insert()
	dill.dump_session(archivo_main)			#Guarda datos de sesion...
	time.sleep(0.33)
	menu.func_menu_opciones()
	    
    elif entrada == '5':	#Deteccion en modo consola
	deteccion.func_deteccion_vehiculos_consola()
	menu.func_menu_opciones()
		
    elif entrada == 'cerrar':
        menu.cerrando_logo()
        break
    
    else:
        print 'ERROR: Entrada invalida!'
	print "\n"
        time.sleep(1)
          
    
    
