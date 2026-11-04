import random

print(input('press enter to start: '))

while True:
    hand = [random.randint(1, 6) for _ in range(5)]
    print('your hand: ', hand)

