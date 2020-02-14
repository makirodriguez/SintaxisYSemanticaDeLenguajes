def crearCola():
	#Crea la cola vacia            
	cola=[]
	return cola

def encolar(cola,proceso):
	#Agrega un proceso al final de la cola  
	cola.append(proceso)

def desencolar(cola):
	#Elimina el primer proceso de la cola     
	elem=cola[0]
	del cola[0]
	return elem

def esVacia(cola):
	#Retorna true si la cola esta vacia y false en caso contrario
	if(cola==[]):
		return True
	else:
		return False

def duplicar(cola):
	#Copia los elementos de la cola2 en la cola1
	while not esVacia(cola2):
		proceso=desencolar(cola2)
		encolar(cola1, proceso)
		
