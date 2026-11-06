import random

hand = [random.randint(1, 6) for _ in range(5)]

print(hand)

while True: 

    try:
        change = input('які кубики замінити? ').split()

        for x in change:
            x = int(x) - 1
            hand[x] = random.randint(1, 6)
        
        break

    except IndexError:
        print('Error: pishi ot 1 do 6')

    except ValueError: 
        print('Error: pishi chislo')

num = 0

for i in hand:
    num += 1
    print("Nomer", num, ":", i)
