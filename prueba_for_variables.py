
class espacio_estacionamiento:
	def __init__(self, id_espacio, estado, x_1, y_1, x_2, y_2):
			self.id_espacio = id_espacio
			self.estado = estado
			self.x_1 = x_1
			self.y_1 = y_1
			self.x_2 = x_2
			self.y_2 = y_2
			


def cant_espacios():
	global n_esp
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
	
	
cant_espacios()

x = 101
y = 101
w = 5
h = 5


for i in range(1,n_esp+1):
	
	x = int(x)
	y = int(y)
	x_1 = int(eval('espacio_%s.x_1'% i))
	y_1 = int(eval('espacio_%s.y_1'% i))
	x_2 = int(eval('espacio_%s.x_2'% i))
	y_2 = int(eval('espacio_%s.y_2'% i))
	x2 = x + w
	y2 = y + h
	'''
	print 'x: {}'.format(x)
	print 'y: {}'.format(y)
	print 'x2: {}'.format(x2)
	print 'y2: {}'.format(y2)
	print '\n'
	print 'x_1: {}'.format(x_1)
	print 'y_1: {}'.format(y_1)
	print 'x_2: {}'.format(x_2)
	print 'y_2: {}'.format(y_2)
	print '\n'
	'''
	
	#Caso unico si se busca que el auto este totalmente dentro del espacio de estacionamiento
	#if x>x_1 and y>y_1 and x2<x_2 and y2<y_2:
	#	print 'Carro'
	
	'''
	Cuatro casos posibles para cuando se detecte al menos parcialmente un auto dentro
	del espacio de estacionamiento:
	'''
	if x_2>x2>x_1:
		if y_2>y2>y_1:
			print 'Carro caso 1'
		elif y_2>y>y_1:
			print 'Carro caso 2'
		else:
			print 'No carro caso 1 y 2'
	elif x_2>x>x_1: 
		if y_2>y2>y_1:
			print 'Carro caso 3'
		elif y_2>y>y_1:
			print 'Carro caso 4'
		else:
			print 'No carro caso 3 y 4'
	else:
		print 'NO carro Ningun caso!'
			
	'''
	if x > x_1:
		print 'A'
	if y > y_1:
		print 'B'
	if x2 < x_2:
		print 'C'
	if y2 < y_2:
		print 'D'
	'''
	
	
	#print eval('espacio_%s.id_espacio'% i)  #eval('string') interpreta un string como codigo
	#print eval('espacio_%s.estado'% i)
	#print eval('espacio_%s.x_1'% i)
	#print eval('espacio_%s.y_1'% i)
	#print eval('espacio_%s.x_2'% i)
	#print eval('espacio_%s.y_2'% i)
	
	
	
	
