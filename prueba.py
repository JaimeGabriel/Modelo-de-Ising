import numpy as np

N_vec = np.genfromtxt('Input/Input.csv', delimiter=',', dtype=np.int64, max_rows=1)[1:]

print(N_vec)

data = np.genfromtxt('Input/Input.csv', delimiter=',', dtype=np.float64, skip_header=1, usecols=(1,))

print(data)
