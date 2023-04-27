import numpy as np

#Resto de variables
list_Input = np.genfromtxt('Input/Input.csv', delimiter=',', dtype=np.float64, skip_header=1, usecols=(1,))

N_mover=int(list_Input[0]) # Número de veces que movemos antes de medir
N_med=int(list_Input[1])   # Número de veces que medimos
N_calentar=int(list_Input[2])  # Número de movimientos de calentamiento
B = list_Input[3] # Campo externo (B=\mu H)
pintar_intermedios = bool(int(list_Input[4])) # Variable que nos dice si pintar los pasos intermedios o no
loop_T = int(list_Input[5]) # Cantidad de puntos en los que se ejecuta el loop de temperaturas
temp_i = list_Input[6]
temp_f = list_Input[7]
una_temp = list_Input[8]
T_c = list_Input[9]
nu = list_Input[10]