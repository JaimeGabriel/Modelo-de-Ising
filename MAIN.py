from concurrent.futures import *
import time

from Ising import *

def main():

    start=time.time()   # Comienza a contar el tiempo de ejecución

    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------INPUT--------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    #Vector con distintos tamaños de red para hacer varios seguidos
    N_vec = np.genfromtxt('Input/Input.csv', delimiter=',', dtype=np.int64, max_rows=1)[1:]
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

    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------LOOP O ONE TEMP----------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------    

    if loop_T == 1:
        N=N_vec[0]
        print("Se ha entrado en el caso de una sola temperatura.")
        One_Temp(N, N_calentar, N_med, N_mover, una_temp, B, pintar_intermedios)
    else:
        print("Se ha entrado en el caso de varias temperaturas.")
        #Para ejecutarlo solo una vez y dejarlo que haga varios tamaños de red
        for N in N_vec:
            print("Bucle para N =", N)
            N_mover_spin = N_mover*N**2
            N_calentar_spin = N_calentar*N**2
            Loop_Temp(N, N_calentar_spin, N_med, N_mover_spin, temp_i, temp_f, loop_T, B, pintar_intermedios)
    
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------FIN----------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------- 

    print("------------------------------------------------------------------")
    print("Duración de la simulación: ", time.time()-start, "segundos")
    print("------------------------------------------------------------------")
    print("MAGNETO")
    print("""              ⣀⣤⣴⣶⣶⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢀⣴⡿⢛⣿⣿⣿⣿⣿⣿⣿⣿⡛⢿⣦⡀⠀⠀⠀
    ⠀⠀⣰⣿⡟⠀⠀⣿⣿⠿⠛⠛⠿⣿⣿⠀⠀⢻⣿⣆⠀⠀
    ⠀⣰⣿⣿⣿⡀⠀⠹⣿⠀⠀⠀⠀⣿⠏⠀⢀⣿⣿⣿⣧⠀
    ⢠⣿⣿⣿⣿⣿⣦⣤⣘⣇⠀⠀⣸⣁⣤⣴⣿⣿⣿⣿⣿⡄
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⠟⡛⠛⠻⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣇⠀⠚⠛⠓⠈⠛⠛⠁⠚⠛⠓⠀⣹⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣷⣤⣤⣄⠀⠀⠀⠀⣠⣤⣤⣾⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⠘⠻⠿⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⣿⣿⣿⣿⣿⣿⠿⠟⠃
    ⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠉⠋⠉⠉⠀⠀⠀⠀⠀""")


if __name__ == '__main__':
    main()