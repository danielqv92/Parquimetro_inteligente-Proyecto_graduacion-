#prueba listas
# coding=utf-8
"""
Fecha:18 de diciembre del 2018

@author: Daniel Quesada Vindas

@ITCR_sede_San_Carlos

@Funcion:Menu para los espacios de estacionamiento, aqui hay una clase para guardar los parametros de cada espacio 
"""
class espacio_estacionamiento:
	
	def __init__(self, id_espacio, estado, x_1, y_1, x_2, y_2):
		self.id_espacio = id_espacio
		self.estado = estado
		self.x_1 = x_1
		self.y_1 = y_1
		self.x_2 = x_2
		self.y_2 = y_2


#Menu para los espacios de estacionamiento:


def cant_espacios():
	n_esp = input("Digite la cantidad de espacios de estacionamiento a configurar: ")

	#Aca se debe de introducir los parametros de cada espacio de 1 hasta n_esp:

	for i in range(1,n_esp+1):	#de 1 a n_esp+1 para que cuente el ultimo entero
		
		'''se declaran variables de 1 hasta la cantidad de espacios disponibles para guardar 
		los parametros a definir por el usuario'''
		m =  raw_input("\nDigite id del espacio {}: ".format(i) )
		globals()['id_%s'% i] = m					
		
		m =  raw_input("Digite estado del espacio {}: ".format(i) )
		globals()['est_%s'% i] = m
		
		m =  raw_input("Digite x_1 del espacio {}: ".format(i) )
		globals()['x1_%s'% i] = m
		
		m =  raw_input("Digite y_1 del espacio {}: ".format(i) )
		globals()['y1_%s'% i] = m
		
		m =  raw_input("Digite x_2 del espacio {}: ".format(i) )
		globals()['x2_%s'% i] = m
		
		m =  raw_input("Digite y_2 del espacio {}: ".format(i) )
		globals()['y2_%s'% i] = m

	for i in range(1,n_esp+1):
		#print "id_{}".format(i), ":"
		#print globals()['id_%s'% i]
		
		#Crea los espacios utilizando clases
		globals()['espacio_%s'% i] = espacio_estacionamiento(globals()['id_%s'% i], globals()['est_%s'% i], globals()['x1_%s'% i], globals()['y1_%s'% i], globals()['x2_%s'% i], globals()['y2_%s'% i])
		return 1	#regresa 1 si se completa el proceso
	
#print id_1
#print id_2

#espacio_1 = espacio_estacionamiento(101, True, 228, 114, 264, 155)




#print espacio_1.id_espacio
#print espacio_1.estado
#print espacio_1.x_1
#print espacio_1.y_1
#print espacio_1.x_2
#print espacio_1.y_2
