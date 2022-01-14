# metodi per leggere matrice da file txt

# metodo numpy: funziona
import numpy as np
input = np.loadtxt("matriceinput.txt", dtype='i', delimiter=',')
print(input)


# non funziona, vedi ian (screen)
l = []
with open('matriceinput.txt', 'r') as f:
  for line in f:
    line = line.strip()
    if len(line) > 0:
      l.append(list(map(int, line.split(','))))
      #l.append(map(int, line.split(','))) # non funziona, serve list
print(l)


# non funziona
fin = open('matriceinput.txt','r') 
a=[]
for line in fin.readlines():
  a.append( [ int (x) for x in line.split(',') ] )