a = 1
b = 0
c = 0

control = True

while control:
    s = input('Enter something:')
    if s == 'q':
        break


while (a == 1):
    s = input('Enter something:')
    if s == 'q':
        break

print(list(range(1,5)))

for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')


number = 23; running = True
while running:
    guess = int(input('Enter an integer:'))
    if guess == number:
        print('Congratulations, you guessed it.') # this causes the while loop to stop
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
    # Do anything else you want to do here
    print('Done')


while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
print('Input is of sufficient length')


a = iter(list(range(10)))

for i in a:
    print(i, next(a))
