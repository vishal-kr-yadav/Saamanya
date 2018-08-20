import numpy as np

given_list = np.array([1, 2, 3, 4])
np.save('numpy_list.npy', given_list)
read_numpy_list = np.load('numpy_list.npy')
print(read_numpy_list.tolist())

# this is platform independent
