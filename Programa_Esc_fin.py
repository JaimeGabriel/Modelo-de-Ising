from Escalado_fin import *
import numpy as np
import matplotlib.pyplot as plt

N = 10
T_c = 2.27
nu_0 = 1
gamma_0 = 1.76


data = np.loadtxt('./Data/Promedios(T).csv', delimiter=',')
Sus_vec = data[:, 4]
T = data[:, 0]
k=0
plotSus = finito(T, T_c, nu_0, N, gamma_0, Sus_vec)


np.savetxt('Data/plotsus.csv', np.transpose(plotSus), delimiter=',')
plt.plot(plotSus[0], plotSus[1], alpha = 1, lw = 3, label = 'Susceptibilidad', color = 'purple')
plt.title("Susceptibilidad")
plt.ylabel("Susceptibility scaling function")
plt.xlabel("$L^{(1/nu)}*t$")
plt.savefig('./Graphics/Sus_escalado_N20.pdf', bbox_inches = 'tight')
plt.close()




