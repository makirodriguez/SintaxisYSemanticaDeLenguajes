from tadProceso import*
from datetime import*
from tadCpu import*
from tadCola import*
import os

cpu=crearCPU()

def validacionFecha():
	while True:
		try:
			print('Ingrese la fecha (dd/mm/yyyy): ')
			dia=input('Dia: ')
			mes=input('Mes: ')
			anio=input('Anio: ')
			if ((int(anio)>1990)):
				fecha=date(int(anio), int(mes), int(dia))
				return fecha
			else:
				print('-'*44,'\nNo es una fecha valida, ingresela nuevamente\n','-'*43)
		except(ValueError):
			print('-'*44,'\nNo es una fecha valida, ingresela nuevamente\n','-'*43)
			return validacionFecha()

def validacionHora():
	while True:
		try:
			print('Ingrese la hora (hh:mm): ')
			h=input('Hora: ')
			m=input('Minutos: ')
			s=0
			hora=time(int(h), int(m), int(s))
			return hora
		except(ValueError):
			print('-'*44,'\nNo es una hora valida, ingresela nuevamente\n','-'*43)
			return validacionHora()

def validarNombre():
	nombre=input("Nombre: ")
	tam=cantidad(cpu)
	i=0
	while i<tam:
		proceso=recuperarProceso(cpu, i)
		if((verNom(proceso))==(nombre)):
			print('-'*52,'\nYa existe el nombre ingresado, intentelo nuevamente\n','-'*51)
			return validarNombre()
		else:
			i+=1
	return nombre

def ingresarProceso():
	resp=input('Quiere ingresar un proceso? s/n: ')
	while (resp=='s'):
		print('Ingrese datos del proceso: ')
		nom=validarNombre()
		tipo=input('Tipo: ')
		tam=input('Tamanio: ')
		prioridad=input('Prioridad: ')
		fecha=validacionFecha()
		hora=validacionHora()
		proceso=crearProceso()
		cargarProceso(proceso, nom, tipo, tam, prioridad, fecha, hora)
		agregarProceso(cpu, proceso)
		print('-'*29,'\nProceso cargado correctamente\n','-'*28)
		resp=input('Desea ingresar otro proceso? s/n: ')
		os.system('clear')			

def modificarPrioridad():
	tam=cantidad(cpu)
	i=0
	if (tam!=0):
		nomProc=input('Ingrese el nombre del proceso a modificar la prioridad: ')
		for k in range (tam):
			proceso=recuperarProceso(cpu, k)
			if(verNom(proceso)==nomProc):
				nuevaPrioridad=input('Ingrese la nueva prioridad del proceso: ')
				modifPrioridad(proceso, nuevaPrioridad)
				os.system('clear')
				print('-'*39,'\nLa prioridad fue cargada correctamente.\n', '-'*38)
				i+=1
		
		if(i==0):
			print('-'*43, '\nEl nombre', nomProc,  'no existe, intentelo nuevamente\n', '-'*42)
			resp=input('Desea seguir con la ejecucion?(s/n)\n--De lo contrario regresara al menu--: ')
			os.system('clear')
			if(resp=='s'):
				return modificarPrioridad()
	else:
		print('-'*25,'\nNo hay procesos cargados\n','-'*24)
	
def eliminarUnProceso():
	tam=cantidad(cpu)
	k=0
	i=0
	if(tam!=0):
		nomProcElim=input('Ingrese el nombre del proceso a eliminar: ')
		while k<(tam):
			proceso=recuperarProceso(cpu, k)
			if(verNom(proceso)==nomProcElim):
				eliminarProceso(cpu, proceso)
				tam=tam-1
				os.system('clear')
				print('-'*27,'\nProceso eliminado con exito\n', '-'*26)
				i+=1
			else:
				k+=1
		if(i==0):
			print('-'*44, '\nEl nombre ', nomProcElim,'no existe, intentelo nuevamente\n', '-'*43)
			resp=input('\nDesea seguir con la ejecucion?(s/n)\n--De lo contrario regresara al menu--: ')
			os.system('clear')
			if(resp=='s'):
				return eliminarUnProceso()
	else:
		print('-'*25,'\nNo hay procesos cargados\n','-'*24)			

def listarProcesos():
	tam=cantidad(cpu)
	print ("Listado de procesos de la CPU: \n")
	if (tam==0):
		print('-'*25,'\nNo hay procesos cargados\n','-'*24)
	for k in range (tam):
		proceso=recuperarProceso(cpu, k)
		print('-'*10,'Proceso numero:',k+1,'-'*10, '\nNombre:',verNom(proceso), '\nTipo:',verTipo(proceso),'\nTamanio:',verTam(proceso),'\nPrioridad:',
	    verPrioridad(proceso),'\nFecha:', verFecha(proceso),'\nHora:', verHora(proceso),'\n','-'*39)
	
def modificarProcesoABaja():
	i=0
	tam=cantidad(cpu)
	if(tam!=0):
		mes=input('Ingrese el mes para modificar los procesos a baja: ')
		if(int(mes)>12):
			print('El mes ingresado no es valido')
		prioridadBaja='Baja'	
		for k in range (tam):
			proceso=recuperarProceso(cpu, k)
			if(verFecha(proceso).month==int(mes)):
				modifPrioridad(proceso,prioridadBaja)
				os.system('clear')
				print('-'*36,'\nProceso modificado a baja con exito\n', '-'*35)
				i=+1
		if(i==0):
			print('-'*49,'\nNo hay procesos en el mes', mes, 'intentelo nuevamente\n', '-'*48)
			resp=input('Desea seguir con la ejecucion?(s/n)\n--De lo contrario regresara al menu--: ')
			os.system('clear')
			if(resp=='s'):
				return modificarProcesoABaja()
	else:
		print('-'*25,'\nNo hay procesos cargados\n','-'*24)		

def eliminarSegunTipo():
	tam=cantidad(cpu)
	k=0
	i=0
	if(tam!=0):
		tipoProc=input('Ingrese el tipo del proceso a eliminar: ')
		while k<(tam):
			proceso=recuperarProceso(cpu, k)
			if(verTipo(proceso)==tipoProc):
				eliminarProceso(cpu, proceso)
				tam=tam-1
				os.system('clear')
				print('-'*27,'\nProceso eliminado con exito\n', '-'*26)
				i+=1
			else:
				k+=1
		if(i==0):
			print('-'*43, '\nEl tipo ', tipoProc, 'no existe, intentelo nuevamente\n', '-'*42)
			resp=input('Desea seguir con la ejecucion?(s/n)\n--De lo contrario regresara al menu--: ')
			os.system('clear')
			if(resp=='s'):
				return eliminarSegunTipo()
	else:
		print('-'*25,'\nNo hay procesos cargados\n','-'*24)	

def colaDeProcesos():
	i=0
	j=0
	tam=cantidad(cpu)
	if(tam!=0):
		cola=crearCola()
		print('Primer hora:')
		h01=validacionHora()
		print('Segunda hora: ')
		h02=validacionHora()	
		for k in range(tam):
			proceso=recuperarProceso(cpu, k)
			if((verHora(proceso)<(h02))&(verHora(proceso)>(h01))):
				encolar(cola, proceso)
				print('-'*77, '\nLa cola de procesos entre las horas', h01, 'y',h02,'fue creada con exito\n', '-'*76 )
				i+=1
		while not esVacia(cola):
			j+=1
			print('Cola de procesos: \n')
			proceso=desencolar(cola)
			print('-'*10,'Proceso numero:',j,'-'*10, '\nNombre:',verNom(proceso), '\nTipo:',verTipo(proceso),'\nTamanio:',verTam(proceso),'\nPrioridad:',
				  verPrioridad(proceso),'\nFecha:', verFecha(proceso),'\nHora:', verHora(proceso),'\n','-'*39)

		if(i==0):
			os.system('clear')
			print('-'*77,'\nNo existen procesos entre las horas', h01, 'y', h02,'intentelo nuevamente\n', '-'*76)
			resp=input('Desea seguir con la ejecucion?(s/n)\n--De lo contrario volvera al menu--: ')
			os.system('clear')
			if(resp=='s'):
				return colaDeProcesos()
	else:
		print('-'*25,'\nNo hay procesos cargados\n','-'*24)

while True:

	# Mostramos el menu
	print ("Selecciona una opción")
	print ("\t1- Agregar proceso")
	print ("\t2- Modificar la prioridad del proceso")
	print ("\t3- Eliminar el proceso")
	print ("\t4- Listado de procesos")
	print ("\t5- Dado un determinado mes, modificar la prioridad de los procesos a baja")
	print ("\t6- Eliminar los procesos cuyo tipo sea igual al ingresado")
	print ("\t7- Generar una cola con aquellos procesos cuya ultima modificacion se encuentra entre dos horas dadas")
	print ("\t0- salir")

	# solicitamos una opción al usuario
	opcionMenu = input("Seleccione una opcion: ")
 	
	if opcionMenu=="1":
		ingresarProceso()

	elif opcionMenu=="2":
		modificarPrioridad()
		
	elif opcionMenu=="3":
		eliminarUnProceso()

	elif opcionMenu=="4":
		listarProcesos()

	elif opcionMenu=="5":
		modificarProcesoABaja()

	elif opcionMenu=="6":
		eliminarSegunTipo()

	elif opcionMenu=="7":
		colaDeProcesos()
		
	elif opcionMenu=="0":
		break
	else:
		print("")
		input("No has pulsado ninguna opción correcta, intentelo de nuevo")



	
		
	