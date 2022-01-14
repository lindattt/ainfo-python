range(3)
print(range(3))

for i in range(1,10,2):
  print(i)

for i in range(-1, -10, -1):
   print(i) # For negative lists

for i in range(70, 60):
  print(i) # Nothing is printed

for i in range(10, 60, 70):
  print(i) # Only start is printed



# zip 1
a = ("Marco", "Luca", "Claudio")
b = ("Giovanna", "Maria", "Anna", "Francesca")
x = zip(a, b)
print(tuple(x))


# zip 2
coordinate = ['x', 'y', 'z'] 
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

c, v = zip(*result_list) 
print('c =', c)
print('v =', v)