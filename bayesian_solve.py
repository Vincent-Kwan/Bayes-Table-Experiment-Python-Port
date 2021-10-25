import numpy as np

x,y = np.meshgrid(np.linspace(0,1,11),np.linspace(0,1,11))

x = x.flatten()
y = y.flatten()

xypos = np.stack((x,y), axis = 1)
print(len(xypos))