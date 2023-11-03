import numpy as np

path = "data/data.csv"

rows = 10**6
columns = 10

data = np.random.rand(rows, columns)

np.savetxt(path, data, delimiter=",")
