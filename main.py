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
import cv2
import time
import numpy as np
import menu                      #importa el script menu.py que contiene el menu inicial y el de opciones...
import video_camara as vidcam    #script que muestra el video en tiempo real (para tomar datos de posicion)
import menu_espacios as esp      #script que guarda la cantidad de espacios de estacionamiento y los parametros de cada uno



                            


    
menu.func_menu_inicial()        #Llama al menu inicial
menu.func_menu_opciones()       #Menu con las opciones

while True:
    
    
    #luego de mostrar el menu con las opciones:
    entrada = raw_input("Digite una opcion valida: ")   #raw_input siempre devuelve un string
    
    
    #Opciones:
    if entrada == '1':                  #Opcion 1: mostrar el video en tiempo real
        vidcam.func_video_camara()      #llama a la funcion que muestra el video en tiempo real
        menu.func_menu_opciones()       #Menu con las opciones
    
    elif entrada == '2':                #Configuracion de parametros de los espacios de estacionamiento
        
        if esp.cant_espacios() ==1:
            print'\n\nSe definieron los parametros satisfactoriamente...'
            time.sleep(2)
            
        else:
            print'Ocurrio un error...'
        menu.func_menu_opciones()
        
    elif entrada == '3':
        print entrada
        time.sleep(2)
        menu.func_menu_opciones()
    
    elif entrada == 'cerrar':
        menu.cerrando_logo()
        break
    
    else:
        print 'ERROR: Entrada invalida!'
        time.sleep(1)
        
        
    
    
    
    
    
    
