import matplotlib.pyplot as plt
import numpy as np
import scipy.io
import os

dataset_name = "signal1.mat"
dataset_path = os.path.join(os.getcwd(), "datasets", dataset_name)
sig = scipy.io.loadmat(dataset_path)
print(sig)

plt.plot(sig['X051_DE_time'][:2000], 'black')

plt.show()