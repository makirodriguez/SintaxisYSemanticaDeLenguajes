def crearCPU():
	#Crea una CPU vacia
	cpu=[]
	return cpu

def agregarProceso(cpu, proceso):
	#Agrega un proceso en la CPU
	cpu.append(proceso)	

def eliminarProceso(cpu, proceso):
	#ELimina un proceso de la CPU
	cpu.remove(proceso)

def cantidad(cpu):
	#Retorna la cantidad de elementos de la cola
	return len(cpu)

def recuperarProceso(cpu, i):
	elemento=cpu[i]
	return elemento

def existe(cpu, proceso):
	return proceso in cpu
