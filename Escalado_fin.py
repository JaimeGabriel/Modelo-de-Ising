import numpy as np
import matplotlib.pyplot as plt

def finito(T, T_c, nu_0, N, gamma_0, sus):

    inv_nu_0 = 1/nu_0
    t = (T-T_c)/T_c
    x = N**(inv_nu_0)*t
    sus_esc = N**(-gamma_0 * inv_nu_0) * sus
    np.savetxt('Data/t - sus_esc.csv', np.column_stack((t, sus_esc)), delimiter=',')

    """ plt.plot(T, sus, alpha = 1, lw = 3, label = 'Sin interpolar', color = 'purple')
    plt.plot(t, sus_interpolado, alpha = 1, lw = 3, label = 'Interpolado', color = 'blue')
    plt.title("Susceptibilidad")
    plt.legend()
    plt.ylabel("Susceptibilidad")
    plt.xlabel("Temperaturas")
    plt.savefig('./Graphics/Interpolacion_prueba.pdf', bbox_inches = 'tight')
    plt.close() """


    plt.plot(t, sus_esc, alpha = 1, lw = 3, label = 'con t', color = 'blue')
    plt.plot(x, sus_esc, alpha = 1, lw = 3, label = 'con x', color = 'orange')
    plt.legend()
    plt.title("Susceptibilidad")
    plt.xlim([-5, 6])
    plt.ylabel("Susceptibilidad")
    plt.xlabel("Temperatura (t)")
    plt.savefig('./Graphics/sus_esc respecto x y t.pdf', bbox_inches = 'tight')
    plt.close()

    plt.plot(x, sus_esc, alpha = 1, lw = 3, label = 'con x', color = 'orange')
    plt.scatter(x, sus_esc, alpha = 1, lw = 3, label = 'con x', color = 'blue')
    plt.legend()
    plt.title("Figura 8.6")
    plt.xlim([-5, 6])
    plt.ylabel("Función susceptibilidad escalada")
    plt.xlabel("$L^{1/nu}t$")
    plt.savefig('./Graphics/Graph8_6.pdf', bbox_inches = 'tight')
    plt.close()
    

    return np.array([x, sus_esc])


