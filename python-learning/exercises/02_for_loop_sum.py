import random

hand = [5, 4, 6, 3, 2]

for number in hand:
    print('your hand: ', number)

suma = 0
for number in hand:
    suma += number

print('suma: ', suma)

numer = 0

for die in hand:
    numer += 1
    print('kybik ', numer, die)
