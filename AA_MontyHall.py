import random
import numpy as np


#Se crea una lista de puertas, cuyo contenido son dos cabras y un carro en orden aleatorio.
def sort_doors():

	list = ['goat','goat','car']

	random.shuffle(list)

	return list


#Funcion que escoje un numero aleatorio, que determina la posicion seleccionada.
def choose_door():

	aleat = [0,1,2]

	return np.random.choice(aleat)



#Funcion que revela la primera cabra del juego.
def reveal_door(lista, choice):

	for i in range (len(lista)):
		if ((choice != i)&(lista[i]=='goat')):
			lista[i]='GOAT_MONTY'
			return lista


#Funcion que determina si el jugador cambia o no de puerta.
def finish_game(lista,choice,change):

		if (change == False):
			return lista[choice]
		
		else:

			for i in range(len(lista)):
				if ((i!=choice) & (lista[i]!='GOAT_MONTY')):
				return lista[i]

#Se crean dos listas, en donde una guarda el resultado de cambiar la puerta y el otro de no cambiarla.
listatrue=[]
listafalse=[]

for i in range(100):
	numero = choose_door()
	listatrue.append(finish_game(reveal_door(sort_doors(), numero), numero, True))
	listafalse.append(finish_game(reveal_door(sort_doors(), numero), numero, False))

#Se cuenta el numero de veces que se gano cambiando la puerta.
contadorv = 0
for i in range (len(listatrue)): 
 
	if(listatrue[i] == 'car'):
		contadorv= contadorv+ 1  			
print contadorv,"%"

#Se cuenta el numero de veces que se gano no cambiando la puerta.
contadorf = 0 
for i in range(len(listafalse)):
	
	if(listafalse[i] == 'car'):
		contadorf = contadorf+1
print contadorf,"%"








