import numpy as np

#uso di SHAPE e NDIM
a=np.array([[1,2],[2,2]])
print(a.shape)
print(a.ndim)

b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b.shape)
print(b.ndim)
print()

#creazione array
a = np.array([11,22,33,99])
print(a)
list1 = [1,2,3,4]
tupla = (5,6,7,8)
a = np.array(list1)
b = np.array(tupla)
c = np.array([list1,tupla])
print(a)
print(b)
print(c)
e = np.arange( 2,20,2, dtype=None )
print(e)
print()

#altre creazioni array
d=np.zeros( (2,2), dtype=float, order ='C')
print(d)
print()

# OPERAZIONI con array: v. note

#RESHAPE RESIZE
a=np.arange(20)
print("prima del resize:")
print(a)
a.resize(5,6)
print("dopo il resize:")
print(a)
print()

a=np.arange(20)
a.reshape((5,4))
print("shape (5,4):")
print(a)
a.reshape((4,5))
print("dopo il reshape (4,5):")
print(a)
#?????
