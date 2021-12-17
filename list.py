#slides 31-35 python2.pdf,  lezione 6


l1 = [1,2,3]
print(l1, l1[1])
print()


l2 = range(10)
l22 = list(range(10))
l3 = range(1,10)
print(l2, l3, l22)
print()

l3 = [1,2,3,4,5,6,7,8,9]
print(l2[5:8])
print()
l4 = [0] + l3 # non va
l5 = [1,2] + [3,4]
print(l4, l5)
print()

b = [el*2 for el in l3]
print(b)
print()

print(min(b),max(b), len(b))




# tempo, efficienza
import time
#l=list(range(100000000))
#v=list(range(1000000))
#T1=time.clock()
#s=l+v
#print(s)
#T2=time.clock()
#print('concat execution time:', T2-T1)
#T3=time.clock()
#l.extend(v)
#T4=time.clock()
#print('extend execution time:', T4-T3)


