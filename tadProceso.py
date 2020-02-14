def crearProceso():
	#Crea un proceso vacio
	proceso=['', '',0,'',0,0]
	return proceso

def cargarProceso(proceso, nom, tipo, tam, prioridad, fecha, hora):
	#Carga los datos del producto con su nombre, tipo, tamanio, prioridad y fecha y hora de su ultima modificacion
	proceso[0]=nom
	proceso[1]=tipo
	proceso[2]=tam
	proceso[3]=prioridad
	proceso[4]=fecha
	proceso[5]=hora

def verNom(proceso):
	#Muestra el nombre del proceso
	return proceso[0]

def verTipo(proceso):
	#Muestra el tipo del proceso
	return proceso[1]

def verTam(proceso):
	#Muestra el tamanio del proceso
	return proceso[2]

def verPrioridad(proceso):
	#Muestra la prioridad del proceso
	return proceso[3]

def verFecha(proceso):
	#Muestra la fecha del proceso
	return proceso[4]

def verHora(proceso):
	#Muestra la hora del proceso
	return proceso[5]

def modifNom(proceso, nuevoNom):
	#Modifica el nombre del proceso
	proceso[0]=nuevoNom

def modifTipo(proceso, nuevoTipo):
	#Modifica el tipo del proceso
	proceso[1]=nuevoTipo

def modifTam(proceso, nuevoTam):
	#Modifica el tamanio del proceso
	proceso[2]=nuevoTam

def modifPrioridad(proceso, nuevaPrioridad):
	#Modifica la prioridad del proceso
	proceso[3]=nuevaPrioridad

def modifFecha(proceso, nuevaFecha):
	#Modifica la fecha del proceso
	proceso[4]=nuevaFecha

def modifFecha(proceso, nuevaHora):
	#Modifica la hora del proceso
	proceso[5]=nuevaHora

def asignar(p1, p2):
	#Le asigna al proceso 2 los datos del proceso 1
	p1[0]=p2[0]
	p1[1]=p2[1]
	p1[2]=p2[2]
	p1[3]=p2[3]
	p1[4]=p2[4]
	p1[5]=p2[5]



