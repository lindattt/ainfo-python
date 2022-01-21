import numpy as np

a = np.arange(0,4*np.pi,0.1)

#VECTORIZED VERSION 
yv = np.sin(a)*2
print(yv)

#SCALAR VERSION 
ys = np.zeros(len(a))
for i in range(len(a)):
  ys[i]=np.sin(a[i])*2
print(ys)