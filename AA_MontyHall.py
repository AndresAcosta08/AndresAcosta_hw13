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
				if (i!=choice & i!='GOAT_MONTY'):
					return lista[i]


for i in range(100):


	








