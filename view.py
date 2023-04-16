import numpy as np

# Load the .npy file
data = np.load('arr_0.npy')

# Print the data
print(data[0][0][0])
print(data.shape)
