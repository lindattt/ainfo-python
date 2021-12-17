my_dict = {'name': 'Alice', 'age': 29, 1: [2, 4, 3]}

#print(my_dict[name])
print(my_dict['name'])
print(my_dict.get('age'))

#modifica
my_dict['age']=30
print(my_dict['age'])
my_dict['address']='The Nederlands'
print(my_dict)
print(len(my_dict))
my_dict.pop(1)
print(my_dict)